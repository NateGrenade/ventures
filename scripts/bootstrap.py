#!/usr/bin/env python3
"""Scaffold the repo and seed frontier/cells.jsonl from the taxonomy CSVs committed alongside it.

    python scripts/bootstrap.py

Reads frontier/taxonomies/manifest.json and ingests every CSV listed there. No flags needed.
Idempotent: cell_ids already present are skipped, so re-running after adding a taxonomy only
adds what's new and never disturbs sweep history.

To add a taxonomy: drop the CSV in frontier/taxonomies/, add an entry to manifest.json, re-run.
"""
import argparse, csv, json, sys
from pathlib import Path

DIRS = ["frontier", "frontier/taxonomies", "ideas", "merged", "dossiers",
        "calibration", "logs", "scripts"]

NOTES_SEED = """# Rubric Notes

Cases where my judgment diverged from the rubric. Written by hand, by me.
`niche-scrutiny` reads this file and is instructed that these notes override its
anchored scales — this is how my taste becomes the scoring function instead of
the model's generic priors.

Format: date / slug / what the rubric said / what I said / why.

---

"""


def load_manifest(root):
    p = root / "frontier" / "taxonomies" / "manifest.json"
    if not p.exists():
        sys.exit(f"missing {p} — see frontier/taxonomies/README.md")
    return json.loads(p.read_text(encoding="utf-8"))["taxonomies"]


def rows_from(root, t):
    path = root / "frontier" / "taxonomies" / t["file"]
    if not path.exists():
        print(f"  SKIP {t['name']}: {t['file']} not found")
        return []
    out = []
    with open(path, newline="", encoding="utf-8-sig") as fh:
        for r in csv.DictReader(fh, delimiter=t.get("delimiter", ",")):
            f = t.get("filter")
            if f and str(r.get(f["col"], "")).strip() != str(f["equals"]):
                continue
            code = (r.get(t["code_col"]) or "").strip()
            label = (r.get(t["label_col"]) or "").strip()
            if not code or not label:
                continue
            hint = None
            if t.get("desc_col"):
                hint = (r.get(t["desc_col"]) or "").strip()[: t.get("hint_chars", 400)] or None
            out.append({
                "cell_id": f"{t['name'].lower()}-{code}",
                "taxonomy": t["name"],
                "label": label,
                "hint": hint,
                "last_swept": None,
                "sweep_count": 0,
                "ideas_yielded": 0,
                "promoted_yielded": 0,
                "est_cost_usd": 0.0,
                "notes": None,
            })
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    a = ap.parse_args()
    root = Path(a.root).resolve()
    if not (root / "frontier" / "taxonomies").exists() and Path.cwd().name == "scripts":
        root = Path.cwd().parent

    for d in DIRS:
        (root / d).mkdir(parents=True, exist_ok=True)
    for f in ["frontier/ledger.jsonl", "calibration/verdicts.jsonl"]:
        (root / f).touch()
    notes = root / "calibration" / "rubric-notes.md"
    if not notes.exists():
        notes.write_text(NOTES_SEED, encoding="utf-8")

    cells_path = root / "frontier" / "cells.jsonl"
    existing = set()
    if cells_path.exists():
        for line in cells_path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                existing.add(json.loads(line)["cell_id"])

    added = 0
    with open(cells_path, "a", encoding="utf-8") as fh:
        for t in load_manifest(root):
            n = 0
            for cell in rows_from(root, t):
                if cell["cell_id"] in existing:
                    continue
                fh.write(json.dumps(cell, ensure_ascii=False) + "\n")
                existing.add(cell["cell_id"])
                n += 1
            added += n
            print(f"  {t['name']}: +{n} cells")

    print(f"\nFrontier: {len(existing)} cells total ({added} added this run).")
    print("Next:  python scripts/next_cells.py --count 8")


if __name__ == "__main__":
    main()
