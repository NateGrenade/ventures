---
slug: plc-commissioning-test-evidence-compilation
status: demoted
cell_id: onet-17-2199.05
created: 2026-09-15
owner_agent: 2026-09-15-codex-24-sweep-05
job: Controls engineers manually translate I/O lists and PLC/HMI behavior into stepwise
  test scripts and signed FAT/SAT records between engineering project files and customer
  handover documents, because the tables and acceptance evidence are maintained in
  separate office documents.
split_from: null
evidence_tier: 1
buyer_role: Director of Automation or Engineering Manager at a control-system integrator
buyer_count: 100
annual_price_usd: 420
persistence: regulatory-moat
scores:
  buyer_clarity: 2
  pain_evidence: 2
  persistence_quality: 1
  replicability: 1
  tractability: 2
  incumbent_gap: 1
  reachability: 2
  deal_economics: 1
human_verdict: null
cost_usd: null
source_count: 4
revenue_ceiling_usd: 42000.0
composite: 50
gate_pass: false
scored_profile: balanced
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

## Evaluation & Scrutiny Log

### Evidence verification

Two independent practitioner sources support the workflow. One asks for a generator after using Excel and Word for stepwise commissioning plans and describes repetitive boilerplate that takes days; the other describes a client-specified FAT document with input, expected-output, and initials boxes on every line, plus an Excel object list for I/O, alarm, HMI/SCADA, and communications checks. https://www.reddit.com/r/PLC/comments/11e66fk/commissioning_automation/ and https://www.reddit.com/r/PLC/comments/12v6jtk/functional_testing_of_plc_code/

The current job posting independently confirms that automation engineers own I/O lists, test documentation, FAT, SAT, and commissioning work. The municipal packet did not render in the research tool and was not needed to establish the pain score. https://builtin.com/job/senior-rockwell-plc-automation-engineer/9906964 and https://www.clackamasriverwater.gov/files/932cfc921/CRW%2BReg%2BBoard%2BMtng%2BPacket%2B10.09.2025.pdf

### Competition

This job is already partly productized. Bluerithm manages industrial checksheets, testing, evidence, reporting, and turnover documents and reports more than 30,000 users. Kalman FAT Suite manages phased FAT/SAT test items and participant decisions, while T-IA Connect directly generates TIA Portal project, FAT, SAT, and handover reports from live project data. The last is Siemens-specific, and none of these pages establishes reliable cross-vendor generation from arbitrary control narratives, but they materially narrow the incumbent gap. https://bluerithm.com/industrial-commissioning-software/ ; https://www.kalmancontrol.de/en/fat ; https://t-ia-connect.com/en/devops/reporting

Direct-competitor queries run: `PLC FAT SAT test management software generate test procedures evidence signoff industrial automation`; `commissioning management software FAT SAT test scripts signoff`; `PLC commissioning evidence software FAT SAT`; `industrial commissioning software public pricing per user per month`.

### Buyer and deal economics

The named buyer is the Director of Automation or Engineering Manager at a control-system integrator, a role that plausibly controls the engineering tools used to standardize FAT/SAT delivery. CSIA says it has hundreds of members, and an association white paper identifies more than 400 system-integrator members. The buyer count applies a low-confidence 25% size-and-frequency cut to that 400-member lower bound, yielding 100 firms with enough repeat commissioning work to buy. https://controlsys.org/about/ and https://controlsys.org/wp-content/uploads/2024/05/Certified_white_paper.pdf

The $420 annual price is anchored to one year of one TestRail Professional seat, an adjacent test-management system that includes test plans, runs, reports, CSV/XML import/export, and an API. This produces a $42,000 ceiling across 100 buyers; it is a conservative one-seat comparison, though it does not establish willingness to pay for PLC-specific parsing. https://www.testrail.com/pricing/

### Replicability and technical barrier

The input is technically reachable: Rockwell Studio 5000 exports tags and documentation as CSV/TSV and projects or components as L5X, while Siemens TIA Portal Openness exports PLC tag tables as XML. These are two separate vendor surfaces rather than one market-wide schema. https://www.rockwellautomation.com/en-us/docs/studio-5000-logix-designer/38-01/contents-ditamap/studio-5000-logix-designer/import-and-export.html and https://cache.industry.siemens.com/dl/files/802/109773802/att_1007204/v1/TIAPortalOpenness_en-US.pdf

Replicability is 1 because the cited practitioner says the client specified the exact FAT format, and the hypothesis also depends on customer templates and control narratives. Core document assembly can be shared, but each buyer still needs connector and template mapping work; customer two is cheaper only after another custom setup. https://www.reddit.com/r/PLC/comments/12v6jtk/functional_testing_of_plc_code/

### Persistence hypothesis — `regulatory-moat`

The paperwork persists because FAT/SAT evidence is a contractual acceptance record: customers prescribe the format, and named operators or inspectors must review and sign individual results. Software can prefill and track the record, but liability, customer-specific acceptance criteria, and human sign-off keep the final judgment manual rather than making this a technically unsolved generation problem.

### Decision

Demote. The reachable export surfaces support tractability 2, but the `regulatory-moat` persistence tag is not promotion-eligible and replicability 1 fails the hard floor because every buyer needs custom PLC and document-template mapping.
