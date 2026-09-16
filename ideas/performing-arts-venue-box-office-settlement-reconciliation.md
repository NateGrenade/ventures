---
slug: performing-arts-venue-box-office-settlement-reconciliation
status: demoted
cell_id: naics-711311
created: 2026-09-15
owner_agent: 2026-09-15-codex-24-sweep-09
job: performing arts venue box office managers manually reconcile ticketing-system
  reports with cash and card records and artist deal terms into finance and performer
  settlement reports, because the ticketing system does not contain every payment
  adjustment and contractual settlement rule
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 3
---

# Performing Arts Venue Box Office Settlement Reconciliation

## Problem statement

Box office managers at live performance facilities reconcile cash, card, and ticket sales, report the results to finance, and prepare counts or settlements for outside artists and agents. Current job descriptions place daily sales reconciliation, ticketing-system administration, finance reporting, and artist settlement in the same role. A ticketing-system support article describes moving ticket-revenue totals into a separate Excel settlement sheet and adjusting for tickets recorded as sales even when the venue has not collected the money.

## Evidence

- [type: job-posting] (2026-05-20) Union County Performing Arts Center's Box Office Manager description requires managing ticketing platforms including VBO, AudienceView, Tessitura, and Eventbrite; preparing and reconciling daily cash, credit-card, and ticket-sales reports; and coordinating across finance, rental clients, and touring productions. The listed salary is $45,000-$55,000. https://ucpac.org/wp-content/uploads/2025/05/UCPAC-BO-Mgr_Job-Description_updated-5.20.2026-2.pdf
- [type: job-posting] (accessed 2026-09-15) Live Nation's Summit Music Hall Box Office Supervisor posting requires balancing seller cash drawers, reconciling and accounting for ticket sales, conducting band settlements for split-point deals, and distributing daily ticket counts to agents and artists. https://livenation.wd503.myworkdayjobs.com/en-US/LNExternalSite/job/Box-Office-Supervisor-PT--Summit-Music-Hall_JR-91878
- [type: vendor] (accessed 2026-09-15) Theatre Manager's event-settlement support page says its revenue totals are used in a separate settlement Excel sheet and warns that some tickets appear in sales totals even though the box office has not collected the money, requiring settlement adjustments outside the sales total. https://help.theatremanager.com/frequently-asked-questions/event-settlement

## Automation hypothesis

SPECULATIVE. A settlement workspace could ingest ticketing exports, POS and deposit records, and artist contract terms; identify unmatched payments or adjustments; and generate reviewed finance and performer settlement packets. Feasibility depends on stable access to ticketing and payment data and reliable parsing of venue-specific artist agreements; whether existing ticketing suites already cover enough of this workflow is unverified.

## Scrutiny decision

Demoted at triage (critic-scrutiny-20260915T204319Z-6): venue box-office-to-artist-settlement is already a mature software category with well past three established players selling exactly this job — [Opendate](https://www.opendate.io/info/music-venue-management-software), which names performing arts centers as a target segment and sells integrated ticketing plus "offers and settlement"; [Prism.fm](https://prism.fm/blog/venue-insights/concert-venue-settlement-best-practices/), which markets settlement automation for versus/split-point deals explicitly as a replacement for the settlement spreadsheet; and [VenuePilot](https://www.venuepilot.com/), whose "artist settlement platform" covers multi-date settlement sheets, artist payouts, and complex deal structures including bar-percentage splits at $0.75/ticket. Gigwell and Muzeek sell the same workflow, and the idea's own cited ticketing vendor (Theatre Manager) ships an event-settlement module. The residual gap — daily cash/card drawer reconciliation feeding the settlement — is a feature of the ticketing suite the venue already runs, not a standalone product. No full critique written.
