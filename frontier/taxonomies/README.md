# Taxonomies

The enumerable frontier. These CSVs are committed so a research round needs no local setup —
clone, run `python scripts/bootstrap.py`, sweep.

| File | Source | Cells used | License |
|---|---|---|---|
| `naics.csv` | US Census Bureau, NAICS 2022 | 922 (6-digit only) | Public domain (US government work) |
| `onet-occupations.csv` | O*NET Occupation Data | 1,016 | CC BY 4.0 |

## Attribution

This product uses public information provided by O\*NET® under the Creative Commons
Attribution 4.0 International License. O\*NET® is a trademark of the U.S. Department of
Labor, Employment and Training Administration. Anthropic and the maintainers of this
repository are not affiliated with or endorsed by USDOL/ETA.

## Adding a taxonomy

1. Drop the CSV in this directory.
2. Add an entry to `manifest.json`:

```json
{
  "name": "SIC",
  "file": "sic.csv",
  "code_col": "code",
  "label_col": "description",
  "filter": { "col": "level", "equals": "4" },
  "desc_col": null
}
```

`filter` is optional — use it when the file mixes granularities, as NAICS does.
`desc_col` is optional; when present its text becomes the cell's `hint`, which the sweep
agent reads for free. Prefer taxonomies that have one.

3. Re-run `python scripts/bootstrap.py`. Existing cells and their sweep history are untouched.

## Worth adding later

State professional licensing rosters, trade association member directories, and county
procurement vendor categories. All three are more granular than NAICS and none are
nationally standardized, so they need per-source cleanup — but they point at exactly the
kind of fragmented, unglamorous work this pipeline is looking for.
