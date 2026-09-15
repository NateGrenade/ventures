# Ventures — Niche Hunting Pipeline

A frontier-driven pipeline for finding underserved markets: agents sweep a finite,
enumerable set of industry and occupation cells for evidence of manual operational work,
criticize what they find against sourced rubrics, try to kill the survivors cheaply, and
only then spend real research budget.

**The central design choice:** this does not search the internet for good ideas. Searching
for "underserved markets" returns content written by vendors selling into those markets.
Instead it walks a finite frontier — 1,938 NAICS industry codes and O\*NET occupations —
with a coverage ledger, so progress is measurable. One coordinator assigns disjoint
cells; the ledger alone does not reserve work against overlapping batches.

---

## Quick start

```bash
git clone https://github.com/NateGrenade/ventures.git
cd ventures
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install pyyaml
python3 scripts/bootstrap.py      # idempotent; safe to re-run anytime
python3 scripts/next_cells.py --count 8
```

The frontier is already seeded. Python 3 and PyYAML are the local script dependencies.
Keep the project virtual environment out of version control.

### Interactive Claude Code and Codex

Open this repository as the working project. Claude Code discovers `.claude/skills/`;
Codex discovers the same five skills through relative links in `.agents/skills/`.
`AGENTS.md` provides Codex's project-level guidance. Edit the canonical skills once.

Examples:

- "Use niche-batch to sweep 6 cells."
- "Use niche-sweep on cell onet-43-3011.00."
- "Use niche-scrutiny to evaluate all sandbox ideas."
- "Use niche-falsify to test the promoted ideas."
- "Use niche-dossier for <slug> with <declared budget>."

Codex CLI also supports explicit `$niche-batch` skill mentions. Claude's `/sweep`,
`/scrutinize`, `/falsify`, and named `niche-sweeper` wrapper remain Claude-specific;
Codex uses the shared skills and available native worker tools. Batch sweeps default to
24 cells, with at most six workers and fewer when the host has fewer slots. Sweep batches
leave candidates at sandbox; scrutiny and falsification are separately requested stages.

### Legacy shell driver

`scripts/driver.sh` remains a Claude-only runner. It sweeps, verifies, runs scrutiny,
regenerates outputs, and commits/pushes. It does not run falsification. It still uses the
`python` command, so activate the virtual environment first. Do not use it concurrently
with an interactive batch.

This compatibility change does not adapt or harden that runner: `COST_CEILING` is only
printed, worker failures are not fully aggregated, the sandbox-candidate check treats a
summary footer as a nonempty result, and repository-wide staging can include unrelated
work. These need script changes before relying on unattended operation with either agent.

---

## The four phases

| Skill | Phase | When it runs | Writes |
|---|---|---|---|
| `niche-batch` | Phase 1 orchestration | Explicit batch request | Assignments, coordinated outputs |
| `niche-sweep` | 1 — evidence gathering | Every batch, once per cell | `ideas/*.md`, ledger |
| `niche-scrutiny` | 2 — triage + sourced critique | Requested review of `sandbox` | Idea frontmatter, scrutiny logs |
| `niche-falsify` | 3 — cheap disconfirmation | Requested tests of promoted ideas | Falsification logs, `worklist.md` |
| `niche-dossier` | 4 — deep research | Only when you name an idea | `dossiers/<slug>/` |

Four phase skills plus the batch orchestrator keep discovery, evaluation, testing, and
deep research separate. Each invocation loads only the relevant instructions and references.

Status lifecycle: `sandbox → demoted | promoted → falsified | validated`.
Dossiers are directories for selected validated ideas; `dossier` is not an indexed status.
Duplicates use `status: duplicate`. Preserve the records of failed and duplicate ideas.

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
.claude/skills/        five canonical skills, versioned with the repo
.agents/skills/        relative links exposing those same skills to Codex
AGENTS.md              Codex project guidance
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
| `ledger_append.py` | Appends a sweep record without rewriting cells |
| `rollup_cells.py` | Recomputes cell counters after workers finish |
| `list_ideas.py` | Lists by status, so agents don't glob the corpus into context |
| `build_index.py` | Regenerates `INDEX.md` |
| `cost_report.py` | Yield-per-dollar by cell and taxonomy |
| `driver.sh` | Legacy Claude-only sweep + scrutiny runner; see limitations above |

Anything a model could get wrong by being inconsistent lives here rather than in a prompt:
dedup thresholds, score arithmetic, and coverage bookkeeping. Source verification still
has limits: it checks reachability and tags, not claim support or independence. Scrutiny
must inspect the qualifying sources; a script pass alone does not establish those facts.

---

## Concurrency contract

Use one coordinator per shared checkout. Select assignments before spawning workers;
`next_cells.py` does not reserve cells against another coordinator.

1. Workers create only their own new idea files and never overwrite existing slugs.
2. Workers return near-matches and proposed evidence; the coordinator updates existing
   ideas after workers finish.
3. Workers append sweep records with `ledger_append.py`. The coordinator resolves
   duplicates, verifies affected sources, then runs rollup and index generation serially.
4. Use up to six workers, bounded by the host's available capacity. Prefer a shared
   checkout; isolated worktrees require explicit collection and reconciliation of outputs.
5. Preserve pre-existing edits. Commit/push within task authorization and stage only the
   task's changes, including selective staging for shared files.

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
known drift mode. Decide whether to retune after reviewing the evidence. For an authorized
threshold change, update `THRESHOLD` in `scripts/score.py` and synchronize the rubric text
in `.claude/skills/niche-scrutiny/references/rubric.md`, with a dated explanation.

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
