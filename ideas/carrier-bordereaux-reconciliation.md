---
slug: carrier-bordereaux-reconciliation
status: demoted
cell_id: naics-524121
created: 2026-09-15
owner_agent: sweep-16
job: Carrier ceded-reinsurance and program accounting analysts manually prepare and
  reconcile premium, claims, and commission bordereaux by comparing MGA, broker, reinsurer,
  and internal system reports, because each counterparty delivers its own bordereaux
  file and none of them import automatically into the carrier's ledger.
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 2
---

# Carrier Bordereaux Reconciliation

## Problem statement

Direct P&C carriers that write business through MGAs or program administrators, and
that cede risk to reinsurers, must periodically reconcile bordereaux — premium, claims,
and commission reports — coming in from each counterparty against their own policy,
claims, and financial systems. Current job postings describe this as a dedicated
analyst function: comparing MGA, broker, reinsurer, and internal reports line by line,
investigating exceptions (missing data, duplicate activity, reporting inconsistencies),
and coordinating resolution across counterparties who each use their own file formats.

## Evidence

- [type: job-posting] (2026, undated but currently live) Accredited Insurance, a
  carrier operating exclusively through MGA partners, advertised a Senior Program
  Analyst — Insurance & Reinsurance role ($120,000–$130,000) whose duties include
  "Prepare, review, and reconcile premium, claims, commission, and reinsurance
  bordereaux using policy, claims, and financial data," "Prepare and maintain
  program-level reconciliations covering premium, commissions, claims, reinsurance,
  cash, receivables, and settlement balances," and "Compare MGA, broker, reinsurer,
  and internal system reporting and investigate differences through resolution."
  https://www.simplyhired.com/job/ki_qM7wAPeXGR0wVIXRbyFDtr8RJQzd0vTK15NLD2F4Ygv98Xz-c-A
- [type: job-posting] (2026-08-21) NextEra Energy's PALMS Insurance operation
  advertised a role to "Manage and reconcile claim statements and bordereaux with
  counterparties," "Maintain accurate records of outstanding recoverable and
  settlements in the claims management system," and "Coordinate the submission,
  tracking, and resolution of reinsurance recoveries, including facultative and
  treaty claims."
  https://www.simplyhired.com/job/LqKLrODjq7vsQeNQ2PpSo3rhN7IwYpIGHh-QBAeNYocDKSiPvn8nPw

## Automation hypothesis

SPECULATIVE. A bordereaux-reconciliation tool could ingest each counterparty's
bordereaux file (Excel/CSV/PDF, no two alike), normalize the schema against the
carrier's internal policy/claims/financial extracts, auto-match line items by
policy or claim reference, and surface only genuine exceptions (missing records,
duplicate entries, amount mismatches) for analyst review. It would need durable
per-counterparty format mappings, tolerance rules for timing differences, and an
audit trail suitable for settlement disputes with MGAs and reinsurers.

## Scrutiny decision

Demoted at triage: bordereaux ingestion, normalization, validation, and reconciliation are already a mature software category served directly by [VIPR INTRALI](https://www.viprsolutions.com/news/delegated-data-manger-to-exit-london-market), [Xceedance Bordereaux Management](https://www.xceedance.com/what-we-do/data-analytics/insurance-data-and-modeling-platforms/xceedance-bordereaux-management/), and [Appian's reinsurance automation](https://appian.com/fr/industries/insurance/re-insurance).
