---
slug: automation-vendor-points-list-consolidation
status: demoted
cell_id: onet-17-2199.05
created: 2026-09-15
owner_agent: 2026-09-15-codex-24-sweep-05
job: Automation package managers manually consolidate vendor points lists, network
  addresses, alarm lists, and interface details between supplier submissions and a
  master Excel workbook, because supplier submissions arrive as separate files with
  inconsistent formats and missing project details.
split_from: null
evidence_tier: 1
buyer_role: Director of Automation or Engineering Manager at a control-system integrator
buyer_count: null
annual_price_usd: null
persistence: genuinely-hard
scores:
  buyer_clarity: 2
  pain_evidence: 2
  persistence_quality: 3
  replicability: 2
  tractability: 2
  incumbent_gap: 1
  reachability: 2
  deal_economics: 0
human_verdict: null
cost_usd: null
source_count: 3
revenue_ceiling_usd: null
composite: 59
gate_pass: false
scored_profile: balanced
---

# Automation Vendor Points List Consolidation

## Problem statement

Automation package managers collect monitoring points and connection details from multiple equipment vendors and consolidate them into a project-wide workbook. One commissioning engineer reports poor supplier submissions and describes a master Excel file spanning IP addresses, network scans, topologies, firewall rules, I/O and alarm lists, interface lists, firmware versions, safety matrices, and test-report exports; they estimate manual compilation would take a month and be error-prone.

## Evidence

- [type: practitioner] (2024-10-20) A commissioning and systems engineer asks for a reusable vendor points-list template after receiving poor submissions, then describes a large project Excel workbook covering network, I/O, alarm, interface, firmware, safety, and test-report data; the practitioner says manual assembly would take a month and likely contain errors. https://www.reddit.com/r/PLC/comments/1g7ueov/template_for_vendors_points_list/
- [type: practitioner] (2023-09-06) A PLC programmer describes spending at least a week developing a spreadsheet of sensors, actuators, I/O layout, sequences, and interlocks before programming, and later updating its I/O layout after cell wiring. https://www.reddit.com/r/PLC/comments/16b1wet/programming_process/
- [type: job-posting] (2026-09) A current automation engineering posting requires preparation and review of I/O schedules, interface definitions, network architecture, commissioning documents, and handover packages while coordinating contractors, integrators, and client representatives. https://www.careers-page.com/logistics-executive-group/job/937XV7VY

## Automation hypothesis

SPECULATIVE. A vendor-submission intake layer could map spreadsheets and exported point lists into a canonical project schema, flag missing or conflicting fields, and regenerate the master workbook and downstream schedules. It would need project-specific mapping rules, approval controls, and a clear source-of-truth policy for conflicting vendor revisions.

## Evaluation & Scrutiny Log

### Evidence verification

The principal practitioner source supports the stated job: the package manager asks for a reusable multivendor point-list intake process, and a second practitioner in the thread describes a large project Excel workbook that depends on automated import/export tooling and would take about a month to compile manually. An independent building-automation thread also describes point and cable lists being created in Excel, controller data exported to CSV, and names copied into controller-specific sheets, while asking for a better tool. These are two independent practitioner accounts of the spreadsheet work at issue. https://www.reddit.com/r/PLC/comments/1g7ueov/template_for_vendors_points_list/ and https://www.reddit.com/r/BuildingAutomation/comments/1l33y86/is_there_anything_better_than_excel/

The existing `programming-process` source supports heavy spreadsheet planning in controls projects, but it does not substantiate multivendor submission consolidation, so it was not used to raise the pain score. The listed job page did not render in the research tool and was not relied on for scoring. https://www.reddit.com/r/PLC/comments/16b1wet/programming_process/ and https://www.careers-page.com/logistics-executive-group/job/937XV7VY

### Competition

PointCheck BMS is a direct beta competitor: it imports messy CSV/XLSX point lists, maps columns, and flags BACnet/data-quality problems, though it is read-only and does not cover the proposed full project-wide consolidation. Distech Xpressgfx Points and TRIC Global Edit/List are adjacent vendor or engineering-suite tools for creating and updating point/function lists and exporting spreadsheets. The remaining substitute is the current Excel workbook plus internal scripts. https://www.reddit.com/r/BuildingAutomation/comments/1w4x48l/built_a_bms_pointlist_qa_tool_between_working_on/ ; https://www.environmental-expert.com/software/distech-controls-version-xpressgfx-points-points-list-configuration-tool-906120 ; https://en.tric.de/global-edit-list

Direct-competitor queries run: `vendor points list consolidation software BACnet Modbus`; `BMS point list QA import Excel multiple vendors`; `data center commissioning software points list vendor submissions integration`; `site:reddit.com/r/BuildingAutomation point list Excel manual check BACnet vendors`.

### Buyer and deal economics

The named buyer is the Director of Automation or Engineering Manager at a control-system integrator: that role can standardize project delivery and plausibly owns a small engineering-tool budget. CSIA describes control-system integrators as firms that design and implement control systems and says the association has hundreds of members; a CSIA white paper gives a lower-bound registry of more than 400 system-integrator members. The buyer count uses 25% of that 400-member lower bound, or 100 firms, as the subset with enough recurring multivendor project volume to buy; confidence is low because the size cut is an explicit assumption rather than a registry field. https://controlsys.org/about/ and https://controlsys.org/wp-content/uploads/2024/05/Certified_white_paper.pdf

The annual price is $420 per buyer, anchored to one TestRail Professional seat for 12 months. TestRail is an adjacent paid test-management product with test plans, runs, reports, CSV/XML exchange, and an API; using a single-seat price is conservative for a manager-operated consolidation tool. At 100 buyers, the annual revenue ceiling is $42,000; the floor would still clear with 60 of the 400 registered firms. https://www.testrail.com/pricing/

### Replicability and technical barrier

The immediate surface is CSV/XLSX rather than a live controller connection. BACnet gives a shared semantic starting point across a meaningful share of the target building-automation market: BACnet International reports that 77% of projects globally specify BACnet. That supports replicability 2 for a BACnet-first product, although Modbus, discrete I/O, proprietary columns, and missing vendor fields would still require mapping rules. https://bacnetinternational.org/news/bacnet-protocol-expands-dominant-market-share-in-latest-market-research-report/

Spreadsheet ingestion and BACnet normalization are reachable by software, so tractability is 2. The hard part is resolving incomplete fields and project-specific naming without silently inventing engineering facts; the original practitioner explicitly says suppliers submit incomplete connection details, so the design needs review queues and source-of-truth controls. https://www.reddit.com/r/PLC/comments/1g7ueov/template_for_vendors_points_list/

### Persistence hypothesis — `genuinely-hard`

The inefficiency persists because a common protocol does not make vendor submissions semantically complete or consistent: point names, writable behavior, addressing, and required project fields still arrive in different spreadsheet layouts and with omissions. Normalizing that data while preserving provenance and refusing unsafe guesses is a technically hard reconciliation problem, even though CSV/XLSX and BACnet make a bounded first product feasible.

### Decision

Promoted. The deterministic scorer returned 64/100 with all gates passing. The opportunity has two independent practitioner sources, a plausible budget owner, a BACnet-backed replication surface, and a conservative revenue ceiling above the floor; the main uncertainty is the low-confidence 25% buyer-size cut.

### Confirmation pass (confirm-scrutiny-20260915T204319Z-automation)

Overturned. The two independent practitioner sources support the manual point-list work: the PLC thread describes incomplete multivendor submissions and a month of error-prone manual compilation, while the Building Automation thread describes Excel point/cable lists and a controller-export-to-CSV workflow. https://www.reddit.com/r/PLC/comments/1g7ueov/template_for_vendors_points_list/ and https://www.reddit.com/r/BuildingAutomation/comments/1l33y86/is_there_anything_better_than_excel/

The `genuinely-hard` tag and tractability 2 hold: inconsistent and incomplete vendor semantics require reconciliation, while CSV/XLSX provides a software-accessible intake surface. Replicability 2 also holds for the BACnet-first wedge because BACnet International reports that 77% of projects globally specify BACnet, although that does not cover Modbus or discrete-I/O submissions. https://bacnetinternational.org/news/bacnet-protocol-expands-dominant-market-share-in-latest-market-research-report/

The deal-economics derivation does not hold. CSIA does substantiate more than 400 system-integrator member companies, but no cited registry field or other evidence supports the 25% cut to 100 firms with sufficient recurring multivendor volume; the log itself labels that cut a low-confidence assumption. TestRail confirms a $420 annual Professional seat and adjacent CSV/API functionality, but nothing cited shows this buyer role already purchases TestRail or another comparable tool, so it does not meet the rubric's price-anchor requirement. `buyer_count` and `annual_price_usd` were therefore set to null. https://controlsys.org/wp-content/uploads/2024/05/Certified_white_paper.pdf and https://www.testrail.com/pricing/

Direct-competitor searches run: `vendor points list consolidation software automation Excel I/O schedule`; `building automation point list software Excel import vendor submissions`. Distech's Xpressgfx Points officially creates and updates point lists, imports and exports Excel data, and supports submittal through commissioning; Johnson Controls supports configured-point Excel import and submittal-data export; Hexagon Smart Completions consolidates asset information and Control System I/O points. These findings support keeping `incumbent_gap` at 1 rather than increasing it. https://www.distech-controls.com/products/detail/947824/distech-controls/xpressgfx-points ; https://docs.johnsoncontrols.com/bas/r/BCPro/en-US/BCPro-User-Interface/4.0/Setup-module/Network-Tree/Importing-updated-points ; https://aliresources.hexagon.com/procurement-fabrication-construction/save-time-and-money-with-early-commissioning-plans

## Falsification Log

### Riskiest assumption

Control-system integrators do not already have an adequate point-list or commissioning tool in their stack, so a lightweight vendor-submission normalization layer would displace manual Excel work rather than duplicate an incumbent feature.

### Test: incumbent feature audit

- Assumption targeted: no adequate solution already sits in the buyer's stack.
- Queries run: `automation vendor points list consolidation software Excel I/O schedule import vendor submissions`; `controls engineering software point list management vendor submittal Excel import`; `building automation point list QA software CSV XLSX vendor submissions`; `industrial automation commissioning software I/O list management vendor data`.
- Result: **FAILS / strong disconfirmation.** Distech's official Xpressgfx Points is an Excel add-in for creating and updating points lists, importing and exporting Excel data, and supporting submittal through commissioning (https://www.distech-controls.com/products/detail/947824/distech-controls/xpressgfx-points). Johnson Controls documents submittal data reports, point mapping checks, and Excel export in Metasys (https://docs.johnsoncontrols.com/bas/r/Johnson-Controls/en-US/Metasys-Enterprise-Management-Professional-Productivity-Tool-PPT-Guide/1.3.1/Initial-Assessment-Phase/Generating-a-Submittal-Data-Report). Hexagon describes Smart Completions as consolidating vendor, equipment, and I/O data and verifying commissioning performance (https://aliresources.hexagon.com/procurement-fabrication-construction/save-time-and-money-with-early-commissioning-plans).
- Verdict on assumption: **DOES NOT SURVIVE.** The product may still have a narrow wedge around cross-vendor intake and provenance, but the promotion's incumbent-gap score is not credible without showing why these existing tools fail for the exact buyer and workflow.

### Human test queued

The incumbent audit is strong enough to require practitioner confirmation before validation. See `worklist.md` for five control-system integrator contacts and the pre-registered falsifying answer.
