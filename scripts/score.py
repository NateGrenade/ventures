#!/usr/bin/env python3
"""Compute the composite scrutiny score. Models emit anchored field values; this does the arithmetic.

Kept out of model context deliberately — LLMs drift generous on weighted averages across a batch.

All numbers come from config/scoring.yaml, which is also what generates the numbers section
of the scrutiny rubric. There is exactly one source of truth, so the critic can never be
reasoning against a floor the scorer does not apply.

deal_economics is DERIVED, not emitted: the agent supplies a sourced buyer_count and
annual_price_usd, and the band is computed here. Models are unreliable at mapping a dollar
figure onto a band and drift upward across a batch.
"""
import argparse
import nichelib as nl

DERIVED = {"deal_economics"}


def validate(cfg):
    """Fail loudly on a malformed profile rather than misbehaving at scoring time."""
    problems = []
    bands = cfg["ceiling_bands"]
    if sorted(bands, key=lambda b: -b[0]) != list(bands):
        problems.append("ceiling_bands must be sorted by descending amount")
    band_vals = {b for _, b in bands}
    for dim, floor_ in cfg["floors"].items():
        if dim not in cfg["weights"]:
            problems.append(f"floor set for {dim!r}, which has no weight")
        if floor_ > cfg["max_value"]:
            problems.append(f"floor {dim}={floor_} exceeds max_value {cfg['max_value']}")
    de_floor = cfg["floors"].get("deal_economics", 0)
    if de_floor and de_floor not in band_vals:
        problems.append(f"deal_economics floor {de_floor} matches no ceiling band {sorted(band_vals)}")
    if problems:
        raise SystemExit("config/scoring.yaml is invalid:\n  " + "\n  ".join(problems))


def ceiling(meta):
    """Plausible annual revenue ceiling = reachable buyers x annual price. None if undetermined."""
    n, price = meta.get("buyer_count"), meta.get("annual_price_usd")
    if not n or not price:
        return None
    return int(n) * float(price)


def deal_economics(meta, cfg=None):
    cfg = cfg or nl.config()
    c = ceiling(meta)
    if c is None:
        return 0, None
    for floor_, val in cfg["ceiling_bands"]:
        if c >= floor_:
            return val, c
    return 0, c


def composite(scores, cfg=None):
    cfg = cfg or nl.config()
    w, mx = cfg["weights"], cfg["max_value"]
    total = sum(w[k] * int(scores.get(k, 0)) for k in w)
    return round(100 * total / (mx * sum(w.values())))


def gates(meta, cfg=None):
    cfg = cfg or nl.config()
    s, g, fl = meta.get("scores") or {}, cfg["gates"], cfg["floors"]
    fails = []

    if (meta.get("evidence_tier") or 9) > g.get("max_evidence_tier", 2):
        fails.append("no Tier 1/2 evidence")
    if (meta.get("source_count") or 0) < g.get("min_sources", 2):
        fails.append(f"fewer than {g.get('min_sources', 2)} sources")
    if g.get("require_buyer_role", True) and not meta.get("buyer_role"):
        fails.append("no named buyer role")
    if meta.get("persistence") not in g.get("eligible_persistence", []):
        fails.append(f"persistence={meta.get('persistence')!r} not eligible")

    de, ceil_ = deal_economics(meta, cfg)
    de_floor = fl.get("deal_economics", 0)
    if de_floor and de < de_floor:
        if ceil_ is None:
            fails.append("revenue ceiling undetermined — needs a sourced buyer count and a "
                         "plausible annual price before it can be judged")
        else:
            need = min((v for v, b in cfg["ceiling_bands"] if b >= de_floor), default=None)
            need_s = f"${need:,.0f}" if need is not None else f"band {de_floor}"
            fails.append(f"revenue ceiling ~${ceil_:,.0f}/yr is below the {need_s} floor")

    for dim in ("tractability", "replicability"):
        floor_ = fl.get(dim, 0)
        if floor_ and dim in s and int(s[dim]) < floor_:
            why = ("no usable integration surface, so software cannot absorb this"
                   if dim == "tractability" else
                   "every customer is a bespoke build, so this cannot be stacked")
            fails.append(f"{dim}={s[dim]} below floor {floor_} — {why}")

    missing = [k for k in cfg["weights"] if k not in s and k not in DERIVED]
    if missing:
        fails.append(f"missing scores: {sorted(missing)}")
    return fails


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug"); ap.add_argument("--all", action="store_true")
    ap.add_argument("--recompute", action="store_true")
    ap.add_argument("--dry-run", action="store_true", help="report without writing")
    a = ap.parse_args()
    cfg = nl.config()
    validate(cfg)
    print(f"profile: {cfg['profile']}  threshold: {cfg['threshold']}  floors: {cfg['floors']}\n")

    targets = ([(nl.IDEAS / f"{a.slug}.md",) + nl.read_idea(nl.IDEAS / f"{a.slug}.md")] if a.slug
               else nl.all_ideas())
    for path, meta, body in targets:
        s = dict(meta.get("scores") or {})
        de, ceil_ = deal_economics(meta, cfg)
        s["deal_economics"] = de
        meta["scores"] = s
        meta["revenue_ceiling_usd"] = ceil_
        c = composite(s, cfg)
        meta["composite"] = c
        f = gates(meta, cfg)
        meta["gate_pass"] = not f
        meta["scored_profile"] = cfg["profile"]
        if not a.dry_run:
            nl.write_idea(path, meta, body)
        verdict = "PROMOTE-ELIGIBLE" if (not f and c >= cfg["threshold"]) else "DEMOTE"
        ceil_str = f"${ceil_:,.0f}/yr" if ceil_ else "ceiling=?"
        print(f"{path.name}: {c}/100 {ceil_str} -> {verdict}")
        for x in f:
            print(f"    gate fail: {x}")


if __name__ == "__main__":
    main()
