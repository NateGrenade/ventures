# Niche batch closeout: 2026-09-15-codex-24

## Outcome

- Requested: 24 cells; host allowed three concurrent workers.
- Workers used gpt-5.6-sol with high reasoning initially and medium after the user changed the setting.
- Finished: five waves, 15 complete cells, 24 candidates.
- Interrupted wave 6: one partial toolroom cell with one additional verified candidate; two cells produced no saved research.
- Eight assigned cells were not completed by this run. The partial toolroom cell also needs follow-up.
- Total saved: 25 new sandbox candidates; no scoring or promotion; zero completed cells yielded no candidate.
- One worker-reported overlap merged as additional evidence; no duplicate file created.
- Cost unknown. Ledger defaults of zero do not represent measured free usage.

## Verification and generated state

- Ran `dedup.py --sweep`: zero near-duplicate pairs at 0.45, including the expanded corpus from the other session.
- Ran `verify_sources.py --unverified-only`: no pending unverified files. All workers had run per-slug live checks.
- Reverified changed production-record, organic-grain, SIU, and interrupted toolroom files online. No offline mode used.
- Three distinct URLs across three candidates remain flagged unreachable (details below). The SIU job-posting mirror passed earlier but failed at closeout.
- Ran `rollup_cells.py` and `build_index.py`: corpus has 43 ideas and 25 of 1,938 cells marked swept. The rollup counts partial and failed external records as sweeps, so this is ledger coverage rather than confirmed full research coverage.
- Evidence tiers and source counts come from tags, not independent validation of claims or source independence.

## Deduplication resolution

The proposed bindery job-ticket-to-system entry finding matched `chemical-batch-record-to-erp-rekey` at 0.50. Both describe copying paper production quantities, material usage, and run data into digital production systems. Three bindery sources were added to the older canonical file and its job line generalized; its original slug and cell were retained. Chemical and printing claims remain attributed to their own sources. The bindery worker ledger correctly records zero merges at the time it appended; this coordinator merge is recorded here.

## Source yield in this run

| Source type | Cell records with usable evidence |
|---|---|
| job-posting | 12 |
| practitioner | 11 |
| regulatory | 4 |
| procurement | 2 |
| study | 2 |
| vendor | 1 |

Job postings and practitioner accounts produced most findings. Regulatory and procurement artifacts supported specific reporting and matching tasks. No trade-press evidence was recorded by this run. These are bounded search observations, not a basis for changing frontier policy.

## New candidates and jobs

### [dispatch-order-transmission-audit](../../ideas/dispatch-order-transmission-audit.md)

Cell: `onet-43-5032.00`

Dispatch operations staff manually search thousands of Excel order codes one at a time in custom dispatch software and color-code the spreadsheet with the result, because staff do not know of a batch-search or export function in the custom application.

### [freight-load-timestamp-pod-log-reconciliation](../../ideas/freight-load-timestamp-pod-log-reconciliation.md)

Cell: `onet-43-5032.00`

Freight operations support clerks manually copy scheduled-versus-actual times and BOL and POD documents from multiple TMS and internal dispatch systems into OTP tracking sheets and detention logs, because the employer maintains audit and carrier-billing records across those separate systems.

### [apparel-retailer-chargeback-evidence-reconciliation](../../ideas/apparel-retailer-chargeback-evidence-reconciliation.md)

Cell: `naics-414110`

Apparel-wholesale compliance specialists manually reconcile retailer deductions against POs, ASNs, invoices, bills of lading, and shipment records across EDI platforms, retailer portals, and Excel trackers, because dispute evidence and status are split across those systems.

### [clothing-wholesale-po-cross-system-processing](../../ideas/clothing-wholesale-po-cross-system-processing.md)

Cell: `naics-414110`

Clothing-wholesale EDI clerks manually transfer and validate retailer purchase orders between SPS or EDI feeds, SAP or other ERP systems, warehouse systems, and Excel trackers, because each channel requires separate order, ASN, invoice, and exception handling.

### [grain-scale-ticket-to-settlement-reconciliation](../../ideas/grain-scale-ticket-to-settlement-reconciliation.md)

Cell: `naics-493130`

grain accounting clerks manually enter and apply scale tickets and grain contracts to producer settlements between scale records and accounting software, because current cooperative workflows still assign clerks to enter, balance, reconcile, and correct those transactions.

### [grain-warehouse-monthly-regulatory-report-compilation](../../ideas/grain-warehouse-monthly-regulatory-report-compilation.md)

Cell: `naics-493130`

licensed grain warehouse office staff manually compile stock, receipt, liability, and capacity totals between internal position records and government reporting forms, because state portals and federal questionnaires require operator-submitted figures.

### [organic-grain-lot-folder-inventory-reconciliation](../../ideas/organic-grain-lot-folder-inventory-reconciliation.md)

Cell: `naics-493130`

organic grain warehouse administrators manually match scale and shipping records between paper lot folders and electronic inventory balances, because each lot's traceability trail spans operational documents, physical files, and system records.

### [chemical-batch-record-to-erp-rekey](../../ideas/chemical-batch-record-to-erp-rekey.md)

Cell: `onet-51-8091.00`

Production operators manually copy material usage, quantities, and run data from paper batch sheets or job tickets into ERP and shop-floor systems, because paper production records and digital transaction records are maintained separately.

### [automation-vendor-points-list-consolidation](../../ideas/automation-vendor-points-list-consolidation.md)

Cell: `onet-17-2199.05`

Automation package managers manually consolidate vendor points lists, network addresses, alarm lists, and interface details between supplier submissions and a master Excel workbook, because supplier submissions arrive as separate files with inconsistent formats and missing project details.

### [plc-commissioning-test-evidence-compilation](../../ideas/plc-commissioning-test-evidence-compilation.md)

Cell: `onet-17-2199.05`

Controls engineers manually translate I/O lists and PLC/HMI behavior into stepwise test scripts and signed FAT/SAT records between engineering project files and customer handover documents, because the tables and acceptance evidence are maintained in separate office documents.

### [literary-submission-rule-status-reconciliation](../../ideas/literary-submission-rule-status-reconciliation.md)

Cell: `onet-27-3043.05`

poets and other short-form creative writers manually reconcile each market's submission rules and open windows with manuscript versions and statuses spread across spreadsheets, email, and submission portals, because writers maintain submission fields and updates that their chosen trackers do not consolidate

### [scanned-technical-pdf-to-editable-word-reconstruction](../../ideas/scanned-technical-pdf-to-editable-word-reconstruction.md)

Cell: `onet-43-9022.00`

Document conversion contractors manually reconstruct text, formulas, tables, and layout from scanned PDFs in Microsoft Word, because OCR output does not preserve complex document structure reliably.

### [foundry-heat-traceability-record-reconciliation](../../ideas/foundry-heat-traceability-record-reconciliation.md)

Cell: `onet-51-4051.00`

Furnace operators manually reconcile alloy and heat-number paperwork, spectrograph results, molds, material weights, temperatures, and production records between shop-floor documents and tracking systems, because heat traceability evidence is split across separate artifacts.

### [performing-arts-venue-box-office-settlement-reconciliation](../../ideas/performing-arts-venue-box-office-settlement-reconciliation.md)

Cell: `naics-711311`

performing arts venue box office managers manually reconcile ticketing-system reports with cash and card records and artist deal terms into finance and performer settlement reports, because the ticketing system does not contain every payment adjustment and contractual settlement rule

### [performing-arts-venue-technical-rider-reconciliation](../../ideas/performing-arts-venue-technical-rider-reconciliation.md)

Cell: `naics-711311`

performing arts venue production managers manually reconcile incoming artist technical riders with house specifications, current equipment, crew availability, and rental needs, because static rider documents can be outdated and do not reflect the facility's current capabilities

### [brownfield-parcel-inventory-cross-database-reconciliation](../../ideas/brownfield-parcel-inventory-cross-database-reconciliation.md)

Cell: `onet-11-9199.11`

Brownfield inventory consultants manually match parcel records to environmental and historical records across assessor, GIS, state, and federal databases and compile the results in Excel and ACRES, because the source systems require address or coordinate matching and separate updates.

### [carrier-siu-claim-investigation-multisystem-documentation](../../ideas/carrier-siu-claim-investigation-multisystem-documentation.md)

Cell: `naics-524121`

Carrier special-investigation investigators manually summarize fraud-investigation documents and enter findings between evidence sources, claim notes, and multiple SIU systems, because investigation evidence and claim records are maintained separately.

### [commercial-underwriting-transaction-cross-system-entry](../../ideas/commercial-underwriting-transaction-cross-system-entry.md)

Cell: `naics-524121`

Carrier underwriting assistants manually code and enter premiums, policies, endorsements, renewals, and inspections across multiple policy systems, because the documented carrier workflow requires separate transaction entries across those applications.

### [pc-policy-conversion-manual-rekey](../../ideas/pc-policy-conversion-manual-rekey.md)

Cell: `naics-524121`

Carrier policy-conversion representatives manually rekey property and casualty policy records between legacy and target administration systems during acquisitions, because the acquisition workflow assigns record transfer and scenario resolution to manual conversion staff.

### [taxi-driver-dispatch-tax-ledger-reconciliation](../../ideas/taxi-driver-dispatch-tax-ledger-reconciliation.md)

Cell: `onet-53-3054.00`

self-employed taxi drivers manually reconcile dispatch statements, card-terminal totals, cash fares, tips, commissions, and vehicle rent into bookkeeping software, because dispatch and payment records classify or omit parts of the driver's actual income and expenses

### [church-gift-record-cross-system-reconciliation](../../ideas/church-gift-record-cross-system-reconciliation.md)

Cell: `naics-813110`

Church accounting staff manually reconcile donation records among giving platforms, member or donor databases, and the accounting ledger, because each system holds a separate version of the gift data.

### [drywall-takeoff-revision-change-order-reconciliation](../../ideas/drywall-takeoff-revision-change-order-reconciliation.md)

Cell: `naics-238310`

Drywall estimators manually transfer and reconcile quantities between plan takeoff tools, custom spreadsheets, and change-order forms, because assemblies, revisions, and unit conversions do not remain linked across the tools.

### [insulation-rebate-documentation-assembly](../../ideas/insulation-rebate-documentation-assembly.md)

Cell: `naics-238310`

Insulation contractor office staff manually assemble measurements, photos, invoices, product details, signatures, and application fields between job folders and utility rebate submissions, because each program requires a different evidence package.

### [print-finishing-route-queue-reconciliation](../../ideas/print-finishing-route-queue-reconciliation.md)

Cell: `onet-51-5113.00`

bindery leads and small print-shop production managers manually reconcile finishing routes, partial quantities, outsourced steps, rush changes, and due dates across job dockets, physical scheduling boards, and side spreadsheets, because each job's actual floor sequence changes after the static job ticket is issued

### [toolroom-repair-job-handoff-tracking](../../ideas/toolroom-repair-job-handoff-tracking.md)

Cell: `onet-51-4111.00`

Toolroom supervisors manually track mold and die repair jobs, drawings, and completion status across toolmakers, stations, paper travelers, and work-order records, because the shop lacks usable live handoff capture.

## Unreachable citations

- `carrier-siu-claim-investigation-multisystem-documentation`: https://www.theladders.com/job/field-siu-investigation-property-casualty-allstate-insurance-company-odenton-md_87539587
- `grain-scale-ticket-to-settlement-reconciliation`: https://www.indeed.com/viewjob?jk=d985a1f3014a3487
- `organic-grain-lot-folder-inventory-reconciliation`: https://tallo.com/talent/job/business/scheduler-or-operations-coordinator/tx/muleshoe/front-desk-scaleadmin-2679424c

Organic-grain operational details were read through the browser, but its Tallo URL fails the repository verifier. The associated regulations substantiate record obligations, not the employer workflow. The SIU operational claim rests on the now-unreachable job posting; the NAIC material is broader system context. Neither should be treated as independently corroborated current operational evidence.

## Remaining assignments

Partial: `onet-51-4111.00` (toolroom handoff candidate saved).

- `naics-526981`
- `naics-325520`
- `onet-25-1124.00`
- `onet-11-9031.00`
- `naics-531120`
- `naics-561730`
- `onet-29-1124.00`
- `naics-322219`

## Shared-checkout provenance

The earlier coordinator had stopped at a usage limit before selection. Its six recorded sweeps were rolled up before this run selected its 24 cells. During the later session interval, that coordinator resumed, overlapped assignments, and committed its own 17 files as `094ac88`. This closeout preserves those files and all ledger records, then regenerates shared state across both runs. These external records are excluded from this run's completion and candidate counts. The shared selector does not reserve cells; do not resume against the saved list without checking current coverage.

Pre-existing script and Claude configuration edits are left outside this research commit. The existing untracked `scripts/rollup_cells.py` was used for generation and remains outside the commit.
