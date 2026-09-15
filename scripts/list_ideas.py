#!/usr/bin/env python3
"""List idea files by status. Keeps agents from globbing the whole corpus into context.

Truncation is always announced. An earlier version defaulted to 25 results and printed a
footer that looked identical whether or not more existed, so a scrutiny pass over 45 ideas
would process 25, see a clean footer, and stop — leaving 20 silently ungraded. Output now
states the total and, when truncated, says plainly that it is.
"""
import argparse
import nichelib as nl

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--status", default="sandbox")
    ap.add_argument("--limit", type=int, default=0, help="0 = no limit (default)")
    ap.add_argument("--offset", type=int, default=0)
    ap.add_argument("--paths", action="store_true")
    ap.add_argument("--count-only", action="store_true")
    a = ap.parse_args()

    allrows = nl.all_ideas(status=a.status)
    total = len(allrows)
    if a.count_only:
        print(total); return

    rows = allrows[a.offset:]
    truncated = bool(a.limit) and len(rows) > a.limit
    if a.limit:
        rows = rows[: a.limit]

    for f, m, _ in rows:
        print(str(f) if a.paths else
              f"{m.get('slug', f.stem):<44} cell={m.get('cell_id','-'):<18} "
              f"tier={m.get('evidence_tier','-')}")

    shown = a.offset + len(rows)
    print(f"-- status={a.status}: {total} total, showing {len(rows)} "
          f"({a.offset + 1}-{shown})" if rows else f"-- status={a.status}: {total} total, none shown")
    if truncated or shown < total:
        print(f"-- TRUNCATED: {total - shown} more not shown. "
              f"Re-run with --offset {shown} to continue, or --limit 0 for all.")

if __name__ == "__main__":
    main()
