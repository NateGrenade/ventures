#!/usr/bin/env python3
"""Yield-per-dollar by frontier cell and taxonomy. Feed into next_cells.py policy monthly.

This is the file that makes month six smarter than week one.
"""
from collections import defaultdict
import nichelib as nl

def main():
    cells = {c["cell_id"]: c for c in nl.jsonl(nl.FRONTIER / "cells.jsonl")}
    stat = defaultdict(lambda: {"ideas":0,"promoted":0,"validated":0,"accepted":0,"cost":0.0})
    for _, m, _ in nl.all_ideas():
        cid = m.get("cell_id","?"); s = stat[cid]
        s["ideas"] += 1
        s["cost"] += float(m.get("cost_usd") or 0)
        if m.get("status") in ("promoted","validated"): s["promoted"] += 1
        if m.get("status") == "validated": s["validated"] += 1
        if m.get("human_verdict") == "accept": s["accepted"] += 1
    for cid, c in cells.items():
        stat[cid]["cost"] += float(c.get("est_cost_usd") or 0)

    print(f"{'cell':<20}{'ideas':>6}{'prom':>6}{'valid':>6}{'acc':>5}{'cost':>9}{'$/prom':>9}  label")
    rows = sorted(stat.items(), key=lambda kv: -(kv[1]["promoted"] / max(kv[1]["cost"], .01)))
    for cid, s in rows:
        per = s["cost"] / s["promoted"] if s["promoted"] else float("inf")
        per_s = f"{per:8.2f}" if s["promoted"] else "       –"
        label = cells.get(cid, {}).get("label", "")[:34]
        print(f"{cid:<20}{s['ideas']:>6}{s['promoted']:>6}{s['validated']:>6}"
              f"{s['accepted']:>5}{s['cost']:>9.2f}{per_s}  {label}")

    tax = defaultdict(lambda: [0,0,0.0])
    for cid, s in stat.items():
        t = cells.get(cid, {}).get("taxonomy", "?")
        tax[t][0] += s["ideas"]; tax[t][1] += s["promoted"]; tax[t][2] += s["cost"]
    print("\nBy taxonomy:")
    for t, (i, p, c) in tax.items():
        print(f"  {t:<8} ideas={i:<5} promoted={p:<5} cost=${c:.2f}  "
              f"promotion rate={100*p/i if i else 0:.1f}%")
    print("\nReweight next_cells.py toward high-yield taxonomies. Watch promotion rate: a rise "
          "without a matching rise in accepted/ means the critic has gone soft.")

if __name__ == "__main__":
    main()
