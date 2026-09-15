#!/usr/bin/env python3
"""Similarity check against the existing corpus. Run BEFORE writing a new idea file.

Compares the canonical `job:` line from frontmatter, not the document body. Sector
vocabulary is shared by genuinely distinct ideas and absent from genuinely identical ones,
so body-text matching gets this wrong in both directions.

Deliberately lenient about false positives: merging two ideas that were distinct costs
little, while letting the corpus fill with near-duplicates quietly kills this pipeline.
"""
import argparse
import nichelib as nl


def job_of(meta, body):
    """The canonical job line if present, else fall back to the problem statement.

    Comparing whole documents over-merges within a sector (everything in municipal
    utilities shares vocabulary) and under-merges across sectors (the same manual job
    in two industries reads as unrelated). The job line strips both effects."""
    if meta.get("job"):
        return meta["job"]
    return body[:600]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", required=False, help="proposed title")
    ap.add_argument("--summary", default="", help="one-line problem statement")
    ap.add_argument("--threshold", type=float, default=0.45,
                    help="containment for --check; jaccard for --sweep")
    ap.add_argument("--sweep", action="store_true", help="report all near-duplicate pairs in corpus")
    a = ap.parse_args()

    corpus = [(f, m, b) for f, m, b in nl.all_ideas() if m.get("status") != "duplicate"]

    if a.sweep:
        hits = 0
        for i in range(len(corpus)):
            for j in range(i + 1, len(corpus)):
                mi, mj = corpus[i][1], corpus[j][1]
                # deliberate splits share a lineage and must never be auto-remerged
                if mi.get("split_from") and mi.get("split_from") == mj.get("split_from"):
                    continue
                s = nl.jaccard(nl.tokens(nl.canonical(job_of(mi, corpus[i][2]))),
                               nl.tokens(nl.canonical(job_of(mj, corpus[j][2]))))
                if s >= a.threshold:
                    print(f"{s:.2f}  {corpus[i][0].name}  <->  {corpus[j][0].name}"); hits += 1
        print(f"{hits} near-duplicate pair(s) at threshold {a.threshold}")
        return

    if not a.check:
        raise SystemExit("--check or --sweep required")
    probe = nl.tokens(nl.canonical(a.check + " " + a.summary))
    scored = sorted(((nl.overlap(probe, nl.tokens(nl.canonical(job_of(m, b)))), f, m)
                     for f, m, b in corpus), reverse=True, key=lambda t: t[0])
    if scored and scored[0][0] >= a.threshold:
        print(f"NEAR-MATCH ({scored[0][0]:.2f}) -> {scored[0][1].name}")
        print("Do not create a new file. Append evidence under '## Additional Evidence' there.")
    else:
        top = f" (closest {scored[0][0]:.2f} {scored[0][1].name})" if scored else ""
        print(f"NO MATCH — safe to create{top}")

if __name__ == "__main__":
    main()
