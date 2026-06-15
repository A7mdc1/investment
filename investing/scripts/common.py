"""Shared helpers: read holding .md files (YAML front-matter + free-text thesis)."""
from __future__ import annotations
import glob
import os
import yaml

HOLDINGS_DIR = os.path.join(os.path.dirname(__file__), "..", "holdings")


def parse_holding(path: str) -> dict:
    """Return {'meta': <front-matter dict>, 'thesis': <markdown body>, 'path': path}."""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    meta, body = {}, text
    if text.startswith("---"):
        _, fm, body = text.split("---", 2)
        meta = yaml.safe_load(fm) or {}
    return {"meta": meta, "thesis": body.strip(), "path": path}


def load_holdings() -> list[dict]:
    """Load every holding except files starting with '_' (templates)."""
    out = []
    for p in sorted(glob.glob(os.path.join(HOLDINGS_DIR, "*.md"))):
        if os.path.basename(p).startswith("_"):
            continue
        h = parse_holding(p)
        if h["meta"].get("ticker"):
            out.append(h)
    return out
