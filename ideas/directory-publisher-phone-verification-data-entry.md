---
slug: directory-publisher-phone-verification-data-entry
status: demoted
cell_id: naics-511140
created: 2026-09-15
owner_agent: sweep-6
job: teleresearch associates at business-directory/mailing-list compilers manually
  phone businesses on a fixed script and hand-key the answers (name, address, employee
  count, key personnel, line of business) into the compiler's internal business database,
  because the compiler has no automated way to pull structured updates out of an unstructured
  phone conversation.
split_from: null
evidence_tier: 1
scores:
  deal_economics: 0
human_verdict: null
cost_usd: null
source_count: 2
revenue_ceiling_usd: null
composite: 0
gate_pass: false
scored_profile: balanced
---

# Directory Publisher Phone-Verification Data Entry

## Problem statement

Directory and mailing-list publishers (NAICS 511140) sell licensed access to
business databases (name, address, employee size, key personnel, line of
business) that must be kept current. To do this, they run outbound phone
campaigns in which a human caller reads a fixed script to a business, asks it
to confirm or correct its basic details, and then types the answers directly
into the publisher's internal database. This is a standing, high-volume,
entry-level job function, not a one-off project: postings for it recur and
describe production quotas and accuracy targets, implying it is treated as a
core, ongoing operational line rather than a side task.

## Evidence

- [type: job-posting] (posting removed 2026-01-14, was live prior) Data Axle
  "Teleresearch Associate" (remote, USA) job description: "Conduct a short,
  scripted phone interview with via our auto-dialer to companies across the
  country to verify and gather their basic business information," "Use basic
  computer skills to enter the gathered information into our database," and
  "Maintain 99% accuracy rate while meeting company standards for
  production." Data collected includes company name, address, employee size,
  key personnel, and lines of business; average call time under one minute.
  https://builtin.com/job/teleresearch-associate/7660820
- [type: vendor] (2020-03-04) Data Axle (then Infogroup) states on its own
  news page that it "makes more than 24 million verification calls per year
  to ensure data quality," corroborating that phone-based manual verification
  is run at large, recurring scale rather than as an occasional cleanup
  project. https://www.data-axle.com/about-us/news-media-coverage/infogroup-unleashes-all-in-one-solution-for-business-owners-everywhere/

## Automation hypothesis

SPECULATIVE. The integration surface is narrow and well defined: a scripted
set of questions, asked of a business contact, with answers that map directly
onto fixed database fields. This is close to the sweet spot for an AI voice
agent that places the call, asks the same script, transcribes and normalizes
the answers, and writes them into the compiler's database via API — removing
the human "listen, then hand-key" step entirely. What would have to be true:
(1) the compiler's database schema and field validation rules are stable and
documented enough to map voice-agent output directly into records without a
human review step for most calls, and (2) call recipients (small business
staff) tolerate a voice-AI caller as well as they tolerate a human one, since
directory compilers are already sensitive to response/completion rates on
these campaigns. A partial (human-review-in-the-loop) product may be more
realistic than full end-to-end automation given the accuracy bar (99%) these
firms already hold themselves to.

## Scrutiny triage

Demoted: the two cited items are both Data Axle-originated accounts of Data Axle's own workflow, so they do not satisfy the two-independent-sources gate ([job posting](https://builtin.com/job/teleresearch-associate/7660820); [company news release](https://www.data-axle.com/about-us/news-media-coverage/infogroup-unleashes-all-in-one-solution-for-business-owners-everywhere/)).
