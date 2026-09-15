---
slug: securitization-abs-ee-filing-assembly
status: sandbox
cell_id: naics-526981
created: 2026-09-15
owner_agent: 2026-09-15-codex-24-resume-02
job: Securitization compliance analysts manually transform and verify monthly asset-level
  data from accounting files into Form 10-D and Form ABS-EE packages for EDGAR, because
  servicing and accounting systems do not produce complete SEC-formatted disclosures.
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 3
---

# Securitization ABS-EE Filing Assembly

## Problem statement

Issuer compliance staff receive monthly asset-level data files and certificates from
securitization accounting, process and check them, and prepare, review, and revise Form
10-D and Form ABS-EE packages before filing. An employer listing removed in January 2025 assigned this
cycle across approximately 20 outstanding transactions each month. A current industry
comment to the SEC says originating and servicing systems still cannot readily gather
all required Schedule AL fields, while firms pay filing agents to convert Excel files
into the SEC format and employ additional staff to oversee Exchange Act compliance.

## Evidence

- [type: job-posting] (posting removed 2025-01-30) JM Family Enterprises — “Senior
  Compliance Analyst” / Securitization and Treasury Compliance Associate. The role
  prepares, reviews, and revises Form 10-D and Form ABS-EE drafts for approximately 20
  outstanding securitization transactions each month; receives monthly asset-level data
  files and certificates from Securitization Accounting; processes them and confirms
  certificate accuracy; and requires Excel plus knowledge of ABS-EE and SEC compliance.
  https://builtin.com/job/senior-compliance-analyst/3728954 [UNREACHABLE]
- [type: regulatory] (2025-12-01) SIFMA and SIFMA AMG told the SEC that issuers cannot
  readily obtain all Schedule AL data elements across originating, servicing, and other
  business systems on a monthly basis. The letter says a third-party provider charges
  approximately $1,000–$2,000 to format an Excel file into the SEC data format and file
  it on EDGAR, excluding the cost of staff hired to oversee Exchange Act compliance.
  https://www.sec.gov/comments/s7-2025-04/s7202504-680387-2095754.pdf
- [type: regulatory] (2024-05-14) A KeyBank primary-servicing agreement filed on EDGAR
  requires recurring electronic handoffs among primary and master servicers, including
  remittance and collection reports, a Schedule AL file in both EDGAR-compatible and
  Excel formats, and optional Schedule AL additional files. The primary servicer may rely
  on the initial files supplied by the master servicer, showing that the disclosure is
  assembled through contractual file exchanges between transaction parties.
  https://www.sec.gov/Archives/edgar/data/2020017/000153949724001000/exh4-19_keybank.htm

## Source limitation

The employer listing is historical and was retrieved through web search; its URL failed the repository verifier. It does not establish an active vacancy. The December 2025 industry comment and 2024 servicing agreement separately support recurring disclosure preparation and file handoffs.

## Automation hypothesis

SPECULATIVE. A compliance workspace could ingest accounting’s monthly asset-level file
and certificates, map the fields to the applicable Schedule AL schema, run completeness
and cross-document checks, generate reviewer exceptions, and produce a filing-agent-ready
Form ABS-EE package alongside the related Form 10-D draft. This would be tractable only
if each shelf’s source-file layouts and deal-specific disclosure rules can be configured
without weakening the issuer’s legal review and sign-off controls.
