---
slug: brownfield-parcel-inventory-cross-database-reconciliation
status: demoted
cell_id: onet-11-9199.11
created: 2026-09-15
owner_agent: 2026-09-15-codex-24-sweep-10
job: Brownfield inventory consultants manually match parcel records to environmental
  and historical records across assessor, GIS, state, and federal databases and compile
  the results in Excel and ACRES, because the source systems require address or coordinate
  matching and separate updates.
split_from: null
evidence_tier: 1
buyer_role: municipal brownfields program manager
buyer_count: 75
annual_price_usd: 6000
persistence: genuinely-hard
scores:
  buyer_clarity: 1
  pain_evidence: 3
  persistence_quality: 3
  replicability: 1
  tractability: 2
  incumbent_gap: 2
  reachability: 2
  deal_economics: 2
human_verdict: null
cost_usd: null
source_count: 3
revenue_ceiling_usd: 450000.0
composite: 67
gate_pass: false
scored_profile: balanced
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

## Evaluation & Scrutiny Log

### Competition

Queries run: `brownfield inventory GIS software parcel environmental database reconciliation ACRES`; `brownfields inventory management software GIS consultant parcel matching`; `brownfield redevelopment software environmental data parcel inventory platform`; `ACRES brownfields software integration consultant data entry`.

Brownfield.ai is an adjacent incumbent bordering on direct: it targets government brownfield owners, combines federal, state, county, and private records into shared property profiles, and offers a portfolio knowledge base. Its public Organization plan is $500/month, but its public materials do not claim municipal inventory reconciliation or ACRES submission. https://www.brownfield.ai/owners-governments/ https://www.brownfield.ai/pricing/

EPA's public ACRES/CIMC data and ArcGIS layer are adjacent read-side tools. The actual substitute is the qualified-environmental-professional contract plus Excel and ArcGIS: Memphis had four environmental firms under contract and separately procured $36,000 of GIS services for an inventory, web application, and maps. https://cramemphis.org/wp-content/uploads/2024/12/GIS-RFP-QA-12.20.24.pdf

### Buyer

The buyer is the municipal brownfields program manager administering the assessment grant. The role is identifiable, but budget authority is uncertain: SECOG's Environmental Planner ran the procurement while the QEP contractor supplies inventory and ACRES data as one part of a broader four-year environmental-services engagement. That supports `buyer_clarity: 1`, not a confirmed tool budget. https://secogct.gov/wp-content/uploads/CoalitionRFP_16HallsMillRd_Final.pdf

### Deal economics

`buyer_count: 75` uses EPA's FY2026 plan for approximately 75 assessment cooperative agreements whose recipients may inventory brownfield sites. This deliberately counts only one annual cohort, rather than multiplying by grant duration; confidence is medium because it is an official program estimate rather than a current-recipient census. EPA's FY2025 award list provides a named, reachable roster and confirms the buyer population is made up of cities, councils of government, redevelopment authorities, and similar organizations. https://www.epa.gov/system/files/documents/2025-06/fy-2026-epa-congressional-justification.pdf https://www.epa.gov/system/files/documents/2025-05/fy25-arc-rlf-supp-funding-selections.pdf

`annual_price_usd: 6000` is anchored to Brownfield.ai's existing $500/month Organization plan for five users. At 75 buyers, the resulting annual revenue ceiling is $450,000. https://www.brownfield.ai/pricing/

### Replicability and technical barrier

The workflow is technically reachable. Anchorage's work plan used Excel and municipal GIS data, EPA FRS, a state contaminated-sites database, and EDR reports, then geocoded records by address or coordinates and manually located unmatched records. EPA separately offers a query/submit FRS API, while public ACRES data is available through a queryable ArcGIS layer. https://www.muni.org/Departments/OCPD/Planning/Projects/SiteAssets/Pages/Brownfields/2017%20BrwnfieldCloseout.pdf https://www.epa.gov/frs/intergovernmental-frs-api https://geopub.epa.gov/ArcGIS/rest/services/EMEF/efpoints/MapServer/5

ACRES itself is a restricted online database through which recipients submit data; EPA documents public downloads from CIMC but no public ACRES submission API. A tool can automate source ingestion, matching, and review queues, while authenticated ACRES entry remains a constrained final step. https://www.epa.gov/brownfields/acres-frequently-asked-questions

Customer two would still require local assessor/GIS mappings, state-specific environmental sources, and organization-specific historical records. The sources establish recurring Excel/GIS usage, but they do not establish one schema or vendor covering a meaningful share of buyers; `replicability: 1` is therefore below the hard floor. SECOG also requires municipality meetings and judgment about ownership, contamination, redevelopment potential, and prioritization, limiting the share that a common connector can absorb. https://secogct.gov/wp-content/uploads/CoalitionRFP_16HallsMillRd_Final.pdf

### Persistence

`genuinely-hard`. The Anchorage work plan explicitly requires accuracy checks and manual location of records that cannot be matched by address or coordinates, showing a real entity-resolution long tail across changing parcels and heterogeneous sources. Confidence-ranked matching is feasible, but local schemas, historical evidence, and unresolved records prevent a turnkey shared workflow today. https://www.muni.org/Departments/OCPD/Planning/Projects/SiteAssets/Pages/Brownfields/2017%20BrwnfieldCloseout.pdf
