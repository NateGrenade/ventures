#!/usr/bin/env python3
"""Print one cell's label, hint, and sweep history. Sweep agents call this instead of
loading frontier/cells.jsonl, which is ~1,900 lines and would dwarf the rest of their context."""
import argparse, json
import nichelib as nl

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cell_id")
    a = ap.parse_args()
    for c in nl.jsonl(nl.FRONTIER / "cells.jsonl"):
        if c["cell_id"] == a.cell_id:
            print(f"cell_id:   {c['cell_id']}")
            print(f"taxonomy:  {c['taxonomy']}")
            print(f"label:     {c['label']}")
            if c.get("hint"):
                print(f"hint:      {c['hint']}")
            print(f"history:   swept {c['sweep_count']}x, last {c['last_swept'] or 'never'}, "
                  f"{c['ideas_yielded']} ideas, ${c['est_cost_usd']:.2f} spent")
            if c.get("notes"):
                print(f"notes:     {c['notes']}")
            return
    raise SystemExit(f"unknown cell_id: {a.cell_id}")

if __name__ == "__main__":
    main()
