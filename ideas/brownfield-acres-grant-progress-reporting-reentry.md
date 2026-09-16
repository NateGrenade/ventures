---
slug: brownfield-acres-grant-progress-reporting-reentry
status: demoted
cell_id: onet-11-9199.11
created: 2026-09-15
owner_agent: sweep-15
job: Brownfield redevelopment program managers at grant-recipient organizations manually
  re-enter site status, funding, and accomplishment data into EPA's ACRES system every
  quarter and year to satisfy cooperative agreement reporting terms, because their
  internal project files and spreadsheets do not sync with ACRES's web forms.
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 2
---

# Brownfields ACRES Grant Progress Reporting Re-entry

## Problem statement

Recipients of EPA Brownfields cooperative agreements (assessment, cleanup, revolving
loan fund, and area-wide planning grants) must submit quarterly and annual progress
reports into EPA's Assessment, Cleanup and Redevelopment Exchange System (ACRES). The
program manager or site manager assembling these reports pulls site status, funding
drawdown, and accomplishment figures from internal tracking (spreadsheets, project
files, other grant systems) and keys it into ACRES's reporting forms for every active
site and cooperative agreement, on a recurring quarterly/annual cycle for the life of
each grant.

## Evidence

- [type: regulatory] (2024-10-25) EPA's proposed Information Collection Request for
  "Brownfields Program--Accomplishment Reporting in ACRES" states EPA requires program
  recipients to "maintain and report additional information to EPA on the uses and
  accomplishments associated with funded brownfields activities," and estimates 2,697
  respondents, 11,548 annual burden hours, and $1,622,953 in annual respondent cost. The
  notice also states recipients "have always been required to submit quarterly and
  annual progress reports" and that electronic in-ACRES forms with data prefill were
  only recently introduced to reduce (not eliminate) the reporting burden.
  https://www.federalregister.gov/documents/2024/10/25/2024-24843/agency-information-collection-activities-proposed-information-collection-request-comment-request
- [type: regulatory] (2026-01-16) EPA's follow-on submission to OMB for the same
  information collection (EPA ICR Number 2104.10, OMB Control Number 2050-0192) confirms
  the ACRES accomplishment-reporting requirement remains active and under Paperwork
  Reduction Act review as of January 2026, with a comment deadline of February 17, 2026 —
  showing this is a live, current recurring reporting obligation rather than a legacy one.
  https://www.federalregister.gov/documents/2026/01/16/2026-00781/agency-information-collection-activities-submission-to-the-office-of-management-and-budget-for

## Automation hypothesis

SPECULATIVE. A tool that ingests a grantee's internal site-tracking spreadsheet or
project database and maps it to ACRES's reporting schema — pre-filling quarterly and
annual accomplishment, funding, and site-status fields for review before submission —
could absorb a meaningful share of the ~11,500 hours/year EPA itself estimates recipients
spend on this. This depends on ACRES exposing a stable form structure or API surface (the
2024 notice suggests EPA has only just begun adding prefill/electronic forms itself) and
on grantees keeping internal records in a structured-enough format to map automatically;
highly ad hoc internal tracking would limit how much of the re-entry step can be removed.

## Evaluation & Scrutiny Log

Demoted at triage: both citations are notices from EPA for the same information collection (EPA ICR 2104.10, OMB 2050-0192), so the idea has fewer than two independent sources. https://www.federalregister.gov/documents/2026/01/16/2026-00781/agency-information-collection-activities-submission-to-the-office-of-management-and-budget-for
