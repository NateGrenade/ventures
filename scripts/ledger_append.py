#!/usr/bin/env python3
"""Append a sweep record and update the cell's rollup counters. Append-only JSONL merges cleanly in git."""
import argparse, json
import nichelib as nl

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cell", required=True); ap.add_argument("--agent", default="manual")
    ap.add_argument("--stubs", type=int, default=0); ap.add_argument("--merged", type=int, default=0)
    ap.add_argument("--cost", type=float, default=0.0); ap.add_argument("--note", default=None)
    a = ap.parse_args()
    nl.jsonl_append(nl.FRONTIER / "ledger.jsonl",
                    {"cell_id": a.cell, "date": nl.today(), "agent": a.agent,
                     "stubs": a.stubs, "merged": a.merged, "cost_usd": a.cost, "note": a.note})
    path = nl.FRONTIER / "cells.jsonl"
    cells = nl.jsonl(path); found = False
    for c in cells:
        if c["cell_id"] == a.cell:
            c["last_swept"] = nl.today(); c["sweep_count"] = c.get("sweep_count", 0) + 1
            c["ideas_yielded"] = c.get("ideas_yielded", 0) + a.stubs
            c["est_cost_usd"] = round(c.get("est_cost_usd", 0.0) + a.cost, 4)
            if a.note: c["notes"] = a.note
            found = True
    if not found:
        raise SystemExit(f"unknown cell_id {a.cell}")
    with open(path, "w", encoding="utf-8") as fh:
        for c in cells: fh.write(json.dumps(c) + "\n")
    print(f"ledger: {a.cell} +{a.stubs} stubs, ${a.cost}")

if __name__ == "__main__":
    main()
