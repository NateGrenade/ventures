#!/usr/bin/env python3
"""Select which frontier cells to sweep next. This is the ONLY thing that decides where agents look."""
import argparse, datetime, errno, hashlib, json, os, sys, time
import nichelib as nl

LOCK_STALE_SECONDS = 120


class SelectionLock:
    """Serializes select-then-claim across coordinators.

    Timestamp comparison alone leaves a window: the losing orchestrator can re-read the
    ledger before the winner's append lands, see only its own claim, and keep the cell.
    An O_EXCL lock file closes it — only one process is selecting at a time, so the ledger
    it reads already contains every claim made before it started.

    Stale locks (a process that died holding it) are broken after LOCK_STALE_SECONDS."""

    def __init__(self, path, timeout=30):
        self.path, self.timeout, self.fd = path, timeout, None

    def __enter__(self):
        deadline = time.time() + self.timeout
        while True:
            try:
                self.fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                os.write(self.fd, f"{os.getpid()} {datetime.datetime.now().isoformat()}\n".encode())
                return self
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
                try:
                    age = time.time() - os.path.getmtime(self.path)
                    if age > LOCK_STALE_SECONDS:
                        print(f"# breaking stale selection lock ({age:.0f}s old)", file=sys.stderr)
                        os.unlink(self.path)
                        continue
                except FileNotFoundError:
                    continue
                if time.time() > deadline:
                    raise SystemExit("another coordinator has held the selection lock for "
                                     f"{self.timeout}s — retry, or delete {self.path} if stale")
                time.sleep(0.4)

    def __exit__(self, *exc):
        if self.fd is not None:
            os.close(self.fd)
            try:
                os.unlink(self.path)
            except FileNotFoundError:
                pass

CLAIM_TTL_HOURS = 6

def _live_claims():
    """Claim records that are still in force, i.e. not superseded by a later release.

    A release must invalidate the claim that preceded it, for both the blocking check and
    the earliest-claim tiebreak. Without that, a released cell is selectable but then loses
    the tiebreak to its own stale claim and gets yielded straight back."""
    last_release = {}
    records = nl.jsonl(nl.FRONTIER / "ledger.jsonl")
    for r in records:
        if r.get("type") == "release":
            cid, ts = r["cell_id"], r.get("ts", "")
            if ts > last_release.get(cid, ""):
                last_release[cid] = ts
    return [r for r in records
            if r.get("type") == "claim" and r.get("ts", "") > last_release.get(r["cell_id"], "")]


def claimed_recently(ttl_hours):
    """Cell IDs claimed by a still-running batch.

    cells.jsonl is only rolled up after a batch finishes, so last_swept stays null for the
    whole run and every orchestrator that asks gets handed the same never-swept cells.
    Claims are appended to the same append-only ledger. This is NOT fully race-free: two
    orchestrators can both read the pre-claim state and pick overlapping cells before either
    writes (check-then-act). It shrinks the window rather than closing it, and --claim then
    resolves the overlap after the fact by comparing claim timestamps — the earlier claim
    keeps the cell, the later one drops it."""
    cutoff = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=ttl_hours)
    out = set()
    for r in _live_claims():
        try:
            ts = datetime.datetime.fromisoformat(r["ts"])
        except Exception:
            continue
        if ts >= cutoff:
            out.add(r["cell_id"])
    return out

def spread(cell_id):
    """Stable pseudo-random ordering. Never-swept cells sorted by ID would walk the taxonomy
    alphabetically — the first month would be nothing but agriculture. Hashing scatters the
    queue across sectors while staying deterministic, so the same cell always sorts the same
    way and reruns are reproducible."""
    return hashlib.sha1(cell_id.encode()).hexdigest()

def priority(c):
    # never-swept first, scattered across the taxonomy; then stale + historically productive
    if c.get("last_swept") is None:
        return (0, 0, spread(c["cell_id"]))
    cost = max(c.get("est_cost_usd", 0.0), 0.01)
    yield_per_dollar = c.get("promoted_yielded", 0) * 10 + c.get("ideas_yielded", 0)
    return (1, -(yield_per_dollar / cost), c.get("last_swept", ""))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--count", type=int, default=8)
    ap.add_argument("--taxonomy"); ap.add_argument("--json", action="store_true")
    ap.add_argument("--claim", metavar="AGENT_ID",
                    help="record a claim on the selected cells so concurrent orchestrators "
                         "do not re-select them before the batch rolls up")
    ap.add_argument("--ttl", type=float, default=CLAIM_TTL_HOURS,
                    help=f"hours a claim blocks reselection (default {CLAIM_TTL_HOURS})")
    ap.add_argument("--ignore-claims", action="store_true",
                    help="select as if nothing were claimed (use to recover abandoned cells)")
    a = ap.parse_args()
    cells = nl.jsonl(nl.FRONTIER / "cells.jsonl")
    if not cells:
        raise SystemExit("frontier/cells.jsonl is empty — run scripts/bootstrap.py first")
    if a.taxonomy:
        cells = [c for c in cells if c["taxonomy"].lower() == a.taxonomy.lower()]
    lock = SelectionLock(nl.FRONTIER / ".selection.lock") if a.claim else None
    if lock:
        lock.__enter__()
    try:
        picked = _select(a, cells)
    finally:
        if lock:
            lock.__exit__()

    if a.json:
        print(json.dumps(picked, indent=2))
    else:
        for c in picked:
            print(c["cell_id"])


def _select(a, cells):
    if not a.ignore_claims:
        held = claimed_recently(a.ttl)
        cells = [c for c in cells if c["cell_id"] not in held]
        if not cells:
            raise SystemExit(f"every candidate cell is claimed by a batch in the last "
                             f"{a.ttl}h — wait, or pass --ignore-claims")
    picked = sorted(cells, key=priority)[: a.count]

    if a.claim:
        now = datetime.datetime.now(datetime.timezone.utc).isoformat()
        for c in picked:
            nl.jsonl_append(nl.FRONTIER / "ledger.jsonl",
                            {"type": "claim", "cell_id": c["cell_id"],
                             "agent": a.claim, "ts": now})

        # Belt to the lock's braces: were a lock ever bypassed, the earlier claim still
        # wins, so both coordinators converge on disjoint sets rather than duplicating.
        earliest = {}
        for r in _live_claims():
            cur = earliest.get(r["cell_id"])
            if cur is None or (r["ts"], r["agent"]) < cur:
                earliest[r["cell_id"]] = (r["ts"], r["agent"])
        lost = [c["cell_id"] for c in picked
                if earliest.get(c["cell_id"], (now, a.claim))[1] != a.claim]
        if lost:
            picked = [c for c in picked if c["cell_id"] not in lost]
            print(f"# yielded {len(lost)} cell(s) claimed first by another orchestrator: "
                  f"{', '.join(lost)}", file=sys.stderr)

    return picked

if __name__ == "__main__":
    main()
