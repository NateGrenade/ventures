---
slug: self-published-author-royalty-statement-reconciliation
status: demoted
cell_id: onet-27-3043.05
created: 2026-09-15
owner_agent: sweep-11b
job: self-published and hybrid authors manually re-key monthly sales and royalty figures
  from each distribution platform's separate report (Amazon KDP, ACX, IngramSpark,
  Draft2Digital, Kobo, Barnes & Noble Press, direct sales) into a personal tracking
  spreadsheet, because no platform exports a common format or consolidates royalty
  data across an author's whole catalog
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 4
---

# Self-Published Author Royalty Statement Reconciliation

## Problem statement

Authors who publish across more than one self-publishing platform receive a
separate sales/royalty report from each retailer or distributor, in that
platform's own format, on that platform's own schedule. Because no platform
aggregates data from the others, authors who want a single view of what a book
is earning across formats and channels download each report by hand and paste
its figures into a personal spreadsheet every month. Practitioner accounts
describe this as a recurring, multi-source data-entry chore rather than a
one-time setup task, and a cottage industry of paid royalty-reconciliation
software (Royalties HQ, Familiar, Abacus/PublishDrive) has grown up specifically
to replace that spreadsheet work, which is itself evidence the manual version is
still the default for many independent authors.

## Evidence

- [type: practitioner] (2019-01-06) An author-run resource for a DIY sales
  spreadsheet describes the actual workflow: "most of your work will happen once
  a month when you download and paste in data from your various reports"
  spanning Amazon KDP, ACX, IngramSpark, a personal website, and in-person sales,
  each pasted manually into the sheet. https://www.goodreads.com/author_blog_posts/17796409-author-resource-sales-and-royalties-spreadsheet
- [type: practitioner] (2018-10-04) A self-publishing consultant's guide to sales
  tracking states plainly that "none of them can provide a single platform for
  tracking ALL your sales in ALL your channels" and "you're going to have to
  build that yourself," then walks through her own process of manually entering
  monthly figures from Amazon, Barnes & Noble, Kobo, and Smashwords into a core
  spreadsheet tab. https://selfpublishingadvice.org/tracking-book-sales/
- [type: practitioner] (2014-06-05) An indie author's blog post on
  self-publishing bookkeeping describes Amazon alone sending five different
  royalty payments (not counting Createspace), plus separate payments from
  Barnes & Noble and Smashwords, requiring a dedicated spreadsheet just for
  ebook income and another that rolls up all royalty income for the year.
  https://www.goodreads.com/author_blog_posts/6411380-self-publishing-bookkeeping
- [type: trade-press] (2025-09-23) A 2025 publishing-industry blog post on
  royalty transparency notes that "authors with books across multiple platforms
  often find themselves juggling half a dozen dashboards, each with its own
  reporting quirks," indicating the underlying fragmentation persists into the
  current market even as it stops short of describing a specific manual
  workaround. https://blog.publiwrite.com/royalties-in-2025-which-platforms-pay-authors-best-and-why-transparency-matters/

## Automation hypothesis

SPECULATIVE. A lightweight ingestion tool that accepts each platform's native
export (CSV/Excel from KDP, ACX, IngramSpark, Draft2Digital, Kobo, etc.),
normalizes titles, formats, and currencies against the author's own catalog,
and rolls the result into a single dashboard could remove the monthly
copy-paste step for authors who don't sell enough volume to justify existing
paid royalty-management platforms built for publishers with many titles or
staff. This depends on report formats being stable enough to parse reliably and
on individual authors' willingness to pay for something narrower and cheaper
than the existing publisher-grade tools (Royalties HQ, Familiar) that already
serve this exact need at a higher price point; that willingness to pay for a
consumer-grade version at low sales volumes is unverified.

## Scrutiny decision

Demoted at triage on two independent triage criteria.

**Mature software category, three-plus established players doing this exact job at this
exact price point.** [ScribeCount](https://scribecount.com/pricing) consolidates royalty
data from "all 40+ publishing platforms" — KDP, Apple Books, Draft2Digital, Smashwords,
plus Shopify/WooCommerce/BookFunnel direct sales — and its entry tier is **$5.99/month for
authors earning under $500/month**, which is precisely the low-volume indie the automation
hypothesis proposes to serve as an underserved segment. [Book Report](https://www.getbookreport.com/)
is free to authors earning under $1,000/month. [ScribeCount is reviewed head-to-head
against Book Report](https://kindlepreneur.com/scribecount-review/) in the indie-author
trade press, i.e. this is a category with comparison shopping, not a gap. The idea file
itself already names Royalties HQ, Familiar, and PublishDrive's Abacus and concedes they
"already serve this exact need"; the only differentiation offered is a lower price, and
ScribeCount's income-scaled $5.99 tier removes even that.

**No buyer role with budget authority.** The buyer is an individual self-published author
spending personal money, with a demonstrated market price of $0–$6/month. There is no role
holding a budget line for this, and the residual willing-to-pay pool sits below incumbents'
existing free tier.

Recorded for the record, not as the kill reason: the evidence is stale and one tag is
inflated. Three of four sources date to 2014, 2018, and 2019 — before ScribeCount and Book
Report matured — and the one current source is tagged `trade-press` but is
[a vendor's own marketing blog](https://blog.publiwrite.com/royalties-in-2025-which-platforms-pay-authors-best-and-why-transparency-matters/),
which is the "vendor's framing in different words" triage criterion. `evidence_tier: 1` is
not supported.
