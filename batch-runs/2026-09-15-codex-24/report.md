# Niche batch closeout: 2026-09-15-codex-24

## Outcome

- Completed all 24 assigned cells using three concurrent workers per wave.
- Saved 33 sandbox candidates. One cell (`naics-322219`) yielded no candidate.
- Cost is unknown. Ledger numeric-zero values are CLI defaults, not measured free research.
- No candidate was scored or promoted.

## Deterministic passes

- `dedup.py --sweep`: zero corpus pairs at the 0.45 threshold after coordinator resolutions.
- Every new or changed candidate received an online source check; offline mode was not used.
- `rollup_cells.py` and `build_index.py`: 51 ideas total; 30 of 1,938 frontier cells have ledger coverage.
- Source counts and tiers reflect tags and URL resolution. They do not prove source independence or every claim.

## Coordinator resolutions

- Merged the bindery paper-ticket evidence into `chemical-batch-record-to-erp-rekey`; no second file was created.
- Reworked `corrugated-die-room-tooling-coordinator-rekey` around two direct Pratt postings and removed unsupported multi-employer and full-rekey claims.
- Narrowed `foreign-language-study-abroad-syllabus-equivalency-review` to document collection and approval-record handoff, with UVA DocuSign counterevidence.
- Replaced failed SIU and grain-accounting mirrors with direct employer pages.

## Source yield

| Source type | Sweep records with usable evidence |
|---|---|
| job-posting | 17 |
| practitioner | 15 |
| regulatory | 7 |
| procurement | 3 |
| institutional | 3 |
| study | 2 |
| vendor | 2 |
| trade-press | 1 |

Job postings and practitioner artifacts produced most findings. Regulatory and institutional procedures were useful for reporting and education/healthcare handoffs. These counts include continuation records and should not drive a frontier-policy change by themselves.

## Candidates

- [`dispatch-order-transmission-audit`](../../ideas/dispatch-order-transmission-audit.md) — Dispatch operations staff manually search thousands of Excel order codes one at a time in custom dispatch software and color-code the spreadsheet with the result, because staff do not know of a batch-search or export function in the custom application.
- [`freight-load-timestamp-pod-log-reconciliation`](../../ideas/freight-load-timestamp-pod-log-reconciliation.md) — Freight operations support clerks manually copy scheduled-versus-actual times and BOL and POD documents from multiple TMS and internal dispatch systems into OTP tracking sheets and detention logs, because the employer maintains audit and carrier-billing records across those separate systems.
- [`apparel-retailer-chargeback-evidence-reconciliation`](../../ideas/apparel-retailer-chargeback-evidence-reconciliation.md) — Apparel-wholesale compliance specialists manually reconcile retailer deductions against POs, ASNs, invoices, bills of lading, and shipment records across EDI platforms, retailer portals, and Excel trackers, because dispute evidence and status are split across those systems.
- [`clothing-wholesale-po-cross-system-processing`](../../ideas/clothing-wholesale-po-cross-system-processing.md) — Clothing-wholesale EDI clerks manually transfer and validate retailer purchase orders between SPS or EDI feeds, SAP or other ERP systems, warehouse systems, and Excel trackers, because each channel requires separate order, ASN, invoice, and exception handling.
- [`grain-scale-ticket-to-settlement-reconciliation`](../../ideas/grain-scale-ticket-to-settlement-reconciliation.md) — grain accounting clerks manually enter and apply scale tickets and grain contracts to producer settlements between scale records and accounting software, because current cooperative workflows still assign clerks to enter, balance, reconcile, and correct those transactions.
- [`grain-warehouse-monthly-regulatory-report-compilation`](../../ideas/grain-warehouse-monthly-regulatory-report-compilation.md) — licensed grain warehouse office staff manually compile stock, receipt, liability, and capacity totals between internal position records and government reporting forms, because state portals and federal questionnaires require operator-submitted figures.
- [`organic-grain-lot-folder-inventory-reconciliation`](../../ideas/organic-grain-lot-folder-inventory-reconciliation.md) — organic grain warehouse administrators manually match scale and shipping records between paper lot folders and electronic inventory balances, because each lot's traceability trail spans operational documents, physical files, and system records.
- [`chemical-batch-record-to-erp-rekey`](../../ideas/chemical-batch-record-to-erp-rekey.md) — Production operators manually copy material usage, quantities, and run data from paper batch sheets or job tickets into ERP and shop-floor systems, because paper production records and digital transaction records are maintained separately.
- [`automation-vendor-points-list-consolidation`](../../ideas/automation-vendor-points-list-consolidation.md) — Automation package managers manually consolidate vendor points lists, network addresses, alarm lists, and interface details between supplier submissions and a master Excel workbook, because supplier submissions arrive as separate files with inconsistent formats and missing project details.
- [`plc-commissioning-test-evidence-compilation`](../../ideas/plc-commissioning-test-evidence-compilation.md) — Controls engineers manually translate I/O lists and PLC/HMI behavior into stepwise test scripts and signed FAT/SAT records between engineering project files and customer handover documents, because the tables and acceptance evidence are maintained in separate office documents.
- [`literary-submission-rule-status-reconciliation`](../../ideas/literary-submission-rule-status-reconciliation.md) — poets and other short-form creative writers manually reconcile each market's submission rules and open windows with manuscript versions and statuses spread across spreadsheets, email, and submission portals, because writers maintain submission fields and updates that their chosen trackers do not consolidate
- [`scanned-technical-pdf-to-editable-word-reconstruction`](../../ideas/scanned-technical-pdf-to-editable-word-reconstruction.md) — Document conversion contractors manually reconstruct text, formulas, tables, and layout from scanned PDFs in Microsoft Word, because OCR output does not preserve complex document structure reliably.
- [`foundry-heat-traceability-record-reconciliation`](../../ideas/foundry-heat-traceability-record-reconciliation.md) — Furnace operators manually reconcile alloy and heat-number paperwork, spectrograph results, molds, material weights, temperatures, and production records between shop-floor documents and tracking systems, because heat traceability evidence is split across separate artifacts.
- [`performing-arts-venue-box-office-settlement-reconciliation`](../../ideas/performing-arts-venue-box-office-settlement-reconciliation.md) — performing arts venue box office managers manually reconcile ticketing-system reports with cash and card records and artist deal terms into finance and performer settlement reports, because the ticketing system does not contain every payment adjustment and contractual settlement rule
- [`performing-arts-venue-technical-rider-reconciliation`](../../ideas/performing-arts-venue-technical-rider-reconciliation.md) — performing arts venue production managers manually reconcile incoming artist technical riders with house specifications, current equipment, crew availability, and rental needs, because static rider documents can be outdated and do not reflect the facility's current capabilities
- [`brownfield-parcel-inventory-cross-database-reconciliation`](../../ideas/brownfield-parcel-inventory-cross-database-reconciliation.md) — Brownfield inventory consultants manually match parcel records to environmental and historical records across assessor, GIS, state, and federal databases and compile the results in Excel and ACRES, because the source systems require address or coordinate matching and separate updates.
- [`carrier-siu-claim-investigation-multisystem-documentation`](../../ideas/carrier-siu-claim-investigation-multisystem-documentation.md) — Carrier special-investigation investigators manually summarize fraud-investigation documents and enter findings between evidence sources, claim notes, and multiple SIU systems, because investigation evidence and claim records are maintained separately.
- [`commercial-underwriting-transaction-cross-system-entry`](../../ideas/commercial-underwriting-transaction-cross-system-entry.md) — Carrier underwriting assistants manually code and enter premiums, policies, endorsements, renewals, and inspections across multiple policy systems, because the documented carrier workflow requires separate transaction entries across those applications.
- [`pc-policy-conversion-manual-rekey`](../../ideas/pc-policy-conversion-manual-rekey.md) — Carrier policy-conversion representatives manually rekey property and casualty policy records between legacy and target administration systems during acquisitions, because the acquisition workflow assigns record transfer and scenario resolution to manual conversion staff.
- [`taxi-driver-dispatch-tax-ledger-reconciliation`](../../ideas/taxi-driver-dispatch-tax-ledger-reconciliation.md) — self-employed taxi drivers manually reconcile dispatch statements, card-terminal totals, cash fares, tips, commissions, and vehicle rent into bookkeeping software, because dispatch and payment records classify or omit parts of the driver's actual income and expenses
- [`church-gift-record-cross-system-reconciliation`](../../ideas/church-gift-record-cross-system-reconciliation.md) — Church accounting staff manually reconcile donation records among giving platforms, member or donor databases, and the accounting ledger, because each system holds a separate version of the gift data.
- [`drywall-takeoff-revision-change-order-reconciliation`](../../ideas/drywall-takeoff-revision-change-order-reconciliation.md) — Drywall estimators manually transfer and reconcile quantities between plan takeoff tools, custom spreadsheets, and change-order forms, because assemblies, revisions, and unit conversions do not remain linked across the tools.
- [`insulation-rebate-documentation-assembly`](../../ideas/insulation-rebate-documentation-assembly.md) — Insulation contractor office staff manually assemble measurements, photos, invoices, product details, signatures, and application fields between job folders and utility rebate submissions, because each program requires a different evidence package.
- [`print-finishing-route-queue-reconciliation`](../../ideas/print-finishing-route-queue-reconciliation.md) — bindery leads and small print-shop production managers manually reconcile finishing routes, partial quantities, outsourced steps, rush changes, and due dates across job dockets, physical scheduling boards, and side spreadsheets, because each job's actual floor sequence changes after the static job ticket is issued
- [`toolroom-repair-job-handoff-tracking`](../../ideas/toolroom-repair-job-handoff-tracking.md) — Toolroom supervisors manually track mold and die repair jobs, drawings, and completion status across toolmakers, stations, paper travelers, and work-order records, because the shop lacks usable live handoff capture.
- [`securitization-abs-ee-filing-assembly`](../../ideas/securitization-abs-ee-filing-assembly.md) — Securitization compliance analysts manually transform and verify monthly asset-level data from accounting files into Form 10-D and Form ABS-EE packages for EDGAR, because servicing and accounting systems do not produce complete SEC-formatted disclosures.
- [`adhesive-customer-compliance-request-packet-assembly`](../../ideas/adhesive-customer-compliance-request-packet-assembly.md) — Product-stewardship staff at adhesive manufacturers manually coordinate customer regulatory-document requests across commercial teams, technical contributors, SharePoint or Excel records, and customer submission systems, because closing a request requires gathering product and supplier information from separate contributors and records.
- [`language-placement-score-transfer-into-banner`](../../ideas/language-placement-score-transfer-into-banner.md) — Language-program advising staff manually copy language placement results from WebCAPE into Banner SOATEST because the documented workflow requires staff recording before student records can use the assessment outcome.
- [`childcare-ccfa-parent-fee-reconciliation`](../../ideas/childcare-ccfa-parent-fee-reconciliation.md) — Childcare program administrative staff manually reconcile parent fee assessments between Massachusetts CCFA and Procare or their current child care management system, because their documented workflow requires separate fee-entry audits and cross-system checks.
- [`commercial-landlord-cam-lease-rule-reconciliation`](../../ideas/commercial-landlord-cam-lease-rule-reconciliation.md) — Commercial landlord accountants manually reconcile lease-specific expense pools between lease documents, Excel schedules and MRI because their existing setup lacks configured CAM calculations.
- [`landscape-bid-invitation-schedule-intake`](../../ideas/landscape-bid-invitation-schedule-intake.md) — Landscape estimators manually copy bid invitations from email, VBX and Procore into an Excel bid schedule because their documented intake workflow maintains the schedule separately from invitation platforms and ProEst.
- [`landscape-pesticide-monthly-report-compilation`](../../ideas/landscape-pesticide-monthly-report-compilation.md) — Landscape contractor report preparers manually total application records into monthly county pesticide-use forms because the documented form route requires product-level totals and county-specific reports separate from individual applications.
- [`radiation-therapy-charge-review-before-ehr-export`](../../ideas/radiation-therapy-charge-review-before-ehr-export.md) — Radiation therapists manually review and correct treatment charge records between ARIA or MOSAIQ and the hospital EHR export queue, because automated charge interfaces retain a human accuracy check before billing release.

## Verification limitations

- `corrugated-die-room-tooling-coordinator-rekey`: https://careers.prattindustries.com/en/jobs/30-23768/tooling-coordinator-1st-shift/
- `organic-grain-lot-folder-inventory-reconciliation`: https://tallo.com/talent/job/business/scheduler-or-operations-coordinator/tx/muleshoe/front-desk-scaleadmin-2679424c
- `radiation-therapy-charge-review-before-ehr-export`: https://www.uwhealth.org/files-directory/position-descriptions/technologists-technicians/radiation.therapist.clin.doc.spec.500037.pdf
- `securitization-abs-ee-filing-assembly`: https://builtin.com/job/senior-compliance-analyst/3728954

The organic-grain posting and the other flagged job pages were readable through web search or browser retrieval when researched, but the repository verifier could not resolve their URLs. Each file identifies its date and limitation. The remaining reachable sources should be assessed claim by claim before promotion.

## Shared checkout

Another coordinator completed an overlapping batch and committed 17 ideas as `094ac88`. This run preserved those artifacts and excluded them from its 33-candidate count. Shared generated state covers both batches. Unrelated skill and script edits in the checkout remain outside this research batch.
