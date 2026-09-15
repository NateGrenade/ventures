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

## `tractability` (weight 2)

| Value | Anchor |
|---|---|
| 0 | Blocked by a hard technical or data-access problem with no path |
| 1 | Requires integration with a closed system; feasibility unknown |
| 2 | Integration surface exists (API, export, standard file format) or the work is self-contained |
| 3 | Clean surface **and** the capability that makes it newly feasible is identifiable |

## `persistence_quality` (weight 3)

Derived from the mandatory persistence tag.

| Value | Tag |
|---|---|
| 0 | `unattractive-economics`, `fragmented-buyer`, `incumbent-distribution` |
| 1 | `regulatory-moat` — sometimes an opportunity, usually a wall |
| 1 | `unnoticed` — scored low deliberately; near-always a research failure |
| 3 | `genuinely-hard` |
| 3 | `recently-unlocked` |

## Composite

Weighted sum, normalized to 0–100 by `score.py`.

- **Promotion threshold: 62**, *and* all hard gates in SKILL.md Step 5 must pass.
- Scoring above threshold while failing a hard gate is a demote. The gates are not tiebreakers.

## Calibration override

`calibration/rubric-notes.md` records cases where Nathan disagreed with a rubric outcome. Read it before scoring. Where it conflicts with anchors above, his notes win.

When a new divergence appears — he rejects something scored 80, or pulls something scored 40 out of the demoted pile — that belongs in his notes file, written in his own words. Do not write it for him; surface the divergence and let him record it.

## Threshold drift

The threshold is a free parameter and will need retuning. If promotion rate climbs over successive batches without a matching rise in Nathan's acceptance rate, the critic has gone soft. Raise the threshold or re-anchor, and note the change with a date at the bottom of this file.
