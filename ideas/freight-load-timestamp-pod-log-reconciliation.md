---
slug: freight-load-timestamp-pod-log-reconciliation
status: sandbox
cell_id: onet-43-5032.00
created: 2026-09-15
owner_agent: 2026-09-15-codex-24-sweep-01
job: Freight operations support clerks manually copy scheduled-versus-actual times
  and BOL and POD documents from multiple TMS and internal dispatch systems into OTP
  tracking sheets and detention logs, because the employer maintains audit and carrier-billing
  records across those separate systems.
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 1
---

# Freight Load Timestamp and POD Log Reconciliation

## Problem statement

GH Logistics advertised a full-time, 50-hour-per-week support role to keep load tracking, carrier compliance, and TMS records audit-ready. The role enters scheduled and actual times into an OTP tracking sheet across multiple TMS platforms, runs daily trip and load reports, uploads BOL and POD documents into OTP and detention logs, and verifies detention time for carrier billing. https://www.onlinejobs.ph/jobseekers/job/Data-Entry-Systems-Support-Clerk-FMT-Support-GH-Logistics-1358907

## Evidence

- [type: job-posting] (2026-07-06) GH Logistics offered $1,500 per month for a 50-hour-per-week clerk who enters scheduled-versus-actual times into an OTP tracking sheet across multiple TMS platforms, maintains daily LoadStop and internal-dispatch reports, uploads BOL and POD documents to OTP and detention logs, and verifies detention time for carrier billing. The listing says the role touches thousands of load entries and performs manual migration during the company's automation transition. https://www.onlinejobs.ph/jobseekers/job/Data-Entry-Systems-Support-Clerk-FMT-Support-GH-Logistics-1358907

## Automation hypothesis

SPECULATIVE. A load-audit bridge could collect timestamps and shipment documents from each TMS and dispatch system, associate them with a canonical load record, and populate OTP, detention, and billing-review queues with exceptions for human review. The listing does not establish whether the named systems offer APIs or consistent load identifiers, so document matching and write access remain unresolved.
