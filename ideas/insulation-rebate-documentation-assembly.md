---
slug: insulation-rebate-documentation-assembly
status: demoted
cell_id: naics-238310
created: 2026-09-15
owner_agent: 2026-09-15-codex-24-sweep-14
job: Insulation contractor office staff manually assemble measurements, photos, invoices,
  product details, signatures, and application fields between job folders and utility
  rebate submissions, because each program requires a different evidence package.
split_from: null
evidence_tier: 1
buyer_role: Owner or office manager of a residential insulation contracting firm
persistence: incumbent-distribution
buyer_count: 2500
annual_price_usd: 900
scores:
  pain_evidence: 1
  buyer_clarity: 2
  incumbent_gap: 1
  reachability: 2
  tractability: 2
  persistence_quality: 0
  replicability: 1
  deal_economics: 3
human_verdict: null
cost_usd: null
source_count: 5
revenue_ceiling_usd: 2250000.0
composite: 50
gate_pass: false
scored_profile: balanced
---

# Insulation Rebate Documentation Assembly

## Problem statement

Insulation contractors administer utility and government rebates as part of delivering eligible jobs. A current insulation-company posting assigns an office administrator to process, track, and submit data-heavy rebate applications and ensure that documentation meets program rules; current utility applications require combinations of signed forms, invoices, insulation measurements, installation certificates, and photographs under defined submission deadlines.

## Evidence

- [type: job-posting] (2026-09) Logik Insulation advertised an office administrator responsible for accurately processing, tracking, and submitting data-heavy insulation and energy-efficiency rebate applications and checking required documents against strict program guidelines. https://www.workopolis.com/jobsearch/viewjob/tHwY5c1hupm9LpcEksTi7cbdbAazismmPmh7AUAnk8rnBH0w2gCkm0o5yoHSM73b
- [type: regulatory] (2026-01) NIPSCO's 2026 insulation rebate application requires a completed signed application and an itemized contractor invoice documenting the installed insulation, and requires submission within 60 days of installation or by the year-end deadline. https://www.nipsco.com/docs/librariesprovider11/energy-efficiency/home-energy-assessment/hea-insulation-and-air-sealing-application.pdf?sfvrsn=703ce451_4
- [type: regulatory] (2025-10-01) Columbia Rural Electric Association's weatherization checklist requires an invoice, rebate application, installation certificate, and installation pictures for insulation measures. https://www.columbiarea.coop/wp-content/uploads/Residential-Weatherization-10012025-B.pdf
- [type: regulatory] (2025) Efficiency Manitoba's insulation application specifies contractor invoice fields including area insulated, square feet, starting and final R-values, unit costs, manufacturer and material details, quantities, payment proof, discounts, and returned materials. https://efficiencymb.ca/wp-content/uploads/Home_Insulation_Rebate_Application.pdf
- [type: regulatory] (2026-01-21) Focus on Energy's 2026 trade-ally insulation and air sealing rebate application (Wisconsin) requires household AMI income-tier selection with a confirmation number for the moderate- and low-income tiers, utility account numbers for both fuels, a final itemized invoice whose payee matches the billing section, and a combustion safety/ventilation notification where applicable; submission is within 60 days of installation and no later than August 31, 2026, by mail, email, or an online form. Added by the scrutiny critic, verified by direct text extraction. https://assets.focusonenergy.com/production/docs/trade-ally/TAS-Insulation-Air-Sealing-Rebates-Application-20260101_FILLABLE.pdf

## Automation hypothesis

SPECULATIVE. A rebate packet builder could pull job and invoice data from the contractor's operating system, prompt field crews for the required before-and-after evidence, populate the utility's forms, and track missing fields and deadlines. It would need a maintained rule set for each program and explicit contractor review before submission.

## Evaluation & Scrutiny Log

Critic: critic-scrutiny-20260915T204319Z-1, 2026-09-15, assigned mode, cell naics-238310.
Verdict: **demoted**, on two hard gates — `replicability` below its floor, and an ineligible
persistence tag. The revenue ceiling passes; it is not what kills this.

### Source verification

I opened the cited sources rather than trusting the tags.

- **NIPSCO HEA insulation/air sealing application — verified, supports the claim in full.**
  Text extracted directly from the PDF. It requires prior pre-qualification through the
  Residential Home Energy Assessment program, a beginning attic level below R-11 raised
  above R-38, a completed application signed on page 2, one NIPSCO account per application,
  and an itemized invoice carrying pre- and post-R-value, total attic square footage, square
  footage insulated, total cost, install date and address, a paid-in-full indication, and
  contractor contact details, with the instant-discount rebate itemized to the customer.
  Postmarked within 60 days of installation or by December 31, 2026. Caps: $700 insulation,
  $200 air sealing. Notably the form states that **"NIPSCO's energy efficiency programs are
  administered by TRC, a third-party implementation specialist,"** and submission is by
  emailing one application per email to `NIPSCO.SaveEnergy@TRCcompanies.com`, by mail to a
  TRC PO box, or by fax. That detail matters for both persistence and tractability below.
- **Focus on Energy 2026 trade-ally application — verified, added to the Evidence list.**
  Also extracted directly. Different program, same measure, same year, and essentially
  nothing in common with NIPSCO's form (see Replicability).
- **Columbia Rural Electric Association weatherization checklist — could not verify.** The
  URL returned HTTP 403 to my fetch. This is likely bot-blocking rather than a dead link,
  but I did not confirm the "invoice, rebate application, installation certificate,
  installation pictures" claim myself and have not relied on it.
- **Logik Insulation office administrator posting (Workopolis) — could not verify.** HTTP
  403. This is the **only** cited source that describes a human being doing this work, and
  it is Canadian, as is the Efficiency Manitoba form. I have therefore not let it carry the
  pain score. See `pain_evidence` below.

### Competition

**Direct.** [Snugg Pro](https://snuggpro.com/dsm-and-energy-efficiency-program-software),
owned by program implementer [Franklin Energy](https://www.franklinenergy.com/technology/snugg-pro),
is this product. Its own page claims **1,000+ US companies, 50+ integrated energy efficiency
programs, and coverage in 48 states**, offering live rebate calculations inside the
contractor's specific program, on-site photo upload with a preliminary report before leaving
the job, co-branded reports carrying program-specific rebate information, program job
templates with program-defined costs, document storage, and QA workflow. It is BPI-2400
compliant and was the first auditing tool DOE approved for the HER program. Pricing is
**pay-per-job with no setup or renewal fees, and the program decides whether it or the trade
ally is billed** — which is the distribution fact that kills this idea, not merely a
competitive one.

**Adjacent / the submission surface.** Implementer-run trade ally portals already own the
last mile: [CLEAResult's ATLAS Partner Hub](https://www.clearesult.com/contractor-resources),
Franklin Energy's trade ally portal (they state they recruit and support
[2,000+ contractors nationwide](https://www.franklinenergy.com/program-delivery)), plus
program-specific portals at [SRP](https://www.srpnet.com/doing-business/trade-allies/trade-ally-application-support),
[Puget Sound Energy](https://www.pse.com/en/rebates/trade-allies),
[Consumers Energy](https://consumersenergytradeally.com/rebate-center), and Focus on Energy's
own online form. [Incentit](https://www.incentit.com/markets/energy) sells rebate and trade-
ally spiff management, but to utilities and implementation contractors, not to insulation
firms — it is the other side of the same transaction.

**Substitute.** An office administrator with a folder of job photos, the crew's measurement
sheet, and the accounting system's invoice PDF. For a $700-maximum rebate this is perhaps
fifteen minutes of work per job.

Queries run: "insulation contractor rebate application software automate utility rebate
paperwork submission"; "Snugg Pro home performance contractor software utility rebate program
reporting insulation"; "contractor portal utility energy efficiency program CLEAResult
Franklin Energy upload invoice photos insulation rebate submission"; "rebate software for
insulation contractors submit utility rebates trade ally app photos invoice 2026"; "Incentit
rebate management software contractors pricing / MeasureQuick / EnergyLink insulation rebate
packet assembly competitor". Two contractor-side vendor pages surfaced
([Fieldproxy](https://www.fieldproxy.ai/automations/insulation-utility-rebate-submission),
[K.AI](https://kenyonai.co/blog/ai-automation-insulation-contractor/)) that read as
programmatic SEO landing pages rather than shipped products, and I have not counted them as
incumbents. `incumbent_gap` = 1: one clearly established direct player serving this job.

### Buyer

Real and nameable: the **owner or office manager of a residential insulation contracting
firm**. At this firm size the owner signs for software, so budget authority is not several
levels up. What is missing for a 3 is evidence that this buyer already pays for an adjacent
line item — the closest analogue, Snugg Pro, is explicitly pay-per-job with the *program*
often footing the bill. The buyer's habit is to receive this category free from the utility,
not to purchase it. `buyer_clarity` = 2.

### Deal economics

`buyer_count: 2500`. Bottom-up: NAICS 238310 (Drywall **and** Insulation Contractors) counts
**19,339 firms across 19,986 establishments** in the 2020 Census
([IBISWorld classification page](https://www.ibisworld.com/classifications/naics/238310/drywall-and-insulation-contractors/)).
The code conflates drywall with insulation and drywall is the larger share, so the count must
be cut twice: to insulation-focused firms, and again to those doing residential retrofit work
inside utility rebate programs. I applied roughly a 13% cut. Cross-check from the other
direction: Franklin Energy supports 2,000+ trade-ally contractors nationwide across *all*
measures, and Snugg Pro claims 1,000+ US companies across all trades, which bounds the
residential-EE trade-ally universe at low thousands to low tens of thousands, with insulation
a slice of that. **Confidence: low.** This is the load-bearing number and it is an inference
from a conflated NAICS code, not a roster. An insulation-specific licensing roster or ICAA
membership count would settle it; ICAA does not publish a member count publicly.

`annual_price_usd: 900`. Anchored to the sub-$100/month tier of small-contractor SaaS that
this buyer already occupies, and sanity-checked against per-job value: NIPSCO caps the
insulation rebate at $700 and air sealing at $200, so a packet tool has to cost a fraction of
one job's rebate per month to be an obvious yes.

Ceiling ≈ **$2.25M/yr**, band 3. This gate passes. I want to be explicit that it passes
*on paper only* — the price assumes contractors pay, and the Snugg Pro precedent says the
program pays and the contractor gets it bundled.

### Replicability — the binding failure

Score **1**, below the floor of 2. Two US programs, same measure, same calendar year:

| | NIPSCO (Indiana, admin TRC) | Focus on Energy (Wisconsin) |
|---|---|---|
| Gating condition | Pre-qualify via Home Energy Assessment; pre-R < 11, post-R > 38 | Household AMI income tier, with a confirmation number for the two lower tiers; ≥51% of heating from a participating utility |
| Required docs | Signed application + itemized invoice with a nine-item field list | Final itemized invoice with payee matching billing section + combustion safety/ventilation notification |
| Photos | Not required | Not required |
| Deadline | 60 days from install, or Dec 31 2026 | 60 days from install, no later than Aug 31 2026 |
| Submission | Email one application per email to TRC, or mail to a TRC PO box, or fax | Mail to Madison WI, email, or an online form |
| Other | One NIPSCO account per application; 3-year recurrence limit | Property type, cooling system, heating fuel, original heating system, "how did you hear about us" |

They share no schema, no field set, no document list, no deadline rule, and no submission
channel. The Efficiency Manitoba form cited in the Evidence section adds a third, different
field set (manufacturer and material details, returned materials, discounts). The rubric is
explicit that a 2 or 3 "requires naming the standard or vendor, with evidence of its share" —
there is no mandated schema here and no vendor with commanding share of the *form* layer.
There are on the order of two thousand US utilities plus state programs plus HOMES/HEAR, and
each one is its own rule set to write and then maintain as the program year turns over. The
idea's own `job` field states the problem correctly: "because each program requires a
different evidence package." That sentence is the business risk, not the opportunity. Snugg
Pro reaching 50 programs is evidence that the per-program work is grindable, not evidence
that it is shared — it took an implementer-owned company to do it.

This is a consulting practice with a login page, which is exactly what the replicability
floor exists to catch.

### Tractability

Score **2**, which passes. The assembly work is largely self-contained: fill a PDF, attach an
invoice, check a rule list, watch a deadline. NIPSCO literally accepts an emailed PDF, and
Focus on Energy accepts mail, email, or a web form, so no closed API blocks the output side.
Contractor-side job and invoice data is reachable through ordinary CRM/accounting exports.
Software can touch this workflow; it just cannot be sold profitably into it.

### Reachability

Score **2**. Aggregation points exist — ICAA, state trade-ally networks, implementer
onboarding — but note that every one of them routes through the implementer, who is the
incumbent. You cannot reach this buyer without going through the party whose free tool you
are trying to displace.

### Persistence

Tag: **`incumbent-distribution`** (`persistence_quality` 0, and an ineligible tag under the
gates). The work stays manual not because it is technically hard — it is filling in forms —
but because whoever owns the program owns the contractor relationship and the tooling budget.
NIPSCO's program is run by TRC. Snugg Pro is owned by Franklin Energy, who also recruits the
contractors. CLEAResult runs ATLAS Partner Hub for its own trade allies. A contractor who
finds the paperwork painful asks their program rep, and the program hands them a tool that
the program pays for per job. An independent vendor is selling against free, to a buyer they
can only reach through the entity providing the free thing.

I considered and rejected `genuinely-hard` (nothing computational is unsolved — this is PDF
field-filling), `recently-unlocked` (no capability or cost change made this newly feasible;
the programs and the forms predate 2026), and `fragmented-buyer` (true, thousands of small
firms, but it is the second-order reason; the channel is not absent, it is *owned*).

### Structured values emitted

`pain_evidence` 1 — the anchor for 2 wants two or more independent sources with at least one
Tier 1. The two sources I verified are program forms, which establish that the *requirement*
exists and varies, not that a person is grinding through it or what that costs. The only
source describing the labour itself (the Logik posting) returned 403 and is Canadian. This is
a downgrade from what the sweeper's evidence tier implies, recorded here per the verification
rule.

Other values as argued above: `buyer_clarity` 2, `incumbent_gap` 1, `reachability` 2,
`tractability` 2, `persistence_quality` 0, `replicability` 1, with `deal_economics` derived
by `score.py` from `buyer_count` × `annual_price_usd`.

### What would change the verdict

Not much, and nothing I can reach with search. It would take (a) a real mandated schema
emerging across programs — the federal HOMES/HEAR rollout is the only plausible source of one
— plus (b) evidence that contractors, not programs, hold the tooling budget. Both would have
to be true. Absent that, the honest read is that this is Franklin Energy's business and they
already have it.
