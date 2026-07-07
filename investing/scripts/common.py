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
SETUPS_DIR = os.path.join(os.path.dirname(__file__), "..", "setups")


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


def load_setups(setups_dir: str = SETUPS_DIR) -> list[dict]:
    """Load every pre-trade setup card except files starting with '_' (templates).

    A setup card is the swing-trade analogue of a holding's thesis: YAML
    front-matter (ticker, status, setup_type, entry/stop/target logic, earnings
    plan, invalidation, shariah) plus free-text notes. Same shape as
    parse_holding, so downstream code reads {'meta', 'thesis', 'path'}."""
    out = []
    if not os.path.isdir(setups_dir):
        return out
    for p in sorted(glob.glob(os.path.join(setups_dir, "*.md"))):
        name = os.path.basename(p)
        if name.startswith("_") or name.upper() == "README.MD":
            continue
        h = parse_holding(p)
        if h["meta"].get("ticker"):
            out.append(h)
    return out


def setups_by_ticker(setups_dir: str = SETUPS_DIR) -> dict:
    """Map UPPER(ticker) -> setup card dict, for O(1) lookup by ticker."""
    return {str(s["meta"]["ticker"]).upper(): s for s in load_setups(setups_dir)}


# ---- liquidity helpers (shared by discover.py and scaffold.py) ---------------
import sys as _sys


def fetch_mcap(ticker: str):
    """Market cap via fast_info, best-effort. None on any failure."""
    try:
        import yfinance as yf
        return yf.Ticker(ticker).fast_info.get("marketCap")
    except Exception as e:
        print(f"[warn] mcap {ticker}: {e}", file=_sys.stderr)
        return None


def passes_liquidity(mcap, avg_dollar_vol, cfg: dict):
    """Liquidity floor: illiquidity is untradeable 'reward'. A KNOWN value below
    a floor drops the lead; missing data (None) does not drop (unknown != fail).
    Returns (ok: bool, reason: str)."""
    min_mcap = float(cfg.get("screen_min_mcap", 500e6))
    min_adv = float(cfg.get("screen_min_avg_dollar_vol", 5e6))
    if mcap is not None and mcap < min_mcap:
        return False, f"mcap ${mcap/1e6:.0f}M < ${min_mcap/1e6:.0f}M floor"
    if avg_dollar_vol is not None and avg_dollar_vol < min_adv:
        return False, f"avg $vol ${avg_dollar_vol/1e6:.1f}M < ${min_adv/1e6:.0f}M floor"
    return True, ""
