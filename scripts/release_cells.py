#!/usr/bin/env python3
"""Release claimed cells once a batch has finished with them.

Claims otherwise block reselection for their full TTL (6h by default), so a coordinator that
finishes in 40 minutes leaves the frontier artificially narrow for another five hours.
Releasing is append-only and safe to run concurrently.
"""
import argparse, datetime
import nichelib as nl

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cells", nargs="+", help="cell IDs to release")
    ap.add_argument("--agent", default="manual")
    a = ap.parse_args()
    for cid in a.cells:
        nl.jsonl_append(nl.FRONTIER / "ledger.jsonl",
                        {"type": "release", "cell_id": cid, "agent": a.agent,
                         "ts": datetime.datetime.now(datetime.timezone.utc).isoformat()})
    print(f"released {len(a.cells)} cell(s)")

if __name__ == "__main__":
    main()
