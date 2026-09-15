---
name: niche-batch
description: Run a full sweep batch in one session — pull N cells from the frontier, fan them out to parallel niche-sweeper subagents, then run the deterministic passes (dedup, source verification, rollup, index) and commit. Use whenever Nathan wants to sweep without naming cells, says to run a batch, a round, or "go hunt," asks to keep sweeping until a budget or time limit is hit, or invokes /sweep. This is the normal way to run Phase 1 — niche-sweep on its own is for sweeping one named cell by hand. Do NOT use for scrutiny, falsification, or dossier work.
---

# Niche Batch — parallel sweep orchestration

You are the orchestrator. You do not sweep anything yourself. You assign cells, fan out
subagents, run the deterministic passes, and report.

## Step 1 — Decide the size of the batch

If Nathan gave a number, use it. If not, default to **24 cells**.

Cells are swept in **waves of 4 concurrent subagents**. 24 cells is six waves.

Four, not more. WebSearch has a per-session budget (roughly 200 queries) shared across every
subagent you spawn, so wider waves exhaust it and the later cells come back empty having
spent tokens for nothing. Wide waves also produce rate-limit failures and interleaved tool
output without finishing meaningfully faster. If sweepers report budget exhaustion, narrow
the wave further rather than launching more.

If he asked to run until a limit ("keep going for an hour", "until I run low"), keep
launching waves and report progress after each, stopping when the limit is reached or when
three consecutive waves yield zero stubs — the latter means the frontier policy is feeding
you dead territory and is worth a human look.

## Step 2 — Pull the assignments

```bash
python3 scripts/next_cells.py --count <N> --claim <date>-<orchestrator>-batch
```

**Always pass `--claim`.** `cells.jsonl` is not rolled up until the batch ends, so without a
claim every orchestrator that asks gets handed the same never-swept cells — and if a second
runner (another Claude Code session, Codex) is working the same repo, you will both sweep
the same cells and waste the wave. Claims expire after 6 hours; use `--ignore-claims` only
to recover cells abandoned by a batch that died.

Take the whole list at once, before launching anything. Never let subagents call
`next_cells.py` themselves — they would each get overlapping selections.

## Step 3 — Fan out

For each wave, spawn `niche-sweeper` subagents **in parallel** — all Task calls for a wave
in a single message, not one after another. One cell per subagent. Nothing is gained by
giving a subagent two cells; the isolation is the point.

Each subagent prompt should be minimal:

> Sweep frontier cell `<cell_id>` using the niche-sweep skill. Agent id: `sweep-<n>`.
> You are running inside a batch: on a dedup near-match, report it and do not edit the
> existing file.

That last line is not optional. Sweepers running concurrently have no locking, so two of
them independently matching the same canonical file would both write to it and one update
would be lost. In a batch, **you** resolve near-matches in Step 4, single-threaded.

Wait for the whole wave to return before launching the next. Do not run the deterministic
passes between waves.

**Do not use `isolation: worktree`.** Each sweeper writes only files it creates, so there is
nothing to collide over, and worktrees would scatter the idea files across branches that
then need merging.

## Step 4 — Deterministic passes, once, after all waves

In this order, single-threaded:

```bash
python3 scripts/dedup.py --sweep
python3 scripts/verify_sources.py --unverified-only
python3 scripts/rollup_cells.py
python3 scripts/build_index.py
python3 scripts/release_cells.py --agent <your-id> <every cell you were assigned>
```

Release every cell you claimed, including ones that yielded nothing. Claims otherwise block
reselection for their full 6-hour TTL, so a batch that finishes in forty minutes leaves the
frontier artificially narrow for another five hours — and the other coordinator feels it.

If `verify_sources.py` aborts with an environment error, stop and surface it. Do not retry
with `--offline` to get past it — that records unverified sources as verified.

Resolve any near-duplicate pairs `dedup.py --sweep` reports: read both files, and either
merge the evidence into the older one and set the newer to `status: duplicate`, or leave
both and say why they are actually distinct.

## Step 5 — Commit this batch's work only

Another coordinator may be running against this repo at the same time, with uncommitted
edits in shared files. **Never `git add -A`.** Stage only the paths this batch produced:

**Never stage `ideas/` or `merged/` wholesale either.** Another coordinator writes into
those same directories, so a directory-level add sweeps up its in-flight files — in a recent
batch, 25 of 42 new idea files belonged to the other runner. Stage your own by name; you
have every slug from your subagents' reports.

```bash
git add frontier/ledger.jsonl frontier/cells.jsonl INDEX.md
git add ideas/<slug-1>.md ideas/<slug-2>.md          # only slugs your sweepers reported
git add merged/<slug>.md                             # only if you created it
git status            # read it before committing
git commit -m "sweep batch: <N> cells, <M> stubs"
```

Check `git status` for anything unexpected still unstaged — scripts, skill files, config,
and idea files you did not create. Those belong to someone else's in-flight work; leave them
alone and mention them in your report.

**Do not push.** Say the commit is ready and let Nathan push, or push only if he has asked
you to in this session. An unprompted push in a repo with a live second coordinator
publishes work nobody has reviewed.

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
