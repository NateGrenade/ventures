---
name: niche-sweep
description: Sweep a single assigned frontier cell (a NAICS industry code, O*NET occupation, or other taxonomy unit) in Nathan's niche-hunt repo for evidence of manual, tedious, or unautomated operational work, and emit deduplicated candidate idea files with verified sources. Use whenever a cell ID is assigned by the driver script, whenever Nathan says to sweep, scan, or hunt a cell or sector, and whenever he asks for new candidates to be gathered into the ideas/ directory. This is Phase 1 of the niche-hunt pipeline — use it even if Nathan just names a sector and says "go look at this one." Do NOT use for evaluating, scoring, or researching existing ideas; those are niche-scrutiny, niche-falsify, and niche-dossier.
---

# Niche Sweep (Phase 1)

Gather evidence of operational pain inside one assigned frontier cell. Emit candidate idea files.

## Preconditions — check these first, fail fast

1. `frontier/cells.jsonl` exists. If not, stop and tell Nathan to run `python scripts/bootstrap.py`.
2. You have been assigned **exactly one** `cell_id`. If none was given, run `python scripts/next_cells.py --count 1` and take the result.
3. Load your cell's context:
   ```bash
   python scripts/show_cell.py <cell_id>
   ```
   Never read `frontier/cells.jsonl` directly — it is ~1,900 lines and would dwarf everything else in your context.

   O*NET cells carry a `hint` field containing the occupation's official task description. **Read it and mine it.** It is a government-written list of the manual work this occupation performs, which is exactly what you are hunting; treat its verbs as your first round of search queries.

Do not sweep more than one cell per invocation. Do not expand outside the assigned cell, even if a neighbouring sector looks more promising — note it in the ledger instead.

## The central prohibition

**Never search for ideas. Search for artifacts that incidentally reveal manual work.**

Queries like "underserved industries," "markets ripe for disruption," "industries that need automation," or "SaaS opportunities in X" return content written by vendors selling into those markets and by SEO farms. They will produce the same dozen sectors forever, dressed as research.

If you catch yourself writing a query containing *opportunity, underserved, ripe, disruption, untapped, ready for AI*, stop and rewrite it as a search for a document that a practitioner or an employer produced for their own purposes.

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
   python scripts/dedup.py --check "<proposed title>" --summary "<one-line problem statement>"
   ```
   On a reported near match, do not create a new file. Append your evidence to the named canonical file under a `## Additional Evidence` heading and stop there.

2. **Write `ideas/<slug>.md`** using the template in `references/evidence-sources.md`. Required frontmatter:

   ```yaml
   ---
   slug: <kebab-case>
   status: sandbox
   cell_id: <assigned cell>
   created: <YYYY-MM-DD>
   owner_agent: <your agent id, or "manual">
   evidence_tier: null      # computed, leave null
   scores: {}               # populated by score.py, never by hand
   human_verdict: null
   cost_usd: null
   ---
   ```

   Body sections, in order: **Problem statement** (what work is done by hand, by whom, how often), **Evidence** (bulleted, every bullet carrying a URL and a source type), **Automation hypothesis** (one paragraph, explicitly speculative).

3. **Never edit `INDEX.md`.** It is generated. Never edit another agent's idea file except to append evidence under `## Additional Evidence`.

## Source discipline

Every factual claim carries a URL and a source-type tag. Claims you cannot source do not go in the file at all — not as "likely" or "reportedly."

After writing, run:
```bash
python scripts/verify_sources.py --slug <slug>
```
This fetches every URL, confirms it resolves, and computes `evidence_tier`. Unreachable citations are stripped and their claims downgraded. Do not hand-edit `evidence_tier`.

## Closing the sweep

Append one ledger record:
```bash
python scripts/ledger_append.py --cell <cell_id> --agent <agent_id> \
  --stubs <n> --merged <n> --cost <usd> --note "<optional observation>"
```

Use the note field for anything the frontier policy should know: a taxonomy cell that was too broad, a source type that worked unusually well, an adjacent cell worth queueing.

Then stop. Do not score, critique, or research your own candidates — that is Phase 2's job, and doing it here defeats the separation.

## Collection hygiene

Respect `robots.txt` and rate limits. Stay off anything behind authentication. Prefer official APIs where they exist. A pipeline that gets the IP blocked is not autonomous.
