#!/usr/bin/env python3
"""Fetch every cited URL in an idea file, confirm it resolves, and compute evidence_tier.

Catches the two failure modes that corrupt everything downstream: hallucinated URLs, and
inflated source typing. Unreachable citations are marked [UNREACHABLE] in place rather than
deleted, so the claim is visibly unsupported instead of silently disappearing.
"""
import argparse, re, socket, ssl, sys, urllib.request, urllib.error
import nichelib as nl

TIER = {"job-posting":1,"practitioner":1,"regulatory":1,"procurement":1,
        "trade-press":2,"study":2,"conference":2,
        "vendor":3,"analyst":3,"listicle":3}
URL_RE = re.compile(r"https?://[^\s)\]<>\"]+")
TYPE_RE = re.compile(r"\[type:\s*([a-z-]+)\s*\]")
UA = {"User-Agent": "niche-hunt/1.0 (research; contact via repo)"}

class EnvironmentBroken(Exception):
    """Raised when failures look like a local misconfiguration rather than dead links."""


def reachable(url, timeout=12):
    """Returns (ok, env_fault). env_fault flags errors that indicate a broken local
    environment — expired CA bundle, no DNS, proxy refusing — rather than a dead URL."""
    last_env_fault = False
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, headers=UA, method=method)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return 200 <= r.status < 400, False
        except urllib.error.HTTPError as e:
            if e.code in (403, 405, 429):   # blocked, not absent
                return True, False
        except ssl.SSLError:
            last_env_fault = True           # almost always a stale CA bundle
        except urllib.error.URLError as e:
            if isinstance(getattr(e, "reason", None), (ssl.SSLError, socket.gaierror)):
                last_env_fault = True
        except Exception:
            continue
    return False, last_env_fault

def process(path, meta, body, offline=False):
    lines, bad, checked, env_faults = body.split("\n"), 0, 0, 0
    for i, line in enumerate(lines):
        for url in URL_RE.findall(line):
            if offline:
                continue
            checked += 1
            ok, env_fault = reachable(url)
            if ok:
                continue
            if env_fault:
                env_faults += 1
            lines[i] = line.replace(url, f"{url} [UNREACHABLE]"); bad += 1

    # A local misconfiguration fails every URL at once. Writing that result would strip
    # good citations from the whole corpus, so refuse rather than record it.
    if checked >= 3 and (env_faults / checked) > 0.5:
        raise EnvironmentBroken(
            f"{env_faults}/{checked} URLs failed with TLS/DNS errors — this is a broken "
            f"local environment, not dead links. Nothing was written.\n"
            f"On macOS with python.org builds, run:\n"
            r"  /Applications/Python 3.x/Install Certificates.command" "\n"
            f"Then re-run. Use --offline to retier without network checks.")
    if checked >= 3 and bad == checked:
        raise EnvironmentBroken(
            f"All {checked} URLs failed. That is more likely an environment or network "
            f"problem than {checked} simultaneously dead links. Nothing was written.")
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
        try:
            meta, body, bad, unknown = process(path, meta, body, a.offline)
        except EnvironmentBroken as e:
            sys.exit(f"ABORTED on {path.name}:\n{e}")
        nl.write_idea(path, meta, body)
        note = f"tier={meta['evidence_tier']} sources={meta['source_count']} unreachable={bad}"
        if unknown: note += f" UNKNOWN_TYPES={unknown}"
        if meta["evidence_tier"] is None: note += "  <- NO TYPED SOURCES, will fail triage"
        print(f"{path.name}: {note}")

if __name__ == "__main__":
    main()
