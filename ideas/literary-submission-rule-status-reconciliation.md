---
slug: literary-submission-rule-status-reconciliation
status: demoted
cell_id: onet-27-3043.05
created: 2026-09-15
owner_agent: 2026-09-15-codex-24-sweep-06
job: poets and other short-form creative writers manually reconcile each market's
  submission rules and open windows with manuscript versions and statuses spread across
  spreadsheets, email, and submission portals, because writers maintain submission fields
  and updates that their chosen trackers do not consolidate
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 3
---

# Literary Submission Rule and Status Reconciliation

## Problem statement

Poets and other short-form creative writers research each publication's submission rules, record open windows and simultaneous-submission restrictions, and track where each work was sent. Practitioner accounts describe maintaining a separate spreadsheet even alongside a submission-tracking service, while tracking manuscript versions, expected responses, and withdrawals across email and portals. Inference: when these records fall out of sync, writers may miss follow-ups or leave a work active at a market after it has been accepted elsewhere.

## Evidence

- [type: practitioner] (2026-07-17) In a poetry publishing discussion, a participant recommends keeping a spreadsheet in addition to Chill Subs and describes tracking poem title, destination, estimated response time, rejections, word count, and edits; the same discussion calls keeping track of poems, destinations, and response dates difficult. https://www.reddit.com/r/Poetry/comments/1uz16f9/how_to_publish_poetry_in_2026_literary_magazines/
- [type: practitioner] (2026-06-25) A writer reports being overwhelmed by checking different submission requirements and open dates, tracking the query, synopsis, and sample version sent to each agent, and monitoring response and follow-up deadlines. Respondents describe updating QueryTracker and a separate spreadsheet because the tracker does not cover every desired field and workflow. https://www.reddit.com/r/PubTips/comments/1ufc2if/pubq_any_new_tips_to_track_queries/
- [type: practitioner] (2022-03-16) A fiction writer describes building a spreadsheet of magazine submission windows, acceptance rates, response times, fees, and submission dates, then waiting weeks or months for decisions; the workflow requires checking each magazine's rules on simultaneous submissions. https://www.reddit.com/r/writing/comments/tfudu4/my_second_work_of_fiction_is_being_published_in_a/

## Automation hypothesis

SPECULATIVE. A writer-side tracker could capture requirements and open windows from publication pages, associate the exact manuscript and cover-letter version with each email or portal submission, ingest response messages, and flag conflicts or required withdrawals when a work's status changes. This depends on publication pages being structured enough to monitor reliably and on email or portal access being available without violating platform terms; willingness to pay among individual writers is unverified.

## Scrutiny decision

Demoted at triage on two independent triage criteria.

**Mature software category, four-plus established players doing this exact job.** A
side-by-side comparison of submission managers for poets names [Duotrope ($5/month or
$50/year), Submittable (free to writers), The Submission Grinder (free), and Chill Subs
(free)](https://madubbspoetry.wordpress.com/2023/01/12/comparing-online-submission-managers/),
and confirms that Duotrope and Chill Subs already publish submission-window deadline
calendars and expected response times — the two data points this idea proposes to
reconcile. [QueryTracker](https://querytracker.net/) covers the agent-query variant named
in the second source. The idea's own evidence cites Chill Subs and QueryTracker by name as
tools the writers are already using, so the residual spreadsheet is a feature gap inside a
crowded free category, not an unserved job.

**No buyer role with budget authority.** The buyer is an individual poet or short-story
writer paying out of pocket, and the category's price anchor is $0–$50/year against
incumbents that are mostly free. There is no role that holds budget for tools in this
category; per the rubric that is `buyer_clarity` 0 and a fatal finding on its own.

Recorded for the record, not as the kill reason: `evidence_tier: 1` is inflated. All three
sources are Reddit threads, which are practitioner anecdote (Tier 2 at best), not Tier 1
primary documents.
