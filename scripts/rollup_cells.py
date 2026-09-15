#!/usr/bin/env python3
"""Recompute frontier/cells.jsonl counters from the append-only ledger.

Run once after a batch, single-threaded. Derived state, same principle as INDEX.md:
nothing that several agents touch at once is ever mutated in place.

Also reports which evidence source types actually yielded across the corpus, which is the
per-cell observation that otherwise only survives as free text in ledger notes.
"""
import argparse, json
from collections import Counter, defaultdict
import nichelib as nl

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    records = [r for r in nl.jsonl(nl.FRONTIER / "ledger.jsonl")
               if r.get("type", "sweep") != "claim"]
    agg = defaultdict(lambda: {"n": 0, "stubs": 0, "cost": 0.0, "last": None, "note": None})
    for r in records:
        c = agg[r["cell_id"]]
        c["n"] += 1
        c["stubs"] += r.get("stubs", 0)
        c["cost"] += float(r.get("cost_usd") or 0)
        if not c["last"] or r.get("date", "") > c["last"]:
            c["last"] = r.get("date")
            c["note"] = r.get("note") or c["note"]

    promoted = Counter()
    for _, m, _ in nl.all_ideas():
        if m.get("status") in ("promoted", "validated"):
            promoted[m.get("cell_id")] += 1

    path = nl.FRONTIER / "cells.jsonl"
    cells = nl.jsonl(path)
    for c in cells:
        a_ = agg.get(c["cell_id"])
        if not a_:
            continue
        c["last_swept"] = a_["last"]
        c["sweep_count"] = a_["n"]
        c["ideas_yielded"] = a_["stubs"]
        c["est_cost_usd"] = round(a_["cost"], 4)
        c["promoted_yielded"] = promoted.get(c["cell_id"], 0)
        if a_["note"]:
            c["notes"] = a_["note"]
    with open(path, "w", encoding="utf-8") as fh:
        for c in cells:
            fh.write(json.dumps(c, ensure_ascii=False) + "\n")

    swept = sum(1 for c in cells if c.get("last_swept"))
    if a.quiet:
        return
    print(f"rollup: {swept}/{len(cells)} cells swept, {sum(x['stubs'] for x in agg.values())} stubs total")

    st = Counter()
    for r in records:
        for s in r.get("yield_sources", []):
            st[s] += 1
    if st:
        print("source types that yielded evidence:")
        for s, n in st.most_common():
            print(f"  {s:<16} {n} cell(s)")

if __name__ == "__main__":
    main()
