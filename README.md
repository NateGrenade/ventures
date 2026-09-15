# Ventures — Niche Hunting Pipeline

A frontier-driven pipeline for finding underserved markets: agents sweep a finite,
enumerable set of industry and occupation cells for evidence of manual operational work,
criticize what they find against sourced rubrics, try to kill the survivors cheaply, and
only then spend real research budget.

**The central design choice:** this does not search the internet for good ideas. Searching
for "underserved markets" returns content written by vendors selling into those markets.
Instead it walks a finite frontier — 1,938 NAICS industry codes and O\*NET occupations —
with a coverage ledger, so progress is measurable and parallel agents never duplicate work.

---

## Quick start

```bash
git clone https://github.com/NateGrenade/ventures.git
cd ventures
pip install pyyaml
python scripts/bootstrap.py      # idempotent; safe to re-run anytime
python scripts/next_cells.py --count 8
```

The frontier is already seeded and committed, so a fresh clone needs no setup beyond
PyYAML. Skills live in `.claude/skills/`, which Claude Code picks up automatically when
run from this directory — nothing to install into `~/.claude`.

Run a batch:

```bash
mkdir -p logs
CELL_COUNT=8 MAX_TURNS=30 ./scripts/driver.sh
```

Use cron, not a daemon. A daemon has no natural stop condition and no audit trail.

---

## The four phases

| Skill | Phase | When it runs | Writes |
|---|---|---|---|
| `niche-sweep` | 1 — evidence gathering | Every batch, once per cell | `ideas/*.md`, ledger |
| `niche-scrutiny` | 2 — triage + sourced critique | Every batch, over `sandbox` | Idea frontmatter, scrutiny logs |
| `niche-falsify` | 3 — cheap disconfirmation | On promotion | Falsification logs, `worklist.md` |
| `niche-dossier` | 4 — deep research | Only when you name an idea | `dossiers/<slug>/` |

Four skills rather than one, for two reasons. Context: a sweep agent loads ~90 lines and
never sees the scoring rubric or the dossier structure, which is the difference between a
batch costing a few dollars and costing thirty. Triggering: one skill described as "find,
evaluate, test, and research niches" matches every query and therefore discriminates
between none.

Status lifecycle: `sandbox → demoted | promoted → falsified | validated → dossier`.
Nothing is ever deleted. Demoted and falsified ideas are how the pipeline learns what your
promotions are systematically wrong about.

---

## Layout

```
frontier/
  cells.jsonl          1,938 seeded cells — the enumerable universe
  ledger.jsonl         append-only sweep records
  taxonomies/          committed source CSVs + manifest (see its README)
ideas/                 one file per candidate, exclusively owned by its agent
merged/                duplicates folded into canonical files
dossiers/<slug>/       Phase 4 output
calibration/
  verdicts.jsonl       your accept/reject decisions
  rubric-notes.md      hand-written; overrides the rubric
worklist.md            human-executed tests, pre-scripted
scripts/               all deterministic work
.claude/skills/        the four skills, versioned with the repo
INDEX.md               GENERATED — never edit by hand
```

---

## Scripts

| Script | Does |
|---|---|
| `bootstrap.py` | Scaffold + seed frontier from `taxonomies/manifest.json`. Idempotent |
| `next_cells.py` | Selects what gets swept. **The only thing deciding where agents look** |
| `show_cell.py` | One cell's label, O\*NET hint, and sweep history |
| `dedup.py` | Containment check before write (`--check`); corpus pair audit (`--sweep`) |
| `verify_sources.py` | Fetches every cited URL, marks dead ones, computes `evidence_tier` |
| `score.py` | Weighted composite from anchored values + hard-gate checks |
| `ledger_append.py` | Appends a sweep record, rolls up cell counters |
| `list_ideas.py` | Lists by status, so agents don't glob the corpus into context |
| `build_index.py` | Regenerates `INDEX.md` |
| `cost_report.py` | Yield-per-dollar by cell and taxonomy |
| `driver.sh` | Batch orchestration |

Anything a model could get wrong by being inconsistent lives here rather than in a prompt:
dedup thresholds, source tiering, score arithmetic, coverage bookkeeping. Agents emit
structured values; scripts decide what those values mean.

---

## Concurrency contract

Why parallel agents don't collide:

1. Each agent writes only `ideas/<its-own-slug>.md` — never another agent's file, except
   appending under `## Additional Evidence`.
2. Shared state is append-only JSONL. Appends merge cleanly in git; edits to a shared
   markdown index do not.
3. `INDEX.md` is generated. No human and no model edits it.
4. Deterministic passes run after `wait`, single-threaded, in the driver.

Past roughly eight concurrent agents, switch to git worktrees per agent.

---

## The calibration loop

There is deliberately no skill for this.

`calibration/rubric-notes.md` is hand-written by you, recording cases where you disagreed
with a rubric outcome. `niche-scrutiny` reads it and is instructed that your notes override
its anchored scales. That is the mechanism by which your taste, rather than the model's
generic priors, becomes the scoring function. Automating it would put a model between your
judgment and the scoring function, which defeats the point.

The metric to watch, from `cost_report.py`: promotion rate rising over successive batches
*without* a matching rise in your acceptance rate. That means the critic has gone soft — a
known drift mode. Raise the threshold in `.claude/skills/niche-scrutiny/references/rubric.md`
and date the change at the bottom of that file.

---

## Build order

Do not stand all four phases up at once. Each depends on what the previous one actually
produces.

1. **Read twenty cells yourself** (`show_cell.py`) and confirm the granularity is right.
   Everything inherits this decision.
2. **`niche-sweep` on ten cells, reviewed by hand.** You are checking whether it finds
   Tier 1 sources or quietly reverts to listicles. Expect two or three prompt rewrites —
   this step determines whether the pipeline is worth running at all.
3. **`dedup.py` and `verify_sources.py` in the loop**, once volume rises.
4. **`niche-scrutiny`**, with the rubric written against real stubs rather than imagined ones.
5. **`niche-falsify`**, after ~20 promoted ideas show which assumptions recur.
6. **`niche-dossier`** last. It runs least often.
7. **Calibration** accumulates from step 2 onward and never stops.

---

## Known unknowns

- **The promotion threshold (62) is a guess.** Retune after ~30 scored ideas.
- **The dedup threshold (0.45 containment) is tuned on two examples.** Run
  `dedup.py --sweep` monthly and adjust.
- **`next_cells.py` policy is simple** — never-swept first (scattered by a stable hash so
  batches don't walk the taxonomy alphabetically), then yield-per-dollar. It has no notion of
  cell *similarity*, so it can't yet avoid sweeping three near-identical occupations in one
  batch. Revisit once `cost_report.py` has real data.
- **The repository is public.** Its output is, by design, a list of markets nobody has built
  in yet. Consider whether that should stay readable by anyone who finds it.
