#!/usr/bin/env python3
"""Regenerate the numbers block in the scrutiny rubric from config/scoring.yaml.

The critic reads rubric.md; score.py reads scoring.yaml. If those disagree, the critic is
reasoning against floors the scorer does not apply and you get inexplicable demotes. This
keeps them identical. Run after any config change.
"""
import nichelib as nl

START = "<!-- GENERATED FROM config/scoring.yaml — do not edit by hand -->"
END = "<!-- END GENERATED -->"
RUBRIC = nl.ROOT / ".claude" / "skills" / "niche-scrutiny" / "references" / "rubric.md"


def block(cfg):
    w, fl = cfg["weights"], cfg["floors"]
    L = [START, "", f"**Active profile: `{cfg['profile']}` — promotion threshold "
                    f"{cfg['threshold']}/100.**", "",
         "| dimension | weight | hard floor |", "|---|---|---|"]
    for k in sorted(w, key=lambda k: (-w[k], k)):
        f = fl.get(k, 0)
        L.append(f"| `{k}` | {w[k]} | {f if f else '—'} |")
    L += ["", f"Maximum raw score {cfg['max_value'] * sum(w.values())}, normalized to 100.", "",
          "Revenue ceiling bands (`buyer_count` × `annual_price_usd`):", ""]
    for amt, val in cfg["ceiling_bands"]:
        L.append(f"- ≥ ${amt:,} → `deal_economics` {val}")
    g = cfg["gates"]
    L += ["", "Other gates: at least "
          f"{g.get('min_sources', 2)} sources, evidence tier "
          f"{g.get('max_evidence_tier', 2)} or better, "
          f"{'a named buyer role, ' if g.get('require_buyer_role') else ''}"
          f"persistence in {g.get('eligible_persistence', [])}.", "",
          "A hard floor is absolute: scoring below it is a demote whatever the composite says.",
          "Floors shown as — are disabled in this profile.", "",
          "To change any of this, edit `config/scoring.yaml` and re-run "
          "`python scripts/render_rubric.py`. Check the effect on the real corpus first with "
          "`python scripts/tune.py --compare`.", "", END]
    return "\n".join(L)


def main():
    cfg = nl.config()
    text = RUBRIC.read_text(encoding="utf-8")
    new = block(cfg)
    if START in text and END in text:
        pre, rest = text.split(START, 1)
        _, post = rest.split(END, 1)
        text = pre + new + post
    else:
        text = text.rstrip() + "\n\n" + new + "\n"
    RUBRIC.write_text(text, encoding="utf-8")
    print(f"rubric.md synced to profile '{cfg['profile']}' (threshold {cfg['threshold']})")


if __name__ == "__main__":
    main()
