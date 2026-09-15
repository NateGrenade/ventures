---
slug: corrugated-die-room-tooling-coordinator-rekey
status: sandbox
cell_id: onet-51-4111.00
created: 2026-09-15
owner_agent: sweep-21b
job: Tooling coordinators manually assign cutting-die and print-plate identifiers
  in log books and spreadsheets, then enter locations and supporting records into
  HRMS and production systems, because tooling records are maintained across those
  separate artifacts.
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 2
---
# Corrugated Die-Room Tooling Coordinator Rekey

## Problem statement

Pratt tooling coordinators maintain tooling spreadsheets and assign print-plate and cutting-die IDs from a log book, then record plate locations in HRMS and attach supporting documentation. They also scan print cards and CADs into a system. The Sandston posting explicitly assigns these separate records to one role; Tulsa corroborates spreadsheet tracking, tooling identifiers, and system documentation. These are two sites of one employer, not independent evidence from two companies. The Tulsa URL was readable through web browsing but failed the repository verifier at closeout; its claim is retained with an explicit flag.

## Evidence

- [type: job-posting] (2026-09-08; accessed 2026-09-15) Pratt Industries, Sandston, Virginia: maintains monthly tooling spreadsheets; assigns print-plate and cutting-die numbers from a log book; enters plate locations in HRMS; attaches supporting documentation; and scans print cards and CADs into the system. https://careers.prattindustries.com/en/jobs/27-24386/tooling-coordinator-1st-shift/
- [type: job-posting] (2026-07-27; accessed 2026-09-15) Pratt Industries, Tulsa, Oklahoma: assigns and logs tooling numbers, maintains tooling assignment records and die spreadsheets, tracks inventory, and scans or documents print cards and CADs in the system. https://careers.prattindustries.com/en/jobs/30-23768/tooling-coordinator-1st-shift/ [UNREACHABLE]

## Automation hypothesis

SPECULATIVE. A tooling-intake application could capture an identifier and location once, retain the related print-card and CAD documents, and produce the approved updates for HRMS or the plant production system. The postings establish separate recording duties; they do not establish that every field is rekeyed, that the systems lack an import interface, or that staff would adopt another capture device.

## Additional Evidence

The resumed tool-and-die sweep supplied the two direct employer postings above. They replace expired or blocked mirrors and clarify that current corroboration comes from one employer. Earlier citations and claims remain in Git history and the batch's resume notes. No new idea was created for this match.
