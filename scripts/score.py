#!/usr/bin/env python3
"""Compute the composite scrutiny score. Models emit anchored field values; this does the arithmetic.

Kept out of model context deliberately — LLMs drift generous on weighted averages across a batch.
"""
import argparse
import nichelib as nl

WEIGHTS = {"pain_evidence":3,"buyer_clarity":3,"incumbent_gap":2,
           "reachability":2,"tractability":2,"persistence_quality":3}
MAXV = 3
THRESHOLD = 62
GOOD_PERSISTENCE = {"recently-unlocked","genuinely-hard"}

def composite(scores):
    total = sum(WEIGHTS[k] * int(scores.get(k, 0)) for k in WEIGHTS)
    return round(100 * total / (MAXV * sum(WEIGHTS.values())))

def gates(meta):
    s = meta.get("scores") or {}
    fails = []
    if (meta.get("evidence_tier") or 9) > 2: fails.append("no Tier 1/2 evidence")
    if (meta.get("source_count") or 0) < 2: fails.append("fewer than 2 sources")
    if not meta.get("buyer_role"): fails.append("no named buyer role")
    if meta.get("persistence") not in GOOD_PERSISTENCE:
        fails.append(f"persistence={meta.get('persistence')!r} not eligible")
    missing = [k for k in WEIGHTS if k not in s]
    if missing: fails.append(f"missing scores: {missing}")
    return fails

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug"); ap.add_argument("--all", action="store_true")
    ap.add_argument("--recompute", action="store_true")
    a = ap.parse_args()
    targets = ([(nl.IDEAS / f"{a.slug}.md",) + nl.read_idea(nl.IDEAS / f"{a.slug}.md")] if a.slug
               else nl.all_ideas())
    for path, meta, body in targets:
        s = meta.get("scores") or {}
        c = composite(s)
        meta["composite"] = c
        f = gates(meta)
        meta["gate_pass"] = not f
        nl.write_idea(path, meta, body)
        verdict = "PROMOTE-ELIGIBLE" if (not f and c >= THRESHOLD) else "DEMOTE"
        print(f"{path.name}: {c}/100 threshold={THRESHOLD} -> {verdict}")
        for x in f: print(f"    gate fail: {x}")

if __name__ == "__main__":
    main()
