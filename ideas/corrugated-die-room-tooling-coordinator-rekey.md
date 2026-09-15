---
slug: corrugated-die-room-tooling-coordinator-rekey
status: sandbox
cell_id: onet-51-4111.00
created: 2026-09-15
owner_agent: sweep-21b
job: Tooling coordinators at corrugated-packaging and stamping plants manually inspect
  and tag incoming cutting dies and print plates, log them onto die spreadsheets or
  a paper die/cutting-die log book, and then separately scan and re-key the same print-card
  and CAD identifiers into the plant's production system, because the physical tooling-intake
  process and the production/ERP system share no data path.
split_from: null
evidence_tier: 1
scores: {}
human_verdict: null
cost_usd: null
source_count: 4
---

# Corrugated Die-Room Tooling Coordinator Rekey

## Problem statement

Corrugated-box and packaging plants keep a "die room" that stages, inspects, and
repairs the steel-rule cutting dies and print plates used on their die-cutters and
flexo presses — a support function adjacent to tool-and-die making. A dedicated
"Tooling Coordinator" role exists at multiple plants and companies specifically to
run this intake: inspect each die/plate as it comes off a job, tag it, log it (by
tool number) on a die/tooling spreadsheet, and separately scan and key the
associated print-card and CAD identifiers "into the system" so production can find
the right tooling for the next scheduled job. This is described as a recurring,
full-time, hourly position — not a side duty — at more than one employer, which
implies real ongoing labor cost, not a one-time setup task.

## Evidence

- [type: job-posting] (2026-09-09, live) Pratt Industries, Rock Hill, SC —
  "Tooling Coordinator." Duties include "Assign and log tooling numbers for easy
  tracking," "Maintain accurate records of tooling assignments and updates," and
  "assist with scanning and documenting print cards and CADs in the system," plus
  physically inspecting and staging cutting dies and print plates.
  https://careers.prattindustries.com/en/jobs/0138-24023/tooling-coordinator/
- [type: job-posting] (2026-09-11, live) Pratt Industries, Fort Worth, TX (3rd
  shift) — "Tooling Coordinator." Duties include "Maintain die spreadsheets and
  track inventory," "Assign and log tooling numbers for easy tracking," and
  document print cards and CAD files "in the system," across multiple storage
  locations.
  https://careers.prattindustries.com/en/jobs/108-24226/tooling-coordinator/
- [type: job-posting] (retrieved 2026-09-15, undated, since expired) Pratt
  Industries, La Vergne, TN — "Tooling Coordinator." Describes keeping "die
  spread sheets," checking in incoming print plates, assigning IDs "from the
  Print or Cutting Die Log Book," and entering that information "into HRMS."
  https://www.simplyhired.com/job/h7KZSqAxMP_pTfjl2cE_Uwu-69kNIeLtadrxX6_NW0_C9wncefuPWQ
- [type: job-posting] (retrieved 2026-09-15, snippet only, full posting blocked
  by bot-protection) Hood Container Corporation, Sandston, VA — "Tooling
  Coordinator" listing described as "Managing tooling asset lifecycle in
  corrugated packaging manufacturing," confirming the same role exists at a
  second employer, not just Pratt Industries.
  https://www.simplyhired.com/job/u4c864-SU3MK-BcMAHG7ywyg-2HlRO8S8fBB3zR0eVhxfk3X9R99zQ

## Automation hypothesis

SPECULATIVE. If the die/print-plate log (paper log book or spreadsheet) and the
plant's production/ERP system where print-card and CAD identifiers are scanned in
are genuinely disconnected, a lightweight intake app — barcode/QR-tag each die or
plate at first inspection, capture condition and location on a phone or tablet,
and push that record directly into the plant's production system via API or a
scheduled export — could collapse the "log on paper, then re-key into HRMS/ERP"
two-step into one. This is tractable only if the target production system
(unnamed in these postings — likely an ERP or MES module) exposes an import path;
if it is a closed legacy system with no integration surface, this stays a
spreadsheet-replacement product at best. Worth confirming which ERP/MES corrugated
plants commonly run before assuming an integration exists.
