"""Shared helpers for the niche-hunt pipeline. Deterministic work lives here, not in model context."""
import json, os, re, sys, datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required:  pip install pyyaml")

def repo_root(start=None):
    p = Path(start or os.getcwd()).resolve()
    for cand in [p, *p.parents]:
        if (cand / "frontier").is_dir() and (cand / "ideas").is_dir():
            return cand
    return p

ROOT = repo_root()
IDEAS = ROOT / "ideas"
FRONTIER = ROOT / "frontier"
CALIB = ROOT / "calibration"

FM_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.S)

def read_idea(path):
    raw = Path(path).read_text(encoding="utf-8")
    m = FM_RE.match(raw)
    if not m:
        raise ValueError(f"{path}: missing or malformed frontmatter")
    return yaml.safe_load(m.group(1)) or {}, m.group(2)

def write_idea(path, meta, body):
    fm = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True).strip()
    Path(path).write_text(f"---\n{fm}\n---\n{body}", encoding="utf-8")

def all_ideas(status=None):
    out = []
    for f in sorted(IDEAS.glob("*.md")):
        try:
            meta, body = read_idea(f)
        except ValueError as e:
            print(f"WARN {e}", file=sys.stderr); continue
        if status and meta.get("status") != status:
            continue
        out.append((f, meta, body))
    return out

def jsonl(path):
    p = Path(path)
    if not p.exists(): return []
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]

def jsonl_append(path, rec):
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")

def today():
    return datetime.date.today().isoformat()

STOP = set("the a an of for and or to in on with by is are that this it as at from".split())

def tokens(text):
    return {w for w in re.findall(r"[a-z0-9]+", (text or "").lower()) if w not in STOP and len(w) > 2}

def jaccard(a, b):
    if not a or not b: return 0.0
    return len(a & b) / len(a | b)

def overlap(a, b):
    """Containment coefficient. Use when comparing a short probe against a long document —
    Jaccard punishes the size asymmetry and misses real duplicates."""
    if not a or not b: return 0.0
    return len(a & b) / min(len(a), len(b))
