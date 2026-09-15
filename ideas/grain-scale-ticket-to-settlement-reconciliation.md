---
slug: grain-scale-ticket-to-settlement-reconciliation
status: sandbox
cell_id: naics-493130
created: 2026-09-15
owner_agent: 2026-09-15-codex-24-sweep-03
job: grain accounting clerks manually enter and apply scale tickets and grain contracts
  to producer settlements between scale records and accounting software, because current
  cooperative workflows still assign clerks to enter, balance, reconcile, and correct
  those transactions.
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 4
---

# Grain Scale-Ticket-to-Settlement Reconciliation

## Problem statement

Grain cooperative accounting staff carry delivery data from scale tickets and contracts
through producer accounts, inventory, settlement, and payment. Current employer artifacts
assign staff to enter contracts in accounting software, apply scale tickets to producer
accounts, balance tickets at day end, and resolve inventory or settlement discrepancies
([Five Star Cooperative](https://recruiting.paylocity.com/recruiting/jobs/Details/4328843/Five-Star-Cooperative/Grain-Feed-Accounting-Assistant),
[United Farmers Cooperative](https://storageatlasengagepdcus.blob.core.windows.net/atlas/all-media/unitedfarmers/content/job-descriptions/grain-scale-operator-customer-service-job-description.pdf)).

## Evidence

- [type: job-posting] (undated, current listing accessed 2026-09-15) Five Star
  Cooperative's Grain & Feed Accounting Assistant maintains shipment, contract,
  settlement, scale-ticket, billing, and payment records; enters grain contracts and
  modifications into the accounting system; and reconciles grain inventory transactions
  and accounting discrepancies.
  https://recruiting.paylocity.com/recruiting/jobs/Details/4328843/Five-Star-Cooperative/Grain-Feed-Accounting-Assistant
- [type: job-posting] (2026, current job description accessed 2026-09-15) United Farmers
  Cooperative assigns a grain scale operator to apply scale tickets to producer accounts,
  balance tickets through end-of-day processing, produce grain settlements, issue grain
  contracts, and maintain physical and electronic compliance filing for multiple locations.
  https://storageatlasengagepdcus.blob.core.windows.net/atlas/all-media/unitedfarmers/content/job-descriptions/grain-scale-operator-customer-service-job-description.pdf
- [type: job-posting] (undated, current listing accessed 2026-09-15) A GROWMARK/Total
  Grain Marketing scale-clerk listing explicitly requires entering scale tickets,
  contracts, and other documents into grain accounting software.
  https://jobs.growmark.com/fssystem/job/Lis-Scale-Clerk-Total-Grain-Marketing%2C-LLC-Lis%2C-IL-IL-62448/1418241900/
- [type: job-posting] (undated, current listing accessed 2026-09-15) Agri Trails Coop's
  Grain Accounting Specialist processes inbound and outbound settlements, enters records
  of account and grain checks into AgTrax, applies settlements to contracts, and contacts
  terminal elevators for settlement corrections.
  https://www.indeed.com/viewjob?jk=d985a1f3014a3487 [UNREACHABLE]

## Automation hypothesis

SPECULATIVE. A workflow layer could ingest scale-ticket documents and contract records,
propose their application to producer accounts, and surface exceptions before posting to
the grain accounting system. The evidence establishes recurring human entry, balancing,
and correction; it does not establish which incumbent systems expose usable APIs or how
often straight-through posting is already configured.
