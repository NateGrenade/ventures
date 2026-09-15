---
name: niche-sweep
description: Sweep a single assigned frontier cell (a NAICS industry code, O*NET occupation, or other taxonomy unit) in Nathan's niche-hunt repo for evidence of manual, tedious, or unautomated operational work, and emit deduplicated candidate idea files with verified sources. Use whenever a cell ID is assigned by the driver script, whenever Nathan says to sweep, scan, or hunt a cell or sector, and whenever he asks for new candidates to be gathered into the ideas/ directory. This is Phase 1 of the niche-hunt pipeline — use it even if Nathan just names a sector and says "go look at this one." Do NOT use for evaluating, scoring, or researching existing ideas; those are niche-scrutiny, niche-falsify, and niche-dossier.
---

# Niche Sweep (Phase 1)

Gather evidence of operational pain inside one assigned frontier cell. Emit candidate idea files.

## Preconditions — check these first, fail fast

1. `frontier/cells.jsonl` exists. If not, stop and tell Nathan to run `python3 scripts/bootstrap.py`.
2. You have been assigned **exactly one** `cell_id`. If none was given, run `python3 scripts/next_cells.py --count 1` and take the result.
3. Load your cell's context:
   ```bash
   python3 scripts/show_cell.py <cell_id>
   ```
   Never read `frontier/cells.jsonl` directly — it is ~1,900 lines and would dwarf everything else in your context.

   O*NET cells carry a `hint` field containing the occupation's official task description. **Read it and mine it.** It is a government-written list of the manual work this occupation performs, which is exactly what you are hunting; treat its verbs as your first round of search queries.

One cell per agent. Do not expand outside the assigned cell, even if a neighbouring sector looks more promising — note it in the ledger instead.

This skill sweeps a single cell. To sweep many cells, the `niche-batch` skill fans out one
`niche-sweeper` subagent per cell and each of those follows this skill. If you were handed
several cells directly, use `niche-batch` instead of working through them in series.

## The central prohibition

**Never search for ideas. Search for artifacts that incidentally reveal manual work.**

Queries like "underserved industries," "markets ripe for disruption," "industries that need automation," or "SaaS opportunities in X" return content written by vendors selling into those markets and by SEO farms. They will produce the same dozen sectors forever, dressed as research.

If you catch yourself writing a query containing *opportunity, underserved, ripe, disruption, untapped, ready for AI*, stop and rewrite it as a search for a document that a practitioner or an employer produced for their own purposes.

## What counts as in-scope work

The target is **information work**: data moving between systems, formats, or organizations
by hand. Rekeying, reconciling, cross-referencing, chasing paperwork, bridging two systems
that do not talk to each other.

The target is **not** physical labor, however tedious or manual. Lifting, driving, inspecting
on site, operating equipment, and caring for people are all real work that no amount of
software absorbs. A sweep that returns well-sourced evidence of hard physical work has found
nothing this pipeline can use.

This matters because the taxonomy is full of physical occupations and they will produce
abundant Tier 1 evidence. `onet-47-5071.00` (Roustabouts, Oil and Gas) is a real cell in the
frontier. Sweeping it for "manual work" would succeed and be worthless.

**But do not discard a physical cell outright.** The paperwork *around* physical work
routinely qualifies even when the work itself does not: a roustabout crew's daily job
tickets, equipment logs, and safety compliance filings are information work, and they are
often exactly the kind of thing still done on carbon paper. Sweep the administrative shadow
of the occupation, not the occupation.

If a cell offers neither — the work is physical and its paperwork is already digital or
trivial — record **zero stubs** and say so in the ledger note. That is a useful result.

Every `job:` line must survive this test: does it describe information moving, or a person
moving? If the latter, it does not get a file.

## Evidence hunt protocol

Work the source types below in order. Stop when you have exhausted reasonable queries or hit the turn budget — partial sweeps are fine and the ledger records them.

1. **Job postings** — the highest-signal source. An employer paying salary for a task has already priced the pain. Search the cell's occupations for postings describing rekeying, reconciliation, manual data entry, chasing paperwork, "maintaining spreadsheets," "coordinating between systems."
2. **Practitioner venues** — trade subreddits, industry forums, professional association boards, niche Discord/Slack communities. You want operators complaining to each other, not to buyers.
3. **Regulatory filings and public comment dockets** — compliance burden described in detail by the people bearing it.
4. **Procurement records and RFPs** — requirements stated in operational language, with budgets attached.
5. **Trade press** — software adoption stories, failed rollouts, persistent workflow complaints.

For source typing and worked query examples, read `references/evidence-sources.md`. Read it on your first sweep of a session; skip it afterwards.

## Emitting candidates

A sweep produces 0–N stubs. **Zero is a legitimate outcome** — record it and move on. A cell that yields nothing is information the frontier policy uses.

For each candidate:

1. **Dedup before writing.**
   ```bash
   python3 scripts/dedup.py --check "<proposed title>" --summary "<one-line problem statement>"
   ```
   On a reported near match, do not create a new file. What you do next depends on how you were invoked:

   - **Running inside a batch** (spawned by `niche-batch`, or told you are one of several sweepers): **do not touch the existing file.** Report the match in your summary — the slug you matched, and the evidence you would have added — and let the orchestrator merge it single-threaded. Concurrent sweepers have no locking, so two agents appending to the same canonical file will lose one of the updates.
   - **Running standalone** on a single named cell, with no other sweepers active: append your evidence to the named canonical file under an `## Additional Evidence` heading and stop there.

   If you are unsure which applies, assume batch and report rather than write.

2. **Write `ideas/<slug>.md`** using the template in `references/evidence-sources.md`. Required frontmatter:

   ```yaml
   ---
   slug: <kebab-case>
   status: sandbox
   cell_id: <assigned cell>
   created: <YYYY-MM-DD>
   owner_agent: <your agent id, or "manual">
   job: <one line — see "One job per file" below. REQUIRED>
   split_from: null         # set only when splitting one finding into several files
   evidence_tier: null      # computed, leave null
   scores: {}               # populated by score.py, never by hand
   human_verdict: null
   cost_usd: null
   ---
   ```

   Body sections, in order: **Problem statement** (what work is done by hand, by whom, how often), **Evidence** (bulleted, every bullet carrying a URL, a source type, and the source's date), **Automation hypothesis** (one paragraph, explicitly speculative).

   **Date every source.** A 2022 procurement document is much weaker evidence of a *current* manual process than a 2025 one, and Phase 2 cannot weigh that if you do not record it.

## One job per file

Write the `job:` line first. It is a single sentence in this shape:

> *\<who\> manually \<verb\> \<thing\> between \<system A\> and \<system B\>, because \<why no tooling bridges them\>.*

If you cannot write **one** such sentence covering your whole finding, you have found more than one thing. Split it.

**The test is buyer and job, not topic.** One file if a single product sold to one buyer solves the whole thing. Two files if solving one half leaves the other untouched, or if different people sign the check. Two problems in the same sector, sharing vocabulary and even sharing sources, are still two problems — a billing clerk balancing daily revenue and a contract manager handing accounts to a collection agency are different buyers with different integration surfaces, however adjacent they sound.

When you split one finding into several files:

- Give every resulting file the same `split_from: <original-slug>` value. This exempts the set from being auto-merged back together by `dedup.py`.
- Copy each source into whichever files it actually supports. A source can support more than one.
- Run `dedup.py --check` for each file separately.

The `job:` line is also what `dedup.py` compares against — not your prose. Write it as plainly as possible, and name the systems rather than the industry. Sector vocabulary is shared by genuinely distinct ideas and absent from genuinely identical ones, so an idea framed as "municipal utility billing reconciliation" hides both the duplicate in the corpus and the distinct idea sitting next to it.

3. **Never edit `INDEX.md`.** It is generated. Never edit another agent's idea file except to append evidence under `## Additional Evidence`.

## Source discipline

Every factual claim carries a URL and a source-type tag. Claims you cannot source do not go in the file at all — not as "likely" or "reportedly."

After writing, run:
```bash
python3 scripts/verify_sources.py --slug <slug>
```
This fetches every URL, confirms it resolves, and computes `evidence_tier`. Unreachable citations are stripped and their claims downgraded. Do not hand-edit `evidence_tier`.

## Closing the sweep

Append one ledger record:
```bash
python3 scripts/ledger_append.py --cell <cell_id> --agent <agent_id> \
  --stubs <n> --merged <n> --cost <usd> \
  --sources <comma-separated source types that actually yielded> \
  --note "<optional observation>"
```

`--sources` records which source types produced usable evidence in this cell — e.g.
`job-posting,procurement`. Record only what actually yielded; omit types you tried and got
nothing from. This is the observation that tells the pipeline, after enough cells, which
kinds of digging are worth the tokens.

Use the note field for anything else the frontier policy should know: a taxonomy cell that was too broad, an adjacent cell worth queueing, a tool that failed.

`ledger_append.py` is append-only and safe to run while other sweepers are working. Do not run `rollup_cells.py`, `build_index.py`, or git — the orchestrator does those once the batch is done.

Then stop. Do not score, critique, or research your own candidates — that is Phase 2's job, and doing it here defeats the separation.

## Collection hygiene

Respect `robots.txt` and rate limits. Stay off anything behind authentication. Prefer official APIs where they exist. A pipeline that gets the IP blocked is not autonomous.
