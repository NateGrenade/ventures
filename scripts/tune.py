#!/usr/bin/env python3
"""Tune the scoring configuration against the corpus you actually have.

    python scripts/tune.py                    # diagnose the active profile
    python scripts/tune.py --target-rate 0.15 # what threshold yields ~15% promotion
    python scripts/tune.py --compare          # all profiles side by side

Never writes to idea files. Reports only.

The number to watch is not the composite distribution — it is which GATE fires most. A
threshold is only the binding constraint if most ideas clear every gate. If half the corpus
fails on an undetermined revenue ceiling, moving the threshold changes nothing, and the real
problem is that critics are not doing the buyer-count research.
"""
import argparse
from collections import Counter
import nichelib as nl
import score as sc


def evaluate(cfg):
    rows = []
    for path, meta, _ in nl.all_ideas():
        if meta.get("status") in ("duplicate",):
            continue
        s = dict(meta.get("scores") or {})
        if not s:
            rows.append((path.stem, None, ["unscored"], meta.get("status")))
            continue
        de, _ = sc.deal_economics(meta, cfg)
        s["deal_economics"] = de
        rows.append((path.stem, sc.composite(s, cfg), sc.gates(dict(meta, scores=s), cfg),
                     meta.get("status")))
    return rows


def histogram(scores, width=44):
    if not scores:
        return
    buckets = Counter(min(int(x // 10) * 10, 90) for x in scores)
    top = max(buckets.values())
    print("\ncomposite distribution")
    for lo in range(0, 100, 10):
        n = buckets.get(lo, 0)
        bar = "#" * int(round(width * n / top)) if n else ""
        print(f"  {lo:>3}-{lo+9:<3} {n:>3} {bar}")


def report(cfg, rows, target=None):
    scored = [r for r in rows if r[1] is not None]
    unscored = len(rows) - len(scored)
    clean = [r for r in scored if not r[2]]
    print(f"profile: {cfg['profile']}   threshold: {cfg['threshold']}")
    print(f"corpus: {len(rows)} ideas ({unscored} unscored, {len(scored)} scored)")
    if not scored:
        print("\nNothing scored yet — run niche-scrutiny before tuning.")
        return

    gate_counts = Counter(g.split(" —")[0].split(" (")[0] for r in scored for g in r[2])
    print(f"\n{len(clean)}/{len(scored)} scored ideas clear every gate.")
    if gate_counts:
        print("gate failures (an idea can fail several):")
        for g, n in gate_counts.most_common():
            print(f"  {n:>3}  {g[:74]}")

    histogram([r[1] for r in scored])

    promoted = [r for r in clean if r[1] >= cfg["threshold"]]
    rate = len(promoted) / len(scored) if scored else 0
    print(f"\nat threshold {cfg['threshold']}: {len(promoted)} promote-eligible "
          f"({rate:.0%} of scored)")

    if not clean:
        print("\nNo idea clears the gates, so the threshold is not your binding constraint.")
        print("Fix the most common gate failure above before touching any number.")
        return

    cs = sorted((r[1] for r in clean), reverse=True)
    print(f"gate-clearing scores: max {cs[0]}, median {cs[len(cs)//2]}, min {cs[-1]}")

    if target is not None:
        want = max(1, round(target * len(scored)))
        if want > len(clean):
            print(f"\nCannot reach a {target:.0%} rate: only {len(clean)} ideas clear the "
                  f"gates at all ({len(clean)/len(scored):.0%}). Relax a floor, not the threshold.")
        else:
            sug = cs[want - 1]
            print(f"\nFor ~{target:.0%} promotion, set threshold to {sug} "
                  f"(promotes {sum(1 for x in cs if x >= sug)} of {len(scored)}).")
            print("Sanity-check by reading the ideas that land just either side of it. If the "
                  "ones just below look better than the ones just above, the weights are wrong "
                  "and no threshold will fix that.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target-rate", type=float, default=None,
                    help="desired share of scored ideas promoting, e.g. 0.15")
    ap.add_argument("--compare", action="store_true", help="run every profile")
    ap.add_argument("--profile", help="evaluate one named profile without changing the config")
    a = ap.parse_args()

    if not a.compare:
        cfg = nl.config(a.profile)
        report(cfg, evaluate(cfg), a.target_rate)
        return

    # Read-only: every profile is loaded by name. The config file is never written.
    for i, name in enumerate(nl.profiles()):
        if i:
            print("\n" + "-" * 70)
        cfg = nl.config(name)
        report(cfg, evaluate(cfg), a.target_rate)


if __name__ == "__main__":
    main()
