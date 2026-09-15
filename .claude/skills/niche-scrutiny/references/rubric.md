# Scrutiny Rubric — Anchored Scales

Emit integer values for each dimension into the `scores:` frontmatter map. `score.py` computes the composite. Anchors are binding: pick the anchor that matches the evidence you actually have, not the one that matches your impression.

**Weights, floors, and the threshold are not stated in the prose below.** They live in
`config/scoring.yaml` and are reproduced in the generated block at the end of this file,
which is the authoritative copy. Where prose and that block disagree, the block wins.

<!-- GENERATED FROM config/scoring.yaml — do not edit by hand -->

**Active profile: `balanced` — promotion threshold 62/100.**

| dimension | weight | hard floor |
|---|---|---|
| `buyer_clarity` | 3 | — |
| `deal_economics` | 3 | 1 |
| `pain_evidence` | 3 | — |
| `persistence_quality` | 3 | — |
| `replicability` | 3 | 2 |
| `tractability` | 3 | 2 |
| `incumbent_gap` | 2 | — |
| `reachability` | 2 | — |

Maximum raw score 66, normalized to 100.

Revenue ceiling bands (`buyer_count` × `annual_price_usd`):

- ≥ $500,000 → `deal_economics` 3
- ≥ $100,000 → `deal_economics` 2
- ≥ $25,000 → `deal_economics` 1
- ≥ $0 → `deal_economics` 0

Other gates: at least 2 sources, evidence tier 2 or better, a named buyer role, persistence in ['recently-unlocked', 'genuinely-hard'].

A hard floor is absolute: scoring below it is a demote whatever the composite says.
Floors shown as — are disabled in this profile.

To change any of this, edit `config/scoring.yaml` and re-run `python scripts/render_rubric.py`. Check the effect on the real corpus first with `python scripts/tune.py --compare`.

<!-- END GENERATED -->

## `pain_evidence`

| Value | Anchor |
|---|---|
| 0 | Only Tier 3 sources, or the pain is inferred rather than described |
| 1 | One Tier 1/2 source describing the manual work |
| 2 | Two or more independent sources; at least one Tier 1 |
| 3 | Multiple Tier 1 sources **plus** a dollar figure attached — salary band from a job posting, burden hours from a filing, contract value from an RFP |

## `buyer_clarity`

| Value | Anchor |
|---|---|
| 0 | No identifiable budget holder; pain distributed across fractions of many roles |
| 1 | A role exists but budget authority is unclear or sits several levels up |
| 2 | Named role that plausibly holds budget for tools in this category |
| 3 | Named role, and evidence they already buy something adjacent — an existing line item you would displace or sit beside |

## `incumbent_gap`

| Value | Anchor |
|---|---|
| 0 | Three or more direct competitors, mature category |
| 1 | One or two direct competitors serving this job adequately |
| 2 | Adjacent players only; nobody targets this job specifically |
| 3 | No direct or adjacent player found after genuine search; the substitute is a spreadsheet, a temp, or an offshore team |

*A 3 here demands you actually searched. Record the queries you ran in the scrutiny log. "Found no competitors" without recorded queries scores 1.*

## `reachability`

How you would get in front of the buyer.

| Value | Anchor |
|---|---|
| 0 | No channel; buyers are numerous, tiny, and unaggregated |
| 1 | Channel exists but is expensive — field sales, long procurement |
| 2 | Identifiable aggregation point: trade association, conference, dominant forum, industry newsletter |
| 3 | Buyers are concentrated, or an existing distributor could carry it |

## `tractability`

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

## `deal_economics` — DERIVED, do not emit

`score.py` computes this. Your job is to supply two sourced frontmatter numbers:

```yaml
buyer_count: 4200          # organizations plausibly reachable AND plausibly buying
annual_price_usd: 4800     # defensible annual price per buyer
```

The ceiling is their product, bucketed per the generated block below.

**Leaving the numbers undetermined is a demote wherever the floor is active.** A
market that cannot fund its own maintenance is not a market, and "we couldn't tell" is not
a reason to promote — it is a reason to go find out.

Both numbers need a derivation in the scrutiny log. `buyer_count` should come from a firm
count (Census County Business Patterns, a licensing roster, an association directory), then
cut by the fraction plausibly large enough to have this problem — state that fraction and
rate your confidence in it, because it is usually the load-bearing assumption. Price should
be anchored to something the buyer already pays for, not invented.

Do not pad the count with organizations you have no way to reach. `reachability` and this
dimension are supposed to bite separately; inflating one to rescue the other defeats both.

## `replicability`

Does customer #2 cost materially less to serve than customer #1?

| Value | Anchor |
|---|---|
| 0 | Every customer is a bespoke integration; #2 costs about what #1 did |
| 1 | Core logic is shared, but each buyer needs custom connector work |
| 2 | One integration surface serves a meaningful share of buyers — a dominant vendor, a common export format |
| 3 | A single standard covers most of the market — mandated schema, regulated filing format, one vendor with commanding share |

**Scoring 2 or 3 requires naming the standard or vendor, with evidence of its share.** "The
formats are probably similar" scores 0.

This dimension exists because of how the ideas get used. A $200k/yr niche that is one
codebase serving forty customers can be built and left running while you move to the next
one. A $2M/yr niche that is twelve bespoke integrations is a consulting firm, and it will
consume all the time the second product needed. Raw market size cannot tell those apart.

**This floor is the most opinionated number in the configuration.** It is set for stacking
several small products rather than building one large one. It is disabled entirely in the
`introductory` profile, which is the right setting while still learning what these
businesses are like.

## `persistence_quality`

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
  persistence tag; `tractability` ≥ 2; **revenue ceiling ≥ $25k/yr and determined**;
  **`replicability` ≥ 2**.
- Scoring above threshold while failing a hard gate is a demote. The gates are not tiebreakers.

Tractability's weight moved from 2 to 3 (2026-09-14). `deal_economics` and `replicability`
were added at weight 3 each (2026-09-15), taking the maximum raw score from 48 to 66.

The threshold stays at 62, but expect the promotion rate to fall sharply — two new hard
gates now apply, and one of them (an undetermined revenue ceiling) will fail ideas that
would previously have sailed through on strong pain evidence alone. That is the intent.
If the rate falls to zero across thirty ideas, the problem is more likely the $25k floor or
the replicability floor than the threshold; check which gate is firing before touching
anything.

## Calibration override

`calibration/rubric-notes.md` records cases where Nathan disagreed with a rubric outcome. Read it before scoring. Where it conflicts with anchors above, his notes win.

When a new divergence appears — he rejects something scored 80, or pulls something scored 40 out of the demoted pile — that belongs in his notes file, written in his own words. Do not write it for him; surface the divergence and let him record it.

## Threshold drift

The threshold is a free parameter and will need retuning. If promotion rate climbs over successive batches without a matching rise in Nathan's acceptance rate, the critic has gone soft. Raise the threshold or re-anchor, and note the change with a date at the bottom of this file.
