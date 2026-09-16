---
slug: grain-warehouse-monthly-regulatory-report-compilation
status: demoted
cell_id: naics-493130
created: 2026-09-15
owner_agent: 2026-09-15-codex-24-sweep-03
job: licensed grain warehouse office staff manually compile stock, receipt, liability,
  and capacity totals between internal position records and government reporting forms,
  because state portals and federal questionnaires require operator-submitted figures.
split_from: null
evidence_tier: 1
buyer_role: Grain accounting manager / controller at a licensed grain warehouse company
persistence: unattractive-economics
buyer_count: 300
annual_price_usd: null
scores:
  pain_evidence: 2
  buyer_clarity: 1
  incumbent_gap: 1
  reachability: 2
  tractability: 1
  replicability: 1
  persistence_quality: 0
  deal_economics: 0
human_verdict: null
cost_usd: null
source_count: 4
revenue_ceiling_usd: null
composite: 32
gate_pass: false
scored_profile: balanced
---

# Grain Warehouse Monthly Regulatory Report Compilation

## Problem statement

Licensed grain warehouses maintain daily position records and submit recurring stock and
receipt totals to regulators. Kansas requires monthly company totals across all functional
units, while Iowa provides a separate portal in which operators enter the prior month's
W-11 report
([Kansas regulation](https://regulations.justia.com/states/kansas/agency-4/article-25/section-4-25-5/),
[Iowa portal](https://data.iowaagriculture.gov/grainreport/)). USDA's current off-farm
grain-stocks questionnaire separately asks multi-facility firms to assemble state-level
capacity and commodity totals
([USDA/NASS](https://www.nass.usda.gov/Publications/Methodology_and_Data_Quality/Grain_Stocks/02_2026/IL_Off_Farm_GrainStocks_Questionnaire_Dec2025.pdf)).

## Evidence

- [type: regulatory] (current through 2025-06-26) Kansas Administrative Regulation
  4-25-5 requires public warehousemen to maintain daily summarized position reports, send
  copies of executed warehouse receipts each month, and submit monthly grain-stock totals
  across all functional units by the fifth day of the month.
  https://regulations.justia.com/states/kansas/agency-4/article-25/section-4-25-5/
- [type: regulatory] (2026 statutes, current page accessed 2026-09-15) Kansas Statute
  34-249a requires a monthly statement of stocks for each licensed warehouse location and
  requires receipt, grain-liability, unencumbered-grain, and total-stock information on
  demand.
  https://kslegislature.gov/b2025_26/laws/034_000_0000_chapter/034_002_0000_article/034_002_0049a_section/034_002_0049a_k/
- [type: regulatory] (current portal accessed 2026-09-15) The Iowa Department of
  Agriculture Grain Warehouse Bureau instructs warehouse operators to enter the previous
  month's W-11 report in its reporting portal and separately enter the quarterly
  per-bushel assessment.
  https://data.iowaagriculture.gov/grainreport/
- [type: regulatory] (2025-12 reference period; form current in 2026) USDA/NASS's Illinois
  off-farm grain-stocks questionnaire asks an operation to report aggregate capacity and
  stock by commodity, prepare separate state reports, and combine multiple facilities when
  individual plants do not report. USDA estimates 15 minutes per response for reviewing
  instructions, searching data sources, gathering and maintaining data, and completing and
  reviewing the form.
  https://www.nass.usda.gov/Publications/Methodology_and_Data_Quality/Grain_Stocks/02_2026/IL_Off_Farm_GrainStocks_Questionnaire_Dec2025.pdf

## Evaluation & Scrutiny Log

Critic `critic-scrutiny-20260915T204319Z-4`, 2026-09-15. Survived triage (Tier 1
regulatory evidence, not a vendor's framing, a real recurring obligation). Demoted after
grounded critique.

### Source verification

I opened sources myself rather than trusting the tags.

- **Kansas K.A.R. 4-25-5 — verified, and it cuts against the idea.** The Justia mirror
  cited in the file 403s to automated fetch; I read the same regulation on Cornell
  (https://www.law.cornell.edu/regulations/kansas/K-A-R-4-25-5). It confirms the claimed
  duties: a daily summarized position report covering quantity received and shipped, the
  quantity remaining at the close of each business day, and total storage obligation per
  kind of grain; copies of executed warehouse receipts by the fifth of each month; and a
  statement of stocks through the last day of the preceding month, also by the fifth.
  It also says something the sweep did not record: **"all records required to be
  maintained pursuant to this regulation may be completed and maintained electronically."**
  Kansas is not forcing paper. The regulator has already removed the obstacle this idea
  assumed.
- **Iowa W-11 portal — verified.** https://data.iowaagriculture.gov/grainreport/ instructs
  operators to "Enter your monthly W-11 grain warehouse report. This is for the previous
  month only," plus a quarterly per-bushel indemnity assessment and license renewal fees.
  Confirmed by reading the page: it is a hand-keyed web form. **No file upload and no API
  are offered.** That is the real technical finding here, and it is bad news, not good.
- **USDA/NASS Illinois off-farm grain-stocks questionnaire — NOT verified.** The PDF
  returns HTTP 403 to both WebFetch and curl with a browser user-agent. I could not
  confirm the "15 minutes per response" burden estimate the file attributes to it. I have
  left the claim in the Evidence section but I am **not scoring on it**; a burden figure I
  could not read cannot support `pain_evidence: 3`. If anything, 15 minutes per response
  would argue against the idea, not for it.

Two independent Tier 1 sources therefore stand on my own reading (Kansas KAR via Cornell,
Iowa portal). The Kansas statute 34-249a source was not independently re-verified and is
not load-bearing — it restates the regulation.

### Competition

Queries run: `grain elevator software "position report" state warehouse regulatory
reporting daily position report DPR AGRIS AgVantage`; `"grain warehouse" licensed
warehouse monthly report software compile state report W-11 Iowa Kansas automate`;
`software to automate state grain warehouse license compliance reports multi-state filing
elevator "compliance reporting"`; `AgVantage OR AGRIS OR "Vertical Software" OR Bushel
grain software "state reports" warehouse examiner monthly stocks report generate`;
`ExamHand grain warehouse examination software state warehouse examiners`.

**Direct.** This job has a dedicated vendor lineage going back to 1988.

- **ExamNet** (https://www.examnet.com/, redirected from getexam.net) is grain inventory
  software that converts USDA-approved measurements into **regulatory reports**. Its own
  page: "Trusted by state agencies, elevator operators, and auditors across the country,"
  delivering "audit-ready reports." It automates bushel calculations, tracks grain across
  **multiple facilities**, and generates timestamped documentation for regulatory
  submission. That is this idea's stated job — aggregate across locations, produce the
  regulator's figures — already shipping, already sold to elevator operators.
- **ExamHand** (https://examhand.com/, Miller & Associates) has been the brand state grain
  warehouse agencies use for examinations since 1988, now in its 4th generation, used by
  CO, IL, IN, OH, MI and KS warehouse examiners among others. Michigan runs a **Measured
  Self Inventory program** in which licensed grain dealers submit inventory through this
  ecosystem rather than waiting for an examiner
  (https://www.michigan.gov/mdard/-/media/Project/Websites/mdard/documents/business-development/grain/exam_net_measured_self_inventory_msi_program_roll_out.pdf).
  So the operator-submits-data-to-regulator pattern already exists as a state program.

**Adjacent.** The grain ERPs generate the upstream numbers and already build bridges to
the regulator side. Cultura/Greenstone documents an **AGRIS "AGRO / AAWCO Warehouse
Examiner Data Interface"** as a shipped feature
(https://culturatech.atlassian.net/wiki/spaces/ACD/pages/586776577/). AgVantage advertises
a live DPR and end-of-month valuations (https://www.agvantage.com/products/grain.html).
Vertical Software markets "ticketing, accounting, inventory, and compliance"
(https://www.verticalsoftware.net/).

**Substitute.** The elevator prints the month-end position report its ERP already
produces and keys ten numbers into the Iowa portal. For a single-location warehouse this
is a few minutes a month. The substitute wins on effort, and it is free.

`incumbent_gap: 1` — one or two direct competitors serving the job adequately, plus
adjacent coverage from every major grain ERP.

### Buyer

The sources name **staff**, not budget. Kansas and Iowa address "the public warehouseman"
and "the operator" — a legal entity, not a purchasing role. The plausible budget holder is
the grain accounting manager or controller at a licensed warehouse company, which is who I
recorded, but no source in this file evidences that person buying a compliance tool, and
at a single-location country elevator the same person is often the general manager. There
is no line item to sit beside: the reporting duty is bundled into a grain ERP subscription
the firm already pays for. `buyer_clarity: 1`.

### Deal economics

**`buyer_count: 300`.** Bottom-up: Iowa's public licensed-warehouse registry
(http://idalsdata.org/IowaData/grainWarehouseDirectoryReportHtml.cfm?version=HTML) lists
roughly 280 licensed operator entries. Iowa is among the top grain states; scaling across
the ten major Corn Belt and Plains grain states plus a tail gives an order-of-magnitude
national count around 2,500–3,500 licensed warehouse **companies** (NAICS 493130's ~1,198
Census establishments undercounts badly, because most country elevators classify under
424510 grain merchant wholesalers). Cut: the compile-and-aggregate pain is only real for
**multi-location, multi-state** firms — a single-site elevator transcribes one form a
month. Multi-location firms are a clear minority, and the largest of them already run
AGRIS or AgVantage with the examiner data interface. I take **~10%**, giving ~300.
**Confidence: low.** This is the load-bearing assumption and I would not defend the 10%
against a phone call to three state warehouse bureaus.

**`annual_price_usd: null` — I could not establish it.** There is no public price for any
product in this category: ExamNet, ExamHand, and the AGRIS examiner interface all price by
quote. Nothing this buyer already pays for maps to a defensible per-year figure for a
regulatory-reporting module, and inventing one to clear the $25k floor is exactly what the
rubric forbids. The ceiling is therefore undetermined and `deal_economics` fails its
floor. That is the correct outcome, not a rounding error — but note it is **not** what
kills this idea; the persistence tag does that on its own.

### Replicability

The upstream surface is shared (AGRIS/AgVantage exports). The downstream surface is not.
Kansas wants executed warehouse receipts plus a statement of stocks mailed or sent
electronically by the fifth; Iowa wants a W-11 typed into a bespoke state portal by the
tenth; USDA/NASS wants a separate paper questionnaire per state. **There is no mandated
common schema across states** — no analogue of an EDI transaction set or an XBRL taxonomy
here. Every state added is a new form, new deadline, new portal, and a new relationship
with a state bureau. Customer #2 in a new state costs roughly what customer #1 did.
`replicability: 1` — below the floor of 2.

### Technical barrier

Read from the source side, fine: the ERPs export. Read from the submission side, this is
the wall. The Iowa portal offers a web form with no upload and no API (verified by reading
the page). Kansas accepts electronic records "upon request" and by email, not by machine
interface. Automating submission means screen-scraping state portals — brittle, and a
category of work state agencies periodically break. Automating only *compilation* leaves
the human doing the typing, which is most of the fifteen minutes. `tractability: 1` —
integration with a closed system, feasibility unestablished. Per the rubric that is a
demote by itself regardless of composite.

### Persistence — `unattractive-economics`

Why is this still manual in 2026? Because the task is small and the money is not there.
Each operator owes a handful of aggregate numbers per month, the state has already
permitted electronic recordkeeping (K.A.R. 4-25-5), and the vendors closest to the data —
ExamNet on one side, AGRIS's examiner interface on the other — have built exactly as much
as the revenue supports and stopped. Fifty state regimes each worth a few hundred small
operators is a per-state market too thin to fund a per-state connector, which is the same
reason no incumbent has unified it either.

It is explicitly **not** `genuinely-hard`: nothing computational is unsolved, ExamNet
already produces regulatory reports from measurements. It is not `recently-unlocked`:
nothing changed in 2024–2026 that makes typing a W-11 newly automatable, and the portal
still has no API. `persistence_quality: 0`.

### Verdict

Demoted. Fails four ways independently: ineligible persistence tag (hard gate),
`tractability` 1 (below floor 2), `replicability` 1 (below floor 2), and an undetermined
revenue ceiling (below the `deal_economics` floor). The persistence tag is the honest
headline — this is a real, recurring, genuinely annoying obligation that stays manual
because it is not worth anyone's money to fix, in a market where the vendors who could fix
it tomorrow have chosen not to.

## Automation hypothesis

SPECULATIVE. A reporting connector could map daily-position and warehouse-receipt exports
to state and federal report fields, aggregate across locations, and retain a reviewable
submission package. The sources prove repeated operator reporting and data aggregation;
they do not prove that any specific regulator offers an API or that a warehouse's existing
grain software lacks built-in exports for these forms.
