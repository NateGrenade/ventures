#!/usr/bin/env python3
"""Select which frontier cells to sweep next. This is the ONLY thing that decides where agents look."""
import argparse, json
import nichelib as nl

def priority(c):
    # never-swept first; then stale + historically productive
    if c.get("last_swept") is None:
        return (0, 0, c["cell_id"])
    cost = max(c.get("est_cost_usd", 0.0), 0.01)
    yield_per_dollar = c.get("promoted_yielded", 0) * 10 + c.get("ideas_yielded", 0)
    return (1, -(yield_per_dollar / cost), c.get("last_swept", ""))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--count", type=int, default=8)
    ap.add_argument("--taxonomy"); ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    cells = nl.jsonl(nl.FRONTIER / "cells.jsonl")
    if not cells:
        raise SystemExit("frontier/cells.jsonl is empty — run scripts/bootstrap.py first")
    if a.taxonomy:
        cells = [c for c in cells if c["taxonomy"].lower() == a.taxonomy.lower()]
    picked = sorted(cells, key=priority)[: a.count]
    if a.json:
        print(json.dumps(picked, indent=2))
    else:
        for c in picked: print(c["cell_id"])

if __name__ == "__main__":
    main()
