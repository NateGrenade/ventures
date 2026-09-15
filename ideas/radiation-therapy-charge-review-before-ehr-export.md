---
slug: radiation-therapy-charge-review-before-ehr-export
status: sandbox
cell_id: onet-29-1124.00
created: 2026-09-15
owner_agent: 2026-09-15-codex-24-resume-08
job: Radiation therapists manually review and correct treatment charge records between
  ARIA or MOSAIQ and the hospital EHR export queue, because automated charge interfaces
  retain a human accuracy check before billing release.
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 3
---

# Radiation Therapy Charge Review Before EHR Export

## Problem statement

Radiation therapists review treatment charges before releasing them into the hospital billing record. UT Southwestern's October 2023 audit describes a peer therapist checking charges in MOSAIQ before its nightly Epic export. This establishes recurring administrative review despite an existing interface, but does not measure labor hours or establish which checks could be automated. Source: https://utsystem.edu/sites/default/files/documents/ut-system-reports/2023/utsw-radiation-oncology-charge-capture-and-reconciliation-report/utsw-radiation-oncology-charge-capture-and-reconciliation-report.pdf

## Evidence

- [type: job-posting] (2021-07) UW Health's Radiation Therapist – Clinical Documentation Specialist position description assigns daily review of treatment charges and necessary edits before export to HealthLink. The document also names ARIA among departmental systems. This is an older role description, not proof of a currently open vacancy. Search-indexed employer text was readable on 2026-09-15; direct web PDF open returned an internal error. https://www.uwhealth.org/files-directory/position-descriptions/technologists-technicians/radiation.therapist.clin.doc.spec.500037.pdf [UNREACHABLE]
- [type: institutional] (2023-10-19; audit period 2022-07 through 2023-06) UT Southwestern's public internal audit describes therapist entry into ARIA or MOSAIQ, an hourly ARIA-to-MOSAIQ interface, peer therapist review/correction, and release for nightly Epic export. The report describes strong existing reconciliation processes overall and corrective-action plans; persistence of the same workflow in 2026 is unverified. The candidate is the therapist's pre-export review, not the financial analyst's separate end-of-treatment review. https://utsystem.edu/sites/default/files/documents/ut-system-reports/2023/utsw-radiation-oncology-charge-capture-and-reconciliation-report/utsw-radiation-oncology-charge-capture-and-reconciliation-report.pdf
- [type: practitioner] (2024-08-06 through 2024-08-08) Respondents in a radiation-therapy practitioner thread describe checking their own billed charges weekly and daily billing review among extra duties. This corroborates recurring checks but does not identify systems, quantify time, or independently verify respondents' employment. Search-indexed discussion was readable on 2026-09-15; direct web open returned an internal error. https://www.reddit.com/r/RadiationTherapy/comments/1ekr1w6/

## Automation hypothesis

SPECULATIVE. A pre-export exception worklist could compare recorded services with draft charges, identify missing identifiers, duplicate entries, unreviewed records, and mismatches in export status, then present supporting records to the therapist. The buyer hypothesis is radiation oncology departmental administration. Existing interfaces already move charges; the untested question is whether a useful share of the retained review consists of repeatable data checks. Clinical interpretation, coding judgment, and charge approval remain with qualified staff. Current workflow validation, access to vendor interfaces, and measured review time are prerequisites to pursuing this candidate.
