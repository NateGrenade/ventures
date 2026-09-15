---
slug: clothing-wholesale-po-cross-system-processing
status: sandbox
cell_id: naics-414110
created: 2026-09-15
owner_agent: 2026-09-15-codex-24-sweep-02
job: Clothing-wholesale EDI clerks manually transfer and validate retailer purchase
  orders between SPS or EDI feeds, SAP or other ERP systems, warehouse systems, and
  Excel trackers, because each channel requires separate order, ASN, invoice, and
  exception handling.
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 2
---

# Clothing-Wholesale Purchase Order Cross-System Processing

## Problem statement

Clothing and apparel distributors employ operations and EDI clerks to process retailer purchase orders across EDI services, ERP records, warehouse requests, invoices, and spreadsheets. A current Lanctôt posting assigns one clerk to process new POs in SAP and SPS, troubleshoot warehouse ASN requests, transfer EDI shipment documents, and verify and export customer invoices; a current Moose Knuckles posting separately assigns a wholesale coordinator to maintain open-order reports while working with order entry, logistics tracking, Excel, NuORDER, ERP systems, and Skypad. https://ca.linkedin.com/jobs/view/commis-edi-edi-clerk-at-lanct%C3%B4t-sports-4454268786 https://www.linkedin.com/jobs/view/wholesale-coordinator-at-moose-knuckles-canada-4456904583

## Evidence

- [type: job-posting] (2026-09) Lanctôt, a Canadian distributor of apparel and other sporting brands, is recruiting an EDI clerk to process customer POs in both SAP and SPS, handle ASN requests from two warehouses, transfer EDI shipment data, and verify and export invoices daily. https://ca.linkedin.com/jobs/view/commis-edi-edi-clerk-at-lanct%C3%B4t-sports-4454268786
- [type: job-posting] (2026-09) Moose Knuckles Canada is recruiting a wholesale coordinator to maintain open-order reports, assist with order entry and logistics tracking, and prepare weekly reporting; the role asks for advanced Excel plus familiarity with NuORDER, ERP systems, and Skypad. https://www.linkedin.com/jobs/view/wholesale-coordinator-at-moose-knuckles-canada-4456904583

## Automation hypothesis

SPECULATIVE. A workflow service could normalize retailer EDI and manually received PO data into draft ERP orders, validate item and quantity fields, synchronize ASN and invoice status with warehouse events, and update the open-order tracker from the same record. This is tractable only where the wholesaler can expose stable exports or APIs from its EDI service, ERP, and warehouse system; account-specific retailer mappings and exception review would remain essential.
