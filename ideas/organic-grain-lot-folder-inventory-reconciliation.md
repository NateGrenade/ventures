---
slug: organic-grain-lot-folder-inventory-reconciliation
status: sandbox
cell_id: naics-493130
created: 2026-09-15
owner_agent: 2026-09-15-codex-24-sweep-03
job: organic grain warehouse administrators manually match scale and shipping records
  between paper lot folders and electronic inventory balances, because each lot's
  traceability trail spans operational documents, physical files, and system records.
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 3
---

# Organic Grain Lot-Folder Inventory Reconciliation

## Problem statement

An April 2026 organic grain-storage posting assigns one administrator to ensure tickets match
operational and inventory records, entries match lot folders and system balances, and
physical and electronic inventory records stay accurate across locations
([Triple Nickel](https://tallo.com/talent/job/business/scheduler-or-operations-coordinator/tx/muleshoe/front-desk-scaleadmin-2679424c [UNREACHABLE])).
The records must preserve the lot trail through handling, transport, and sale under current
organic recordkeeping rules
([7 CFR 205.103](https://www.ecfr.gov/current/title-7/subtitle-B/chapter-I/subchapter-M/part-205/subpart-B/section-205.103)).

## Evidence

- [type: job-posting] (2026-04-02; updated 2026-04-05) Triple Nickel's Front Desk
  (Scale/Admin) posting says the role ensures scale tickets align with operational and
  inventory records, maintains physical and electronic inventory accuracy, matches entries
  to lot folders and system balances, resolves discrepancies, tracks grain-cleaning totes
  and samples by lot, and completes organic handling paperwork.
  https://tallo.com/talent/job/business/scheduler-or-operations-coordinator/tx/muleshoe/front-desk-scaleadmin-2679424c [UNREACHABLE]
- [type: regulatory] (current through 2026-09-11) 7 CFR 205.103 requires certified
  operations' records to disclose all activities and transactions from acquisition through
  sale or transport, include audit-trail documentation, remain traceable to the last
  certified operation, and be available for inspection.
  https://www.ecfr.gov/current/title-7/subtitle-B/chapter-I/subchapter-M/part-205/subpart-B/section-205.103
- [type: regulatory] (2007-03-29; current guidance accessed 2026-09-15) OCIA's audit-trail
  guidance requires storage inventory records with storage-unit ID, source, lot number,
  inbound and outbound quantities and dates, destination, and current balance; it also says
  the lot number should appear on weigh tickets, bills of lading, invoices, and transaction
  certificates.
  https://ocia.org/wp-content/uploads/2024/12/EN-NQ-T-002.pdf

## Verification limitation

The full Tallo posting was read through web browsing again on 2026-09-15, including the lot-folder and system-balance duties. Its embedded WorkInTexas record lists an expiry of 2026-05-02, while the outer listing shows 2026-05-27; both have passed. It is historical evidence, not confirmation of an active vacancy. The repository URL verifier could not reach the page. The regulatory sources corroborate recordkeeping obligations, not the employer-specific manual workflow; that workflow rests on this one dated posting.

## Automation hypothesis

SPECULATIVE. A reconciliation tool could extract lot IDs from scale tickets, bills of
lading, cleaning records, and transaction certificates, compare them with the warehouse's
inventory balance, and present missing links or quantity mismatches for review. The dated
posting describes a mixed paper-and-system workflow at one operator; further research
would need to show how common that arrangement is among organic grain warehouses.
