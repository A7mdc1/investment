"""shariah.py — Shariah pre-screen.

Two layers:
  1. Surfaces the verdict you recorded from Zoya/Musaffa + flags when it's stale.
  2. A *rough* financial-ratio pre-check (AAOIFI-style) computed from yfinance,
     so you get an early warning before re-screening in Zoya/Musaffa.

IMPORTANT: this is NOT a substitute for Zoya/Musaffa. The business-activity
screen and non-compliant-income (<5%) test need their data; treat ratios here
as a heads-up only. Thresholds default to 33% (configurable).
"""
from __future__ import annotations
import datetime as dt
import json
import sys
import yfinance as yf
from common import load_holdings

DEBT_MAX = 0.33          # interest-bearing debt / market cap
LIQUID_MAX = 0.33        # (cash + short-term investments) / market cap
STALE_DAYS = 100         # re-screen if recorded verdict older than ~1 quarter

# Business-activity knockout — sectors/industries whose CORE business fails the
# Shariah screen before any ratio math. Substring match (lowercased) against
# yfinance's sector/industry strings. Conservative: catches the unambiguous
# hard-fails (conventional finance, alcohol, tobacco, gambling, adult, defense
# primes, cannabis). Everything else still needs Zoya/Musaffa for the revenue
# breakdown — this list only stops obvious non-compliants from ranking at all.
HARAM_SECTOR_TERMS = ("financial services", "financial data",)
HARAM_INDUSTRY_TERMS = (
    "bank", "insurance", "capital markets", "credit services",
    "mortgage", "asset management", "financial conglomerates",
    "alcoholic", "brewer", "distiller", "winer",
    "tobacco", "gambling", "casino",
    "aerospace & defense", "adult", "cannabis", "drug manufacturers - specialty & generic cannabis",
)


def business_precheck(ticker: str, info: dict | None = None) -> dict:
    """Core-business knockout from sector/industry metadata. Returns
    {"ok": bool|None, "flags": [...], "sector": ..., "industry": ...}.
    ok=None when metadata is unavailable (unknown, NOT a pass)."""
    try:
        if info is None:
            info = yf.Ticker(ticker).info or {}
        sector = (info.get("sector") or "").strip()
        industry = (info.get("industry") or "").strip()
        if not sector and not industry:
            return {"ok": None, "flags": [], "sector": None, "industry": None,
                    "note": "no sector/industry metadata"}
        flags = []
        sec_l, ind_l = sector.lower(), industry.lower()
        for term in HARAM_INDUSTRY_TERMS:
            if term in ind_l:
                flags.append(f"industry '{industry}' matches '{term}' — core business fails screen")
                break
        if not flags:
            for term in HARAM_SECTOR_TERMS:
                if term in sec_l:
                    flags.append(f"sector '{sector}' — conventional finance, core business fails screen")
                    break
        return {"ok": not flags, "flags": flags, "sector": sector, "industry": industry}
    except Exception as e:
        print(f"[warn] business precheck failed for {ticker}: {e}", file=sys.stderr)
        return {"ok": None, "flags": [], "sector": None, "industry": None, "note": str(e)}


def ratio_precheck(ticker: str) -> dict:
    """Business-activity knockout FIRST, then AAOIFI-style ratio heads-up.

    Missing balance-sheet rows are UNKNOWN, never 0.0 — the old default let
    banks (whose yfinance layouts often lack 'Total Debt' rows) compute
    debt=0 and sail through 'clean'."""
    try:
        t = yf.Ticker(ticker)

        biz = business_precheck(ticker)
        if biz.get("ok") is False:
            return {"ok": False, "flags": biz["flags"],
                    "sector": biz.get("sector"), "industry": biz.get("industry")}

        mcap = t.fast_info.get("marketCap")
        bs = t.balance_sheet
        def row(*names):
            """First present, non-NaN row among candidates; None if all missing."""
            for n in names:
                if n in bs.index:
                    v = float(bs.loc[n].iloc[0])
                    if v == v:  # skip NaN, try the next candidate name
                        return v
            return None
        # 'Total Debt' already includes current debt — only sum the components
        # when Total Debt itself is missing (the old code double-counted).
        debt = row("Total Debt")
        if debt is None:
            ltd = row("Long Term Debt")
            cur = row("Current Debt", "Short Long Term Debt")
            debt = (ltd or 0.0) + (cur or 0.0) if (ltd is not None or cur is not None) else None
        cash = row("Cash Cash Equivalents And Short Term Investments",
                   "Cash And Cash Equivalents")
        if not mcap:
            return {"ok": None, "note": "no market cap", "business_ok": biz.get("ok")}
        if debt is None and cash is None:
            return {"ok": None, "note": "no debt/cash rows in balance sheet — ratios unknown",
                    "business_ok": biz.get("ok")}
        flags = []
        debt_r = debt / mcap if debt is not None else None
        liq_r = cash / mcap if cash is not None else None
        if debt_r is not None and debt_r > DEBT_MAX:
            flags.append(f"debt/mcap {debt_r:.0%} > {DEBT_MAX:.0%}")
        if liq_r is not None and liq_r > LIQUID_MAX:
            flags.append(f"liquid/mcap {liq_r:.0%} > {LIQUID_MAX:.0%}")
        out = {"ok": not flags, "flags": flags, "business_ok": biz.get("ok")}
        if debt_r is not None: out["debt_ratio"] = round(debt_r, 3)
        else: out["debt_ratio_note"] = "no debt rows — unknown, verify in Zoya/Musaffa"
        if liq_r is not None: out["liquid_ratio"] = round(liq_r, 3)
        return out
    except Exception as e:
        print(f"[warn] ratio precheck failed for {ticker}: {e}", file=sys.stderr)
        return {"ok": None, "note": str(e)}


def main() -> None:
    today = dt.date.today()
    out = []
    for h in load_holdings():
        m = h["meta"]
        s = m.get("shariah", {}) or {}
        screened = s.get("screened")
        stale = None
        if screened:
            d = screened if isinstance(screened, dt.date) else dt.date.fromisoformat(str(screened))
            stale = (today - d).days > STALE_DAYS
        out.append({
            "ticker": m["ticker"], "name": m.get("name", m["ticker"]),
            "recorded_status": s.get("status", "unknown"),
            "source": s.get("source", "—"),
            "screened": str(screened) if screened else None,
            "stale": stale,
            "ratio_precheck": ratio_precheck(m["ticker"]),
        })
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
