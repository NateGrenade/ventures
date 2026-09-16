---
slug: foundry-heat-traceability-record-reconciliation
status: demoted
cell_id: onet-51-4051.00
created: 2026-09-15
owner_agent: 2026-09-15-codex-24-sweep-08
job: Furnace operators manually reconcile alloy and heat-number paperwork, spectrograph
  results, molds, material weights, temperatures, and production records between shop-floor
  documents and tracking systems, because heat traceability evidence is split across
  separate artifacts.
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 4
---

# Foundry Heat Traceability Record Reconciliation

## Problem statement

Metal-melting furnace operators maintain the information trail for each heat while also tending the physical process. Current postings require them to match molds and documentation to the correct alloy and paperwork, verify alloy and heat numbers against spectrograph results, track metal inventory, record lot weights and hourly temperatures, maintain logs, and enter production data into tracking systems.

## Evidence

- [type: job-posting] (2026-09) A current foundry melt-operator posting requires matching documentation and molds to alloy and paperwork, checking spectrograph results against alloy heat numbers, maintaining metal inventory, using an online computer system, and completing detailed recordkeeping. https://pcctalentacquisitionportal.tal.net/vx/mobile-1/appcentre-ext/brand-7/candidate/so/pm/1/pl/3/opp/20177-Foundry-Operator-2nd-Shift/en-GB
- [type: job-posting] (2026-08) A current furnace-operator listing requires manual recording of tapping temperatures and times, tap numbers, metal and slag weights, flow rates, and cooling-water temperatures for process control and monitoring. https://www.ziprecruiter.com/Jobs/Blast-Furnace
- [type: practitioner] (2026-03-03) Machining practitioners explain that a heat number must be cross-referenced with supplier certificates and test reports, that material certificates travel with shop travelers, and that mixing heat lots can put an entire order into material review. https://www.reddit.com/r/Machinists/comments/1rjsrcr/how_to_read_heat_treat_numbers/
- [type: study] (2024-01) A steel-plant dataset study reports that blast-furnace production data is stored through online readings, manual entry, and manual correction after online collection. https://www.jstage.jst.go.jp/article/isijinternational/64/1/64_ISIJINT-2023-257/_html/-char/en

## Automation hypothesis

SPECULATIVE. A heat-record layer could combine production schedules, scale readings, furnace temperature data, spectrograph results, and operator confirmations under one heat number, then flag mismatches before material moves downstream. It would need dependable interfaces to the plant's tracking and laboratory systems plus usable offline or rugged shop-floor capture where direct instrumentation is unavailable.

## Evaluation & Scrutiny Log

Triage demotion: this is already a mature foundry ERP/MES category with at least three established direct vendors—B&L Odyssey has served metalcasters since 1976 and provides heat/lot tracking plus direct spectrometer import (https://www.blinfo.com/solutions/quality/heat-analysis-and-lot-tracking/; https://www.blinfo.com/about/newsroom/press-releases/odyssey-62-released/), Guardian says it has supplied foundry-specific ERP/MES for more than 30 years and its MES captures shop-floor data into serialization and traceability records (https://www.guardiansoft.com/a-foundry-specific-erp-mes-solution-is-key-for-metal-casting-success/), and Synchro reports a 50-year history while offering batch/melt traceability, spectrometer integration, and certification generation (https://synchroerp.com/; https://www.synchroerp.com/tour/quality-assurance-detail).
