"""Shared helpers: read holding .md files (YAML front-matter + free-text thesis)."""
from __future__ import annotations
import glob
import os
import yaml

# yfinance's default curl_cffi impersonation ("chrome" -> latest fingerprint)
# gets connection-reset by Yahoo's anti-bot layer; chrome110 still works.
# Each yfinance submodule does `from ._http import new_session` at its own
# import time, so patching yfinance._http alone doesn't reach those already-
# bound references -- every module holding one must be repatched directly.
def _yf_session_workaround():
    from curl_cffi import requests as _backend
    return _backend.Session(impersonate="chrome110")


def _patch_yfinance_session():
    import yfinance._http as _http
    import yfinance.base as _base
    import yfinance.data as _data
    import yfinance.multi as _multi
    import yfinance.scrapers.history as _history

    for module in (_http, _base, _data, _multi, _history):
        module.new_session = _yf_session_workaround


_patch_yfinance_session()

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
