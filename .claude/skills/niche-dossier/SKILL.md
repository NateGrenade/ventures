---
name: niche-dossier
description: Build a full research dossier for one validated idea in Nathan's niche-hunt repo — market analysis with stated methodology, technical architecture and integration surfaces, an explicit open-questions file, and a project proposal — inside a hard declared token budget. Use whenever Nathan flags a specific idea for deep research, says to expand, build out, or go deep on one, or asks for a proposal or full write-up on a niche. This is Phase 4 of the niche-hunt pipeline and it is human-gated — use it only when Nathan names an idea, never automatically. Do NOT use for sweeping, critiquing, or validating; those are niche-sweep, niche-scrutiny, and niche-falsify.
---

# Niche Dossier (Phase 4)

Exhaustive research on one idea Nathan has personally selected.

## Gate — do not skip

1. **Human-selected.** Nathan names the idea. No agent enters this phase on its own.
2. **`status: validated`.** If the idea is only `promoted`, stop and run niche-falsify first. If Nathan explicitly overrides, note the override in the dossier README.
3. **Budget declared before starting.** Ask for a token or dollar ceiling if none was given. This is the expensive phase; an unbounded deep-research run is how a month's budget disappears in an afternoon.

Log the budget and the selection rationale in `dossiers/<slug>/README.md` as the first thing you write.

## Structure

```
dossiers/<slug>/
├── README.md                  # budget, selection rationale, dossier status
├── market-analysis/
│   ├── competitors.md
│   ├── sizing.md
│   └── buyer-profile.md
├── technical-architecture/
│   ├── integration-surfaces.md
│   └── proposed-stack.md
├── open-questions.md
└── project-proposal.md
```

## The derivation rule

**Every number carries its derivation inline.** Not in a footnote — in the sentence.

Bad: *The addressable market is approximately $340M.*

Good: *~18,000 US firms in NAICS 541191 (Census 2022 County Business Patterns), of which perhaps 40% are large enough to employ a dedicated clerk (inferred from job-posting concentration, weak), at a plausible $4-6k/yr — giving $29-43M, with the 40% figure being the load-bearing and least supported assumption.*

A market size without a method is a hallucination with a dollar sign attached. When you cannot derive a number, write that you cannot and put it in `open-questions.md`.

## What each file covers

**`competitors.md`** — Direct, adjacent, and substitute. Pricing where public. For each: what job they actually do, and where the seam is. Include dead competitors and, if findable, why they died. Link everything.

**`sizing.md`** — Bottom-up only. Firm counts from Census/industry registries, multiplied by adoption assumptions you state and rate for confidence. Never cite a top-down analyst TAM figure as evidence; if you mention one, mark it Tier 3 and explain why bottom-up disagrees.

**`buyer-profile.md`** — The role. What they already buy. Where they congregate. What their procurement looks like. What a realistic sales cycle is. This file decides whether the business is reachable, which decides whether it matters that the idea is good.

**`integration-surfaces.md`** — The specific systems the work touches. Whether each has an API, an export, a file format, or nothing. Named endpoints where you can find documentation. Absence of an interface is a finding, stated plainly — it is either the moat or the wall, and which one it is depends on facts worth establishing here.

**`proposed-stack.md`** — Keep short and unopinionated. The stack is the least uncertain part of any of this and deserves the least research.

**`open-questions.md`** — Often the most useful file in the dossier. Everything research could not resolve, each tagged with why: no public data, requires practitioner contact, requires access to the incumbent system, genuinely unknowable without building. Rank by how much the answer would change the decision.

**`project-proposal.md`** — Phased roadmap with a first milestone that is a test rather than a build. Explicitly name what would make you abandon this at each phase.

## Confidence marking

Every substantive claim carries one:
- `[VERIFIED]` — multiple independent sources, links given
- `[SINGLE-SOURCE]` — one source, named
- `[INFERRED]` — reasoning from evidence, reasoning shown
- `[SPECULATION]` — informed guess, flagged as such

Unmarked prose is read as `[VERIFIED]` by a future reader, including future Nathan. Mark everything.

## Budget discipline

Before research, establish whether the host exposes usage and can enforce the declared
ceiling. Do not promise hard token or dollar enforcement from a prompt alone. If the
requested hard limit cannot be enforced, resolve an alternative with Nathan first.
Distinguish estimated API-equivalent cost from actual billing or subscription usage.
Use limits already agreed in the conversation without asking again.

Check measured consumption against the declared ceiling at each file boundary and before
starting another substantial section. File-boundary checks alone do not enforce a hard cap. On breach: stop, write current state into `README.md`, list what remains unresearched in `open-questions.md`, and hand back. Do not silently overrun, and do not thin out later sections to fit — a half-finished dossier with an honest boundary is more useful than a complete one that got vague at the end.

## Hand-off

Finish with a `## Bottom Line` section in `README.md`: the two or three things that would most change the decision, and what it would cost to learn each. That is what Nathan reads first.

Then:
```bash
python3 scripts/build_index.py
```
