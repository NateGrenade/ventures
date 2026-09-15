---
slug: brownfield-parcel-inventory-cross-database-reconciliation
status: sandbox
cell_id: onet-11-9199.11
created: 2026-09-15
owner_agent: 2026-09-15-codex-24-sweep-10
job: Brownfield inventory consultants manually match parcel records to environmental
  and historical records across assessor, GIS, state, and federal databases and compile
  the results in Excel and ACRES, because the source systems require address or coordinate
  matching and separate updates.
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 3
---

# Brownfield Parcel Inventory Cross-Database Reconciliation

## Problem statement

Brownfield inventory consultants gather parcel, environmental, historical, and redevelopment data from multiple public sources and assemble a property-level inventory. The work includes matching environmental records to parcels by address or coordinates, producing an Excel inventory, and separately providing parcel and assessment updates for ACRES.

## Evidence

- [type: procurement] (2025-11) A Southeastern Connecticut Council of Governments brownfields RFP requires a qualified environmental professional to update municipal inventories, present gathered information in an Excel spreadsheet, and provide parcel, environmental-assessment, and contaminant updates to the council's ACRES database. https://secogct.gov/wp-content/uploads/CoalitionRFP_16HallsMillRd_Final.pdf
- [type: procurement] (2024-12) A Memphis brownfield GIS procurement allocated $36,000 for a consultant to use multiple identified and newly discovered data sources to create a brownfield inventory, web application, maps, and story maps. https://cramemphis.org/wp-content/uploads/2024/12/GIS-RFP-QA-12.20.24.pdf
- [type: study] (2018-05) An Anchorage brownfield inventory work plan describes building an Excel parcel database from municipal Excel and GIS data, collecting records from federal, state, local, and commercial environmental databases, and matching those records to parcels using addresses, coordinates, and other spatial data. https://www.muni.org/Departments/OCPD/Planning/Projects/SiteAssets/Pages/Brownfields/2017%20BrwnfieldCloseout.pdf

## Automation hypothesis

SPECULATIVE. A reconciliation layer could ingest assessor, GIS, environmental-registry, and historical-source exports; propose parcel matches with provenance and confidence scores; and produce synchronized Excel, GIS, and ACRES-ready update queues. This depends on access to stable source exports, reliable entity resolution for sites with changed addresses or parcel boundaries, and a review path for uncertain matches.
