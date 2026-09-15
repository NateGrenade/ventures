#!/usr/bin/env python3
"""Fetch every cited URL in an idea file, confirm it resolves, and compute evidence_tier.

Catches the two failure modes that corrupt everything downstream: hallucinated URLs, and
inflated source typing. Unreachable citations are marked [UNREACHABLE] in place rather than
deleted, so the claim is visibly unsupported instead of silently disappearing.
"""
import argparse, re, sys, urllib.request, urllib.error
import nichelib as nl

TIER = {"job-posting":1,"practitioner":1,"regulatory":1,"procurement":1,
        "trade-press":2,"study":2,"conference":2,
        "vendor":3,"analyst":3,"listicle":3}
URL_RE = re.compile(r"https?://[^\s)\]<>\"]+")
TYPE_RE = re.compile(r"\[type:\s*([a-z-]+)\s*\]")
UA = {"User-Agent": "niche-hunt/1.0 (research; contact via repo)"}

def reachable(url, timeout=12):
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, headers=UA, method=method)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return 200 <= r.status < 400
        except urllib.error.HTTPError as e:
            if e.code in (403, 405, 429):   # blocked, not absent
                return True
        except Exception:
            continue
    return False

def process(path, meta, body, offline=False):
    lines, bad = body.split("\n"), 0
    for i, line in enumerate(lines):
        for url in URL_RE.findall(line):
            if offline or reachable(url):
                continue
            lines[i] = line.replace(url, f"{url} [UNREACHABLE]"); bad += 1
    body = "\n".join(lines)
    types = [t for t in TYPE_RE.findall(body) if t in TIER]
    unknown = [t for t in TYPE_RE.findall(body) if t not in TIER]
    supported = [TIER[t] for t in types]
    meta["evidence_tier"] = min(supported) if supported else None
    meta["source_count"] = len(types)
    return meta, body, bad, unknown

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug"); ap.add_argument("--unverified-only", action="store_true")
    ap.add_argument("--offline", action="store_true", help="skip network, retier only")
    a = ap.parse_args()
    targets = ([ (nl.IDEAS / f"{a.slug}.md",) + nl.read_idea(nl.IDEAS / f"{a.slug}.md") ] if a.slug
               else [t for t in nl.all_ideas()
                     if not a.unverified_only or t[1].get("evidence_tier") is None])
    for path, meta, body in targets:
        meta, body, bad, unknown = process(path, meta, body, a.offline)
        nl.write_idea(path, meta, body)
        note = f"tier={meta['evidence_tier']} sources={meta['source_count']} unreachable={bad}"
        if unknown: note += f" UNKNOWN_TYPES={unknown}"
        if meta["evidence_tier"] is None: note += "  <- NO TYPED SOURCES, will fail triage"
        print(f"{path.name}: {note}")

if __name__ == "__main__":
    main()
