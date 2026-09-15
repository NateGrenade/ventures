# Scrutiny Rubric — Anchored Scales

Emit integer values for each dimension into the `scores:` frontmatter map. `score.py` computes the composite. Anchors are binding: pick the anchor that matches the evidence you actually have, not the one that matches your impression.

## `pain_evidence` (weight 3)

| Value | Anchor |
|---|---|
| 0 | Only Tier 3 sources, or the pain is inferred rather than described |
| 1 | One Tier 1/2 source describing the manual work |
| 2 | Two or more independent sources; at least one Tier 1 |
| 3 | Multiple Tier 1 sources **plus** a dollar figure attached — salary band from a job posting, burden hours from a filing, contract value from an RFP |

## `buyer_clarity` (weight 3)

| Value | Anchor |
|---|---|
| 0 | No identifiable budget holder; pain distributed across fractions of many roles |
| 1 | A role exists but budget authority is unclear or sits several levels up |
| 2 | Named role that plausibly holds budget for tools in this category |
| 3 | Named role, and evidence they already buy something adjacent — an existing line item you would displace or sit beside |

## `incumbent_gap` (weight 2)

| Value | Anchor |
|---|---|
| 0 | Three or more direct competitors, mature category |
| 1 | One or two direct competitors serving this job adequately |
| 2 | Adjacent players only; nobody targets this job specifically |
| 3 | No direct or adjacent player found after genuine search; the substitute is a spreadsheet, a temp, or an offshore team |

*A 3 here demands you actually searched. Record the queries you ran in the scrutiny log. "Found no competitors" without recorded queries scores 1.*

## `reachability` (weight 2)

How you would get in front of the buyer.

| Value | Anchor |
|---|---|
| 0 | No channel; buyers are numerous, tiny, and unaggregated |
| 1 | Channel exists but is expensive — field sales, long procurement |
| 2 | Identifiable aggregation point: trade association, conference, dominant forum, industry newsletter |
| 3 | Buyers are concentrated, or an existing distributor could carry it |

## `tractability` (weight 3, HARD FLOOR of 2)

| Value | Anchor |
|---|---|
| 0 | Blocked by a hard technical or data-access problem with no path |
| 1 | Requires integration with a closed system; feasibility unknown |
| 2 | Integration surface exists (API, export, standard file format) or the work is self-contained |
| 3 | Clean surface **and** the capability that makes it newly feasible is identifiable |

**Scoring 0 or 1 here is a demote regardless of composite score.** This pipeline exists to
find work that software can absorb. An idea with vivid pain, an obvious buyer, and no way
for code to touch the workflow is not a near-miss — it is a different kind of business, and
letting the other dimensions carry it is how this pipeline fills up with consulting practices.

Note that an integration surface is a *fact to establish*, not a guess. If you could not
determine whether the incumbent system exports data, score 1 and say so; do not score 2 on
the assumption that something must be possible.

## `persistence_quality` (weight 3)

Derived from the mandatory persistence tag.

| Value | Tag |
|---|---|
| 0 | `unattractive-economics`, `fragmented-buyer`, `incumbent-distribution` |
| 1 | `regulatory-moat` — sometimes an opportunity, usually a wall |
| 1 | `unnoticed` — scored low deliberately; near-always a research failure |
| 3 | `genuinely-hard` — **technically** unsolved, not human-presence-required |
| 3 | `recently-unlocked` |

`genuinely-hard` is the tag most easily abused. It means the computational or data problem
has no good solution yet. It does **not** cover work that stays manual because a person must
physically be somewhere, exercise legal judgment, or hold a relationship. Those are real
reasons the work persists, but they make it unautomatable rather than promising — score
`tractability` at 0 and demote.

## Composite

Weighted sum, normalized to 0–100 by `score.py`.

- **Promotion threshold: 62**, *and* all hard gates must pass.
- Hard gates: two or more independent Tier 1/2 sources; a named buyer role; an eligible
  persistence tag; **`tractability` at 2 or above**.
- Scoring above threshold while failing a hard gate is a demote. The gates are not tiebreakers.

Tractability's weight moved from 2 to 3 (2026-09-14), which shifts the denominator slightly —
a given set of field values now scores marginally differently than it did before. The
threshold is unchanged, because it was a guess either way and needs recalibrating against
~30 real ideas regardless.

## Calibration override

`calibration/rubric-notes.md` records cases where Nathan disagreed with a rubric outcome. Read it before scoring. Where it conflicts with anchors above, his notes win.

When a new divergence appears — he rejects something scored 80, or pulls something scored 40 out of the demoted pile — that belongs in his notes file, written in his own words. Do not write it for him; surface the divergence and let him record it.

## Threshold drift

The threshold is a free parameter and will need retuning. If promotion rate climbs over successive batches without a matching rise in Nathan's acceptance rate, the critic has gone soft. Raise the threshold or re-anchor, and note the change with a date at the bottom of this file.
