---
name: niche-batch
description: Run a full sweep batch in one session — pull N cells from the frontier, fan them out to parallel niche-sweeper subagents, then run the deterministic passes (dedup, source verification, rollup, index) and report; commit or push when authorized. Use whenever Nathan wants to sweep without naming cells, says to run a batch, a round, or "go hunt," asks to keep sweeping until a budget or time limit is hit, or invokes /sweep. This is the normal way to run Phase 1 — niche-sweep on its own is for sweeping one named cell by hand. Do NOT use for scrutiny, falsification, or dossier work.
---

# Niche Batch — parallel sweep orchestration

You coordinate assignments, workers, deterministic passes, and reporting. Delegate
sweeps when the host supports workers; use the sequential fallback below otherwise.

## Step 1 — Decide the size of the batch

If Nathan gave a number, use it. If not, default to **24 cells**.

Use waves of **up to 6 concurrent workers**, reduced to the host's available capacity.
Keep one cell per worker. On a host with three worker slots, 24 cells takes eight waves.
If delegation is unavailable, report that limitation and process one assigned cell at a
time using the same skill and ownership rules.

If he asked to run until a limit ("keep going for an hour", "until I run low"), keep
launching waves and report progress after each, stopping when the limit is reached or when
three consecutive completed waves yield zero stubs — report this as a signal to inspect
the frontier policy, not proof that the sector has no useful work. Failed or partial waves
do not count as zero-yield waves. Clarify vague limits such as "until I run low" before
starting. Use host measurements for usage limits; if a hard limit cannot be enforced,
resolve an alternative with Nathan before launching budgeted work.

## Step 2 — Pull the assignments

```bash
python3 scripts/next_cells.py --count <N>
```

Before selection, confirm no other coordinator is running in this checkout. The selector
does not reserve cells. Run `python3 scripts/rollup_cells.py` if previous sweeps have
finished but their ledger records have not been rolled up.

Take the whole list at once, before launching anything. Never let workers select cells
themselves. If Nathan supplied explicit cells, preserve those assignments. For a continued
run, finish and roll up each bounded batch before selecting the next; exclude cells already
assigned in this run.

## Step 3 — Fan out

In Claude Code, use the named `niche-sweeper` agent. In Codex, use available native
subagent tools and explicitly pass the repository root, canonical `niche-sweep/SKILL.md`
path, and the worker rules below. Do not assume Claude's `Task`, tool allowlist, or
`model: sonnet` configuration is available in Codex. Use the host's configured model unless
Nathan specified another. Launch independent workers concurrently within the available slots.

Each subagent prompt should be minimal:

> Sweep frontier cell `<cell_id>` using `.claude/skills/niche-sweep/SKILL.md`.
> Agent id: `<run-id>-sweep-<n>`. Work from the repository root. Create only your own new
> idea files; never overwrite an existing slug. Report near-matches and proposed evidence
> to the coordinator. Append your ledger record with `ledger_append.py`. Do not run
> rollup, index generation, or git. Return slugs, jobs, matches, source types, and failures.

Wait for every worker in the wave, recording completion or failure by cell. Do not
record failed cells as completed empty sweeps. Before retrying, inspect any partial files
and ledger entries to avoid duplicate records. Run the aggregate passes after all waves
in this bounded batch finish.

Prefer workers sharing this checkout under one coordinator. Workers must not mutate
existing ideas, even to append evidence. Similar discoveries can propose the same slug;
never overwrite a file that already exists. If the host requires isolated worktrees,
collect and reconcile their outputs before generating shared state or reporting completion.

## Step 4 — Deterministic passes, once, after all waves

In this order, single-threaded:

```bash
python3 scripts/dedup.py --sweep
python3 scripts/verify_sources.py --unverified-only
# Resolve reported pairs and verify every changed canonical idea with --slug <slug>.
python3 scripts/rollup_cells.py
python3 scripts/build_index.py
```

If `verify_sources.py` aborts with an environment error, stop and surface it. Do not retry
with `--offline` to get past it — that records unverified sources as verified.

Resolve any near-duplicate pairs `dedup.py --sweep` reports: read both files, and either
merge the evidence into the older one and set the newer to `status: duplicate`, or leave
both and say why they are actually distinct. Incorporate worker-reported near-match
evidence here. `dedup.py --sweep` reports pairs; it does not merge files. Re-run
`verify_sources.py --slug <slug>` for each canonical idea whose evidence changed, even if
it already has an evidence tier. Complete these resolutions before rollup and index generation.

## Step 5 — Save the batch

When committing or pushing is included in the task or established authorization, review
the diff and stage only this batch's changes. Preserve unrelated pre-existing edits,
including edits in shared files; use selective staging when needed. Commit with a summary
of completed cells and stubs, and push only when authorized. Otherwise leave the outputs
ready for review and report their paths. Never stage the entire dirty repository blindly.

## Step 6 — Report

Short. Cells swept and how many yielded nothing. New idea slugs with their `job:` lines.
Duplicates resolved. Which source types are producing evidence and which are not. Anything
the frontier policy should know.

**Do not dump subagent transcripts into the conversation.** The whole point of the fan-out
is that the noisy middle stays in their contexts.

## What this skill must not do

- **Do not score, critique, or promote anything.** Everything lands at `status: sandbox`.
  Scrutiny is a separate phase with a separate skill, run deliberately.
- **Do not adjust `next_cells.py` policy** based on what a batch yielded. A few dozen cells
  is noise, and a model asked to optimize a selection policy will happily do it on three
  data points. Report the observation; leave the decision to Nathan.
