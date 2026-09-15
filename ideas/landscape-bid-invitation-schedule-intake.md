---
slug: landscape-bid-invitation-schedule-intake
status: sandbox
cell_id: naics-561730
created: 2026-09-15
owner_agent: 2026-09-15-codex-24-resume-07
job: Landscape estimators manually copy bid invitations from email, VBX and Procore
  into an Excel bid schedule because their documented intake workflow maintains the
  schedule separately from invitation platforms and ProEst.
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 3
---

# Landscape Bid Invitation Schedule Intake

## Problem statement

A commercial landscape estimator describes filtering incoming invitations, adding relevant projects to an Excel master schedule and creating project folders before estimating in ProEst; maintaining that schedule takes time away from estimates. A separate junior-estimator posting assigns ongoing invitation and deadline updates to an employee. The supported job is intake and schedule maintenance, with no measured hours or error rate available. [type: practitioner] (date not exposed precisely; page displays four months ago, accessed 2026-09-15) https://www.reddit.com/r/estimators/comments/1tmh5j6/commercial_irrigation_and_landscape_estimating/

## Evidence

- [type: practitioner] (date not exposed precisely; page displays four months ago, accessed 2026-09-15) The poster identifies their prior irrigation/landscape supervisor role and current estimating role. They describe invitations arriving by email, VBX and Procore, then manual filtering into an Excel bid schedule and creation of folders containing selected plans. The account establishes a concrete workflow at one unidentified company; it does not establish industry prevalence. https://www.reddit.com/r/estimators/comments/1tmh5j6/commercial_irrigation_and_landscape_estimating/
- [type: job-posting] (undated; accessed 2026-09-15) Maldonado Nursery & Landscaping's Junior Landscape Estimator description, republished by Vaia, assigns adding bid invites and due dates to the schedule, updating changed deadlines, placing pre-bid meetings on shared calendars and organizing project documents. It names PlanHub, ConstructConnect and Virtual Builder as sources of bidding information. The publisher's salary estimate is not employer-confirmed and is excluded. https://talents.vaia.com/companies/maldonado-nursery-landscaping-inc/austin/junior-landscape-estimator-93136834/

## Automation hypothesis

SPECULATIVE. A bid-intake assistant could extract project identifiers, locations and due dates from permitted invitation sources, propose deduplicated schedule rows and flag deadline changes for an estimator to approve. It would retain links to source plans and invitations. The buyer hypothesis is the landscape estimating manager. Email and spreadsheet access may suffice for a narrow prototype; portal access, duplicate-project matching and existing bid-management coverage remain unverified.
