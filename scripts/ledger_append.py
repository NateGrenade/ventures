#!/usr/bin/env python3
"""Append one sweep record. APPEND-ONLY and therefore safe under concurrency.

This script deliberately does NOT touch frontier/cells.jsonl. That file is a rollup, and
rewriting it from N concurrent subagents is a lost-update race: each one reads the whole
file, edits one line, and writes it back, so the last writer silently erases the others.
Counters are recomputed from this ledger by rollup_cells.py after a batch completes.
"""
import argparse
import nichelib as nl

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cell", required=True); ap.add_argument("--agent", default="manual")
    ap.add_argument("--stubs", type=int, default=0); ap.add_argument("--merged", type=int, default=0)
    ap.add_argument("--cost", type=float, default=0.0); ap.add_argument("--note", default=None)
    ap.add_argument("--sources", default=None,
                    help="comma-separated source types that actually yielded evidence, "
                         "e.g. job-posting,procurement")
    a = ap.parse_args()

    known = {c["cell_id"] for c in nl.jsonl(nl.FRONTIER / "cells.jsonl")}
    if a.cell not in known:
        raise SystemExit(f"unknown cell_id {a.cell}")

    nl.jsonl_append(nl.FRONTIER / "ledger.jsonl", {
        "cell_id": a.cell, "date": nl.today(), "agent": a.agent,
        "stubs": a.stubs, "merged": a.merged, "cost_usd": a.cost,
        "yield_sources": [s.strip() for s in a.sources.split(",")] if a.sources else [],
        "note": a.note,
    })
    print(f"ledger: {a.cell} +{a.stubs} stubs ({a.agent})")

if __name__ == "__main__":
    main()
