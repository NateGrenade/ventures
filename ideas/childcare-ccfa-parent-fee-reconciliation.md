---
slug: childcare-ccfa-parent-fee-reconciliation
status: sandbox
cell_id: onet-11-9031.00
created: 2026-09-15
owner_agent: 2026-09-15-codex-24-resume-05
job: Childcare program administrative staff manually reconcile parent fee assessments
  between Massachusetts CCFA and Procare or their current child care management system,
  because their documented workflow requires separate fee-entry audits and cross-system
  checks.
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 2
---

# Childcare CCFA Parent Fee Reconciliation

## Problem statement

Nurtury's childcare administration workflow assigns a staff member weekly or monthly checks of parent fee assessments entered into Procare or another child care management system, followed by monthly reconciliation against Massachusetts CCFA and recommendations to the enrollment team. This is a concrete cross-system control in one provider's March 2025 job posting; its continuation in September 2026 and labor hours have not been established. https://www.jobtarget.com/jobs/jt-yuj4brg0iq/junior-accountant-for-non-profit-child-care-agency-boston-massachusetts

## Evidence

- [type: job-posting] (2025-03-28) Nurtury's Junior Accountant posting assigns recurring audits of parent fee assessments and their entry into Procare/current CCMS, plus monthly reconciliation of those fees against the state CCFA billing system and reporting to enrollment staff. The posting establishes human review across named systems, but does not establish why existing software cannot eliminate it. Search-indexed posting text was readable on 2026-09-15; direct web open returned a cache miss. https://www.jobtarget.com/jobs/jt-yuj4brg0iq/junior-accountant-for-non-profit-child-care-agency-boston-massachusetts
- [type: regulatory] (2026-05-06) Massachusetts EEC's consolidated income-eligible CCFA policies describe parent fees based on household income and size, determined at authorization, reauthorization, and certain reported changes. This supports the changing fee inputs that providers must administer; it does not independently establish Nurtury's manual reconciliation or the absence of an integration. Search-indexed policy text was readable on 2026-09-15; direct PDF web open returned HTTP 403. https://www.mass.gov/doc/eec-ccfa-2026-04-income-eligible-consolidated-policies-may-6-2026/download

## Automation hypothesis

SPECULATIVE. A provider-side reconciliation tool could compare authorized parent fees exported from CCFA with charges in Procare/current CCMS, match family identifiers and effective dates, and send exceptions to the enrollment team for approval. The buyer hypothesis is the childcare provider's administrative or finance lead. Feasibility depends on lawful export access, reliable identity matching, and confirmation that current CCMS integrations leave this specific reconciliation unresolved. The available evidence does not quantify time savings or establish unmet demand across providers.
