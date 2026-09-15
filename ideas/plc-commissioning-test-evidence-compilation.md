---
slug: plc-commissioning-test-evidence-compilation
status: sandbox
cell_id: onet-17-2199.05
created: 2026-09-15
owner_agent: 2026-09-15-codex-24-sweep-05
job: Controls engineers manually translate I/O lists and PLC/HMI behavior into stepwise
  test scripts and signed FAT/SAT records between engineering project files and customer
  handover documents, because the tables and acceptance evidence are maintained in
  separate office documents.
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 4
---

# PLC Commissioning Test Evidence Compilation

## Problem statement

Controls engineers prepare commissioning procedures from I/O lists and control behavior, then record operator or inspector sign-offs for individual checks in customer-facing test documents. A practitioner describes using Word for the test plan and Excel linked to PLC variables, while another describes stepwise input/expected-output documents with initials on every line; current job postings assign I/O lists, test reports, FAT, and SAT documentation to automation engineers.

## Evidence

- [type: practitioner] (2023-02-28) A controls practitioner says they use Word to create test plans and suggests linking PLC variables into an Excel sheet; the discussion notes that a documentation format produced several tables that all had to match. https://www.reddit.com/r/PLC/comments/11e66fk/commissioning_automation/
- [type: practitioner] (2023-04-22) A PLC practitioner describes a client-specified FAT document containing step-by-step inputs, expected outputs, and initials boxes for the test operator and inspector; another describes an Excel object list with separate I/O, alarm, HMI/SCADA, and communications checks. https://www.reddit.com/r/PLC/comments/12v6jtk/functional_testing_of_plc_code/
- [type: job-posting] (2026-07) A senior PLC and automation engineer posting assigns I/O lists, test documentation, change controls, FAT, SAT, and commissioning to a role requiring an automation, electrical, electronic, mechatronic, or related engineering degree. https://builtin.com/job/senior-rockwell-plc-automation-engineer/9906964
- [type: procurement] (2025-10-01) A municipal SCADA upgrade proposal requires authored FAT documentation, a SAT test-plan document, and test documentation signed off after completion. https://www.clackamasriverwater.gov/files/932cfc921/CRW%2BReg%2BBoard%2BMtng%2BPacket%2B10.09.2025.pdf

## Automation hypothesis

SPECULATIVE. A tool could ingest I/O exports, tag databases, control narratives, and customer templates to generate version-linked FAT/SAT steps, capture evidence and signatures during execution, and produce a handover package. This depends on reliable parsers for the PLC vendor exports and on preserving the customer's required document format and approval trail.
