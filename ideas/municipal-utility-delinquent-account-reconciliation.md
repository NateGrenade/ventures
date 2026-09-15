---
slug: municipal-utility-delinquent-account-reconciliation
status: sandbox
cell_id: onet-43-3011.00
created: 2026-09-14
owner_agent: manual-1
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 4
---

# Municipal Utility Delinquent-Account Reconciliation

## Problem statement

Small-to-mid municipal utility billing offices (water/sewer/gas/sanitation)
manually balance daily revenue across multiple disconnected payment channels
— lockbox files, EFTs, web payments, walk-in — into hand-built spreadsheets,
then hand off delinquent accounts to outside collection agencies through
legacy fixed-width batch files rather than any API, with tax-refund
intercepts coordinated by phone/email against a 15-day manual-update clause.
This is daily, recurring clerical work performed by billing/collections
clerks at city and utility-district offices nationwide.

## Evidence

- [type: job-posting] City of Pinellas Park, FL "Billing and Collections
  Specialist" job description: duties include "estimates and makes manual
  adjustments to accounts as needed," "prepares spread sheet for daily and
  monthly balancing of revenues," and processing "EFTs, lockbox files, bad
  debt write offs, and payment redistributions" plus "the over-short
  adjustment process" by hand.
  https://www.pinellaspark.gov/DocumentCenter/View/8774/Billing-and-Collections-Specialist_A-PDF
- [type: procurement] East Bay Municipal Utility District RFP for
  "Collection Service on Delinquent Accounts" (RFP response due July 15,
  2022): Exhibit F specifies a fixed-width mainframe-era flat-file format
  (header/detail/footer record types 1/6/9, positions defined to the byte)
  as the payment-data interchange method between the utility and its
  contracted collection agency — no API or EDI. Section I.C.2 requires the
  District to manually notify the collection agency within 15 days whenever
  the state Franchise Tax Board's intercept program collects against a
  debtor's tax refund, and to manually supply the updated outstanding
  balance.
  https://www.ebmud.com/download_file/force/13275/2445?Collection_Service_on_Delinquent_Accounts_RFP.pdf=
- [type: procurement] City of Thomson, GA RFP #25-010 "Debt Collection
  Agency Services" (issued September 29, 2025): city bills ~8,200 water,
  4,700 sewer, 3,400 sanitation, and 2,700 gas accounts and is soliciting an
  outside agency because delinquent-account follow-up is not handled by any
  integrated system internally.
  https://thomson-mcduffie.gov/DocumentCenter/View/728/Debt-Collection---RFP?bidId=
- [type: job-posting] City of Glenpool, OK "Utility Billing Clerk" job
  description: duties include "post readings into the computer and make
  changes as are necessary to correct accounts" and "prepare an assortment
  of printouts as necessary for the City," covering cutoffs, meter changes,
  and data analysis — clerk-driven, not system-driven.
  https://www.glenpoolonline.com/DocumentCenter/View/819/Utility-Billing-Clerk

## Automation hypothesis

SPECULATIVE. A thin reconciliation layer that ingests each payment channel's
native export (lockbox flat file, EFT/ACH file, web-payment gateway export)
and the collection agency's own fixed-width batch format, matches and posts
them against the utility billing system, and flags exceptions (the
"over-short adjustment process" named in the Pinellas Park posting) could
plausibly absorb the daily spreadsheet-balancing work. The integration
surface is the constraint: it would need to speak whatever legacy utility
billing platform each municipality runs (varies widely, often decades old)
and match the collection agency's proprietary flat-file spec per contract —
this looks more like a services-heavy, per-customer integration business
than a horizontal SaaS product, at least initially.
