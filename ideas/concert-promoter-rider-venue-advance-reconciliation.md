---
slug: concert-promoter-rider-venue-advance-reconciliation
status: sandbox
cell_id: naics-711321
created: 2026-09-16
owner_agent: sweep-22
job: promoter representatives at touring concert and performing-arts promoters manually
  reconcile incoming artist technical and hospitality riders against each venue's
  actual production capabilities to build the show-day advance plan, because tour-management
  tools centralize and share rider documents but do not compare rider requirements
  against a specific venue's capacity
split_from: null
evidence_tier: 1
cursory_screen:
  independent_source_organizations:
  - Peachtree Entertainment
  - AEG Presents (The Bowery Presents)
  - Platinum Road (Dave Ockun, independent tour/production manager)
  competitor_queries:
  - advancing software OR show advance software tour rider venue automate
  - Master Tour Eventric advancing rider venue capabilities match
  direct_competitors: []
  adjacent_competitors:
  - Master Tour (Eventric)
  - Prism.fm
  - ShowAdvance
  - Tour Assistant
  gap_source_urls:
  - https://www.platinumroad.com/post/show-advancing-comedy-tours-before-load-in
  - https://support.eventric.com/hc/en-us/articles/360060671272-Advancing-Events
  pass_reason: All identified tour-management products (Master Tour, Prism.fm, ShowAdvance,
    Tour Assistant) store, generate, or share rider and advance documents, but none
    was shown to automatically compare a specific rider's requirements against a specific
    venue's production capacity; a 30-year veteran tour manager describes doing this
    comparison by hand in Excel workbooks and printed binders even while naming Master
    Tour as an available tool.
scores: {}
human_verdict: null
cost_usd: null
source_count: 3
---

# Concert Promoter Rider-to-Venue Advance Reconciliation

## Problem statement

Promoter representatives and tour/production coordinators at touring concert
and performing-arts promoters (companies that book shows into venues they do
not own, the "promoters/presenters without facilities" business) are hired in
part to take an artist's technical and hospitality rider — a free-form PDF or
Word document produced by the artist's agent or tour manager — and manually
check it against what a specific venue can actually provide: power, rigging,
loading dock, parking, catering, dressing rooms, local labor. The output is a
synthesized "advance sheet" or "day sheet" distributed to venue departments,
security, and the artist's crew before load-in. This is done per show, per
venue, because riders are generic across a tour while venue capabilities are
not, and the negotiated substitutions (equipment rentals, schedule changes)
have to be worked out and documented before the day of the show.

## Evidence

- [type: job-posting] (accessed 2026-09-16, posted ~Feb 2026) Peachtree
  Entertainment's "Promoter Representative" listing (Nashville, TN) requires
  the hire to "review, negotiate, and reconcile technical riders, hospitality
  riders, and production requirements" and separately to reconcile "post-show
  settlements and production costs with internal teams" — two distinct
  reconciliation duties in one role.
  https://jobs.digitalhire.com/job-listing/opening/2nrivhpUNhvOQ1mJilTbNc
- [type: job-posting] (posted 2018-05-29, listing closed but text preserved)
  AEG Presents (The Bowery Presents) "Promoter Representative" listing (New
  York, NY) requires the hire to "review artist contract related to
  production, merchandise, ticketing, and rider requirements" to ensure
  fulfillment on show day, in addition to settling shows with accounting.
  https://wayup.com/i-Entertainment-j-Aeg-Corporation-137766389809471
- [type: practitioner] (2023-07-06, updated 2023-07-13) Dave Ockun, a
  30-year touring/production manager and founder of Platinum Road, describes
  advancing as verifying that "what the show is actually getting" matches the
  rider ("a rider tells people what the show may need"), walks through
  building Excel-based tour info sheets with color-coded tabs, printed tech
  packs kept in binders, and open-item tracking across departments — and
  names Master Tour and "Day Sheets" software as options he sometimes uses
  alongside, not instead of, this manual process.
  https://www.platinumroad.com/post/show-advancing-comedy-tours-before-load-in

## Cursory uniqueness check

Queries run: `"advancing software" OR "show advance software" tour rider venue
automate`; `"Master Tour" Eventric advancing rider venue capabilities match`;
`promoter+"settlement"+"multiple venues"+ticketing data manual spreadsheet
reconcile`.

- **Master Tour (Eventric)** — the dominant tour-management platform named in
  the industry. Its own support docs describe advancing as "a customizable
  checklist" and "shared source-of-truth production data" between touring and
  venue teams — a shared document/checklist system, not an automated diff
  engine. https://support.eventric.com/hc/en-us/articles/360060671272-Advancing-Events
- **Prism.fm** — venue/promoter management suite whose marketing says
  "technical advances, hospitality riders, and production schedules are
  generated automatically from confirmed bookings," i.e. it auto-populates
  standard rider paperwork from booking data, but no page found describes it
  comparing a rider's specific asks against a given venue's actual capacity.
  https://prism.fm/why-prism-for-venues-and-promoters/
- **ShowAdvance** and **Tour Assistant** — smaller apps that store rider
  documents, versions, and open questions per show; both show thin evidence of
  real adoption (placeholder testimonials, "loading" pricing), and neither
  claims automated rider-vs-venue matching.
- No product found performs the actual comparison step — reading a specific
  rider's asks against a specific venue's known capacity and flagging
  conflicts or required substitutions. Every tool found either authors/stores
  the rider (RiderForge, artist-side) or collects/shares it (Master Tour,
  Prism.fm, ShowAdvance, Tour Assistant); the comparison itself is still done
  by a human, evidenced directly by a practitioner naming Master Tour while
  describing his own manual Excel/binder process for the comparison itself.

This is the promoter-side (buyer: touring promoter company such as AEG, Live
Nation, or an independent promoter) mirror of a venue-side version of this
same reconciliation job (venue Technical Director checking an incoming rider
against house specs), which exists as a separate, already-scrutinized and
demoted idea in this corpus at `ideas/performing-arts-venue-technical-rider-reconciliation.md`
(cell `naics-711311`, demoted for unattractive economics, and failing the
replicability and tractability floors). The buyer, integration surface (the
promoter must advance shows across many different venues it does not control,
rather than one venue reconciling against its own fixed inventory), and
employer bearing the cost are different, which is why this is filed
separately per the skill's buyer/job test — but the prior demotion's
reasoning (thin slice of a broader salaried role, no dedicated budget line,
several adjacent vendors sit close to the job without building the diff) may
well transfer to this promoter-side version and should be weighed in Phase 2.

## Automation hypothesis

SPECULATIVE. A tool could ingest a rider (PDF/Word) and a venue's
machine-readable capability profile (power, rigging points, dock dimensions,
parking, labor rules), then auto-flag line items the venue cannot meet as
written and suggest standard substitutions, producing a first-pass advance
sheet and open-item list for the promoter rep to negotiate from. This depends
on riders being extractable despite free-form formatting and on venues having
or being willing to maintain a structured capability profile — the same
digitization dependency that sank the venue-side version of this idea, since
promoters advance into venues that do not maintain such profiles today.
