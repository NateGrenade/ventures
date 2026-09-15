# Evidence Sources Reference

## Source tiers

`verify_sources.py` assigns tiers from the `type:` tag on each evidence bullet. Tag honestly — inflating a tier corrupts the Phase 2 gate.

### Tier 1 — produced by someone with skin in the game
| Type tag | What it is | Why it's strong |
|---|---|---|
| `job-posting` | Listing describing the manual task | Employer has priced the pain in salary |
| `practitioner` | Forum/subreddit/association post by an operator | No incentive to exaggerate to a buyer |
| `regulatory` | Filing, comment docket, inspection report | Burden described under obligation |
| `procurement` | RFP, bid record, contract award | Requirements plus a budget |
| `institutional` | An organization's own published operating procedure — a university policy page, a hospital's documented intake workflow, an agency's internal handbook | The org describing its own process, for its own staff, with no one being sold to |

### Tier 2 — secondhand but disinterested
| Type tag | What it is |
|---|---|
| `trade-press` | Industry publication coverage |
| `study` | Academic paper, government report, census data |
| `conference` | Agenda, session description, panel topic |

`institutional` is for organizations documenting how they actually work. It is not for an
organization's marketing, recruiting, or public-relations pages — those are `vendor`. The
test is who the page was written for: if the audience is the org's own staff or the public
it serves, it is institutional; if the audience is a buyer, it is vendor.

### Tier 3 — someone is selling something
| Type tag | What it is |
|---|---|
| `vendor` | Marketing page, case study, whitepaper |
| `analyst` | Gartner-style report, market-sizing PR |
| `listicle` | "Top 10 industries ready for AI" and anything that smells AI-generated |

**An idea supported only by Tier 3 cannot be promoted in Phase 2.** This rule does more filtering than any rubric.

## Query patterns

### Job postings
Search the cell's O*NET occupation titles plus manual-work verbs:
- `"<occupation>" "data entry" -senior`
- `"<industry>" clerk "reconcile" spreadsheet`
- `"<industry>" coordinator "manual process"`
- `"<industry>" "rekey" OR "re-enter" invoices`

Three or more active postings for a role whose description is a manual workflow is strong Tier 1 evidence. Note the salary band — it bounds what the problem is worth.

### Practitioner venues
- `site:reddit.com "<industry>" "hate" OR "nightmare" workflow`
- `site:reddit.com r/<trade> spreadsheet "every month"`
- `"<industry> forum" "is there a better way"`
- `"<trade association>" forum software frustration`

Look for descriptions of **workarounds**. A detailed workaround is a problem statement someone else wrote for you.

### Regulatory
- `"<industry>" "paperwork reduction" comment`
- `"<agency>" docket "<industry>" burden hours`
- Federal and state comment dockets where the regulated party estimates its own compliance hours.

### Procurement
- `"<county|state>" RFP "<industry function>"`
- Municipal and county portals are underexplored and describe real workflows in operational detail.

### Trade press
- `"<industry>" trade publication "still using"`
- `"<industry>" "legacy system" migration failed`

## Idea file template

```markdown
---
slug: example-slug
status: sandbox
job: title clerks manually cross-reference county recorder indexes against
  the internal title plant, because the plant software has no import for
  recorder feeds
split_from: null
cell_id: naics-541191
created: 2026-09-14
owner_agent: sweep-03
evidence_tier: null
scores: {}
human_verdict: null
cost_usd: null
---

# Title Plant Reconciliation

## Problem statement

Who does what by hand, how often, and at what apparent cost. Two to four
sentences. Operational language only — no market framing, no pitch.

## Evidence

- [type: job-posting] (2026-08) Three current listings at <firm> for a role
  whose description is manual cross-referencing of X against Y.
  https://example.com/posting
- [type: practitioner] (2025-11) Operator describes a monthly two-day
  reconciliation done in Excel. https://example.com/thread
- [type: trade-press] (2024-03) Coverage noting the sector's dominant system
  has no export function. https://example.com/article

## Automation hypothesis

SPECULATIVE. One paragraph on what could plausibly absorb this work, and
what would have to be true for it to be tractable. Flag the integration
surface if known.
```

## Anti-patterns

- **Rewriting a vendor's pitch as a problem statement.** If the framing came from someone selling a solution, the framing is their marketing.
- **Sweeping adjacent cells because they look better.** Note them; the driver will queue them. Wandering breaks coverage accounting.
- **Writing the automation hypothesis first and hunting evidence to fit it.** Evidence first, always.
- **Padding a thin sweep.** Zero stubs recorded honestly is worth more than four speculative ones.
- **Bundling two problems because they share a sector.** If the `job:` line needs an "and" joining two different manual processes, it is two files.
