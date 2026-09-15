---
name: niche-falsify
description: Run cheap disconfirming tests against promoted ideas in Nathan's niche-hunt repo — naming the single riskiest assumption, executing the automatable tests (job-board checks, incumbent feature audits, forum searches), and queueing the human-executed ones with a pre-written call script — then resolving each idea to validated or falsified. Use whenever an idea reaches status promoted, whenever Nathan asks to test, validate, sanity-check, or pressure-test an idea before committing real time to it, and whenever he asks what he should go verify himself. This is Phase 3 of the niche-hunt pipeline and it sits between scrutiny and deep research — use it even if he just says "is this real?" Do NOT use for critiquing sandbox ideas (niche-scrutiny) or for building out proposals (niche-dossier).
---

# Niche Falsification (Phase 3)

Try to kill promoted ideas cheaply, before anyone spends real time on them.

This phase exists because the previous version of this pipeline went straight from "promoted" to a full proposal directory — which produces beautiful architecture documents for businesses that do not exist. **A high kill rate here is the phase working correctly.** If nothing is dying, the tests are too weak.

## Step 1 — Name the single riskiest assumption

Not a list. One belief whose falsity kills the idea outright.

Almost always one of:
- **The pain is real and recurring** — not an anecdote, not one unusual firm
- **Someone with budget authority feels it** — the person suffering and the person paying are the same person, or adjacent
- **No adequate solution already sits in their stack** — including a feature of software they already own
- **The work is actually automatable** — the manual step exists because of judgment, liability, or relationship, not because nobody built the tool

Write it as a falsifiable sentence in a new `## Falsification Log` section. Bad: *demand may be limited.* Good: *Fewer than 20 US firms employ someone whose primary task is this reconciliation.*

## Step 2 — Pick the cheapest disconfirming test

Work down this ladder. Stop at the first test that could actually kill the assumption — do not run all of them.

| Cost | Test | Kills |
|---|---|---|
| Free | Job-board search for the manual role across the sector | "Pain is real and recurring" |
| Free | Check whether incumbent vertical software ships this as a feature — read changelogs, feature pages, help docs | "No adequate solution exists" |
| Free | Forum search for how operators currently work around it | "Pain is real"; also reveals the true substitute |
| Free | Check for a dead startup that already tried this | Everything — and tells you why it failed |
| Low | Post a question in a practitioner venue | "Pain is real"; surfaces budget holder |
| Human | Five practitioner calls | All of the above, definitively |

The dead-startup check is the most underrated. Someone has usually tried. Finding the corpse is worth more than any amount of market sizing.

## Step 3 — Execute what you can, queue what you cannot

**Automatable tests you run yourself.** Record each in the Falsification Log:

```markdown
### Test: job-board sweep for manual reconciliation roles
- Assumption targeted: pain is real and recurring
- Queries run: <verbatim, all of them>
- Result: 4 active postings across 3 firms; salary band $42-51k
- Verdict on assumption: SURVIVES
```

Record the queries verbatim. A null result from a bad query is not evidence, and next month you will not remember which you ran.

**Human-executed tests get queued** to `worklist.md` with the work pre-done:
- Who to contact and how you found them
- A call script: three questions, the first of which does not mention any solution
- What answer would falsify the assumption, written down *before* the call

The pre-registered falsifying answer matters. Without it, any call outcome gets read as encouraging.

## Step 4 — Resolve

- `status: falsified` — assumption failed. Record which test killed it and what the disconfirming evidence was. These are the most valuable files in the repo; they are how the pipeline learns what your promotions are systematically wrong about.
- `status: validated` — the riskiest assumption survived every test run. This means *not yet dead*, not *good idea*. Only validated ideas are eligible for Phase 4.
- `status: promoted` (unchanged) — the decisive test is human-executed and still queued. Leave it pending; do not promote on automatable tests alone when a call was the real test.

```bash
python3 scripts/score.py --slug <slug> --recompute
python3 scripts/build_index.py
```

## Honesty pressure

You will be tempted to read ambiguous results as survival, because killing an idea feels like wasted work. It is the opposite: a kill here saves a dossier's worth of tokens and a week of Nathan's attention.

When a result is genuinely ambiguous, say `AMBIGUOUS` and escalate to the human test. Do not resolve ambiguity in the idea's favour.
