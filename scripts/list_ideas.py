#!/usr/bin/env python3
"""List idea files by status. Keeps agents from globbing the whole ideas/ directory into context."""
import argparse
import nichelib as nl

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--status", default="sandbox"); ap.add_argument("--limit", type=int, default=25)
    ap.add_argument("--paths", action="store_true")
    a = ap.parse_args()
    rows = nl.all_ideas(status=a.status)[: a.limit]
    for f, m, _ in rows:
        print(str(f) if a.paths else
              f"{m.get('slug', f.stem):<40} cell={m.get('cell_id','–'):<18} tier={m.get('evidence_tier','–')}")
    print(f"-- {len(rows)} shown, status={a.status}")

if __name__ == "__main__":
    main()
