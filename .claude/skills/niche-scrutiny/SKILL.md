---
name: niche-scrutiny
description: Triage and rigorously critique candidate ideas sitting at status sandbox in Nathan's niche-hunt repo, producing sourced criticism, a mandatory persistence hypothesis explaining why the inefficiency still exists, structured rubric field values, and a promote/demote decision. Use whenever Nathan asks to review, critique, scrutinize, prune, or evaluate ideas in the repo, whenever the driver script runs a scrutiny batch, and whenever he asks what survived or what should be killed. This is Phase 2 of the niche-hunt pipeline — use it even if he just says "go through the new ones." Do NOT use for gathering new candidates (niche-sweep), for running validation tests (niche-falsify), or for deep research (niche-dossier).
---

# Niche Scrutiny (Phase 2)

Kill most of what Phase 1 produced, and say precisely why.

## The failure mode this skill exists to prevent

You and the sweep agent are the same model with the same priors. Left alone, "critique" degenerates into generic objections — *market size is unclear, incumbents likely exist, execution risk is high* — which sound rigorous, apply to everything, and filter nothing.

**The rule: no criticism without a citation.** If you cannot name the incumbent, link the pricing page, or point at the substitute, you have not found a problem. You have had a feeling.

## Step 1 — Triage (cheap, aggressive)

Load candidates:
```bash
python scripts/list_ideas.py --status sandbox
```

For each, a short pass. Kill immediately on any of:

- No Tier 1 or Tier 2 evidence (check `evidence_tier`, do not re-derive it)
- The buyer cannot be named — not a company type, an actual role that holds budget
- The "manual workflow" is already a mature software category with three-plus established players
- The problem statement is a vendor's framing in different words
- Fewer than two independent sources

Set `status: demoted` with a one-line reason. Target 50–70% elimination here, at a few cents each. Do not write a full critique for a triage kill.

## Step 2 — Grounded critique (expensive, survivors only)

For each survivor, append a `## Evaluation & Scrutiny Log` section addressing all four. Each finding carries a URL or it is not a finding.

**Competition.** Name incumbents. Link them. Note pricing where public. Distinguish *direct* (does this exact job), *adjacent* (does it as a feature), and *substitute* (the spreadsheet, the offshore team, the temp). The substitute is usually the real competitor and usually ignored.

**Buyer.** Name the role holding the budget. If no such role exists — the pain is distributed across people who each own a fraction — say so. That is a finding, and usually a fatal one.

**Deal economics.** Estimate plausible contract value against the cost of reaching the buyer. Many genuine inefficiencies are unsellable: real pain, ten thousand buyers, four thousand dollars a year each, no channel. State the reasoning; a number without a derivation is a hallucination with a dollar sign on it.

**Technical barrier.** Identify the integration surface. Note explicitly when the incumbent system has no API or export — that is simultaneously the moat and the obstacle, and which one it is depends on facts you should try to establish.

## Step 3 — The persistence question (mandatory)

Answer: **why does this inefficiency still exist in 2026?** Choose exactly one tag and defend it in two or three sentences.

| Tag | Meaning |
|---|---|
| `unattractive-economics` | Real pain, too little money to support a business |
| `fragmented-buyer` | Thousands of tiny buyers, no distribution channel |
| `regulatory-moat` | Certification, licensing, or liability gates entry |
| `incumbent-distribution` | Someone owns the relationship; product quality is irrelevant |
| `genuinely-hard` | The technical problem is not solved |
| `recently-unlocked` | A capability or cost change made this newly feasible |
| `unnoticed` | Nobody has looked |

**`unnoticed` is almost always wrong.** Markets are not that inefficient. Selecting it requires evidence that the sector is genuinely obscure — no trade press, no conference track, no vendor category. Absent that, pick the real reason.

Only `recently-unlocked` and `genuinely-hard` are eligible for promotion. This field filters harder than the entire rubric.

## Step 4 — Emit structured values, let the script score

Write rubric field values into frontmatter using the anchored scales in `references/rubric.md`. Read that file before your first scoring of a session.

```bash
python scripts/score.py --slug <slug>
```

**Do not compute the weighted score yourself.** Models are inconsistent at arithmetic and drift toward generosity across a long batch.

## Step 5 — Set status

Promotion requires **all** of:

- Two or more independent Tier 1/2 sources
- A named buyer role with budget authority
- Persistence tag of `recently-unlocked` or `genuinely-hard`
- `tractability` scored 2 or above — software must be able to reach the workflow
- Composite score above threshold (`score.py` reports pass/fail)

Otherwise `status: demoted`. **Demoted ideas are never deleted.** They are the training data for frontier policy and for Nathan's calibration file.

## Step 6 — Check yourself against calibration

Before finishing a batch, read `calibration/rubric-notes.md`. It holds Nathan's hand-written record of cases where the rubric and his judgment diverged. Where it conflicts with the scales in `references/rubric.md`, **his notes win** — the rubric is a proxy, his taste is the target.

If your promotion rate for this batch exceeds roughly 20%, treat that as a signal you have gone soft and re-read the triage criteria before committing.

## Concurrency

Edit only the idea files you were assigned. Append to `calibration/` only via script. Never touch `INDEX.md` — run `python scripts/build_index.py` at the end of the batch and let it regenerate.
