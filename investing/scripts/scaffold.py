"""scaffold.py — auto-fill a setup card from Yahoo-derived data (Change 8).

The scaffold FILLS a card completely from formula outputs — levels, logic text,
plan — so the assessment report can present complete PROPOSED trade plans. The
human step is a REVIEW-AND-APPROVE flip, not blank-field authorship: read the
plan, do your own research, edit what you disagree with, and set status: planned.

Two non-negotiable invariants:
  1. A machine-filled card is written `status: draft` and can NEVER reach
     BUY-CANDIDATE — evaluate_setup caps a draft at RESEARCH until you approve.
  2. The scaffold NEVER writes `shariah.status: compliant`. Only a human
     Zoya/Musaffa screen sets that; here it is ALWAYS `unverified`.

CLI:
  python scripts/scaffold.py TICKER [--setup-type breakout|pullback|earnings_run] [--force]
  python scripts/scaffold.py --all-leads [--force]     # scaffold every LEAD in leads.md

Degrades gracefully: missing data -> null + a `# scaffold: <field> unavailable`
comment. Never crashes, never invents numbers. Refuses to overwrite a card
without --force.
"""
from __future__ import annotations
import argparse
import datetime as dt
import os
import re
import sys

import technicals
import shariah
import discover  # fetch_catalyst_date; leads path/parsing
from common import fetch_mcap, passes_liquidity, SETUPS_DIR
from recommend import catalyst_days_out, load_cfg

HERE = os.path.dirname(__file__)


def _f(x, nd=2):
    """Format a number to nd decimals, or '?' if None."""
    return f"{x:.{nd}f}" if isinstance(x, (int, float)) else "?"


def pick_setup_type(tech: dict | None, cat_days, cfg: dict) -> str:
    """Heuristic: earnings soon -> earnings_run; near the 52w high -> breakout;
    otherwise -> pullback."""
    horizon = int(cfg.get("catalyst_horizon_days", 60))
    if cat_days is not None and 0 <= cat_days <= horizon:
        return "earnings_run"
    dist = (tech or {}).get("dist_52w_high_pct")
    if dist is not None and dist >= -5:      # within 5% of the 52-week high
        return "breakout"
    return "pullback"


def _levels(tech: dict | None, cfg: dict, setup_type: str) -> dict:
    """Derive entry/stop/target levels from technicals. Any may be None."""
    t = tech or {}
    price, atr = t.get("price"), t.get("atr")
    ema20, chand = t.get("ema_fast"), t.get("chandelier_stop")
    dist = t.get("dist_52w_high_pct")
    mult = float(cfg.get("atr_stop_mult", 3.0))
    t1_r, t2_r = float(cfg.get("t1_r", 1.5)), float(cfg.get("t2_r", 3.0))

    hi52 = price / (1 + dist / 100) if (price is not None and dist is not None) else None
    hh22 = (chand + mult * atr) if (chand is not None and atr is not None) else None
    entry = {"breakout": hi52, "pullback": ema20, "earnings_run": price}.get(setup_type)
    stop = chand
    R = (entry - stop) if (entry is not None and stop is not None and entry > stop) else None
    t1 = (entry + t1_r * R) if R else None
    t2 = (entry + t2_r * R) if R else None
    return {"price": price, "atr": atr, "ema20": ema20, "chandelier": stop, "hi52": hi52,
            "hh22": hh22, "mult": mult, "t1_r": t1_r, "t2_r": t2_r,
            "entry": entry, "stop": stop, "R": R, "t1": t1, "t2": t2}


def _shariah_comment(precheck: dict) -> str:
    if precheck.get("ok") is False:
        return "# pre-check FLAGGED: " + "; ".join(precheck.get("flags", []) or ["ratio/business flag"])
    if precheck.get("ok") is True:
        return "# pre-check: business OK, ratios OK — verify in Zoya/Musaffa"
    # Inconclusive: keep the note short and single-line (raw network errors are noisy).
    note = str(precheck.get("note", "no data")).splitlines()[0][:50]
    if "curl" in note.lower() or "403" in note or "perform" in note.lower():
        note = "data unavailable"
    return f"# pre-check inconclusive ({note}) — verify in Zoya/Musaffa"


def _q(text: str) -> str:
    """YAML double-quote a string value (escape embedded double quotes)."""
    return '"' + str(text).replace('"', "'") + '"'


def render_card(ticker: str, tech: dict | None, earnings_iso: str | None,
                liquidity: dict, precheck: dict, cfg: dict, setup_type: str,
                today: dt.date) -> str:
    """Pure: build the full setups/<ticker>.md text from fetched inputs. Every
    level is a formula output; missing inputs become null + a comment."""
    L = _levels(tech, cfg, setup_type)
    cat_days = catalyst_days_out(earnings_iso, today) if earnings_iso else None
    window = int(cfg.get(f"duration_days_{setup_type}", cfg.get("duration_days_swing", 21)))
    entry, stop = L["entry"], L["stop"]

    # entry_trigger / entry_price
    if entry is None:
        entry_price = "null"
        entry_trigger = ('null            # scaffold: entry level unavailable (no price/EMA/52w data)')
    else:
        entry_price = _f(entry)
        if setup_type == "breakout":
            trig = f"close above ${_f(L['hi52'])} (52w high) on >1.2x 20d avg volume"
        elif setup_type == "pullback":
            trig = f"pullback to EMA20 ${_f(L['ema20'])} holding the uptrend (no breakdown on volume)"
        else:  # earnings_run
            trig = f"enter near ${_f(L['price'])} ahead of the {earnings_iso or 'next'} print"
        entry_trigger = _q(trig)

    # stop_price / stop_logic
    if stop is None:
        stop_price, stop_logic = "null", 'null             # scaffold: chandelier stop unavailable'
    else:
        stop_price = _f(stop)
        if L["hh22"] is not None and L["atr"] is not None:
            sl = (f"chandelier trail: HH22 ${_f(L['hh22'])} - {L['mult']:g}x ATR ${_f(L['atr'])} "
                  f"= ${_f(stop)} — exit when decline exceeds ~{L['mult']:g} average daily ranges")
        else:
            sl = f"chandelier trail at ${_f(stop)} (ATR band)"
        stop_logic = _q(sl)

    # target_price / target_logic
    if L["t1"] is None:
        target_price = "null"
        target_logic = 'null           # scaffold: target unavailable (needs entry>stop for R)'
    else:
        target_price = _f(L["t1"])
        tl = (f"T1 ${_f(L['t1'])} = entry ${_f(entry)} + {L['t1_r']:g}x R (R=${_f(L['R'])}); "
              f"T2 ${_f(L['t2'])} = entry + {L['t2_r']:g}x R; structure ceiling = 52w high ${_f(L['hi52'])}")
        target_logic = _q(tl)

    # catalyst + earnings_plan
    if earnings_iso and cat_days is not None and cat_days <= 90:
        catalyst = _q(f"{earnings_iso} earnings")
    else:
        catalyst = "null"
    earnings_in_window = cat_days is not None and 0 <= cat_days <= window
    if earnings_in_window:
        earnings_plan = ("exit_before   # machine default — change to hold_through_sized_down ONLY "
                         "deliberately; sizing then uses the 25% gap assumption")
    else:
        earnings_plan = "no_earnings_in_window"

    # liquidity_check
    adv, liq_ok = liquidity.get("avg_dollar_vol"), liquidity.get("ok")
    min_adv = float(cfg.get("screen_min_avg_dollar_vol", 5e6))
    if adv is None:
        liquidity_check = 'null      # scaffold: avg $ volume unavailable'
    else:
        verdict = "pass" if liq_ok else f"FAIL (< ${min_adv/1e6:.0f}M floor)"
        liquidity_check = _q(f"avg $vol ${adv/1e6:.1f}M; {verdict}")

    # invalidation
    if entry is None:
        invalidation = 'null           # scaffold: needs entry level'
    elif setup_type == "breakout":
        invalidation = _q(f"closes back below the breakout level ${_f(entry)} within 2 sessions, "
                          f"or breakout volume < 1.2x average")
    elif setup_type == "pullback":
        invalidation = _q(f"loses EMA20 ${_f(entry)} on rising volume")
    else:  # earnings_run
        invalidation = _q(f"no positive drift 5 sessions pre-print / gives back >1 ATR (${_f(L['atr'])})")

    sh_comment = _shariah_comment(precheck)

    lines = [
        "---",
        f"ticker: {ticker.upper()}",
        "status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve",
        f"setup_type: {setup_type}",
        f"entry_trigger: {entry_trigger}",
        f"entry_price: {entry_price}",
        f"stop_price: {stop_price}",
        f"stop_logic: {stop_logic}",
        f"target_price: {target_price}",
        f"target_logic: {target_logic}",
        f"holding_window_days: {window}",
        f"catalyst: {catalyst}",
        f"earnings_plan: {earnings_plan}",
        f"liquidity_check: {liquidity_check}",
        f"invalidation: {invalidation}",
        "shariah:",
        "  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant",
        "  source: null",
        f"  screened: null         {sh_comment}",
        "---",
        "",
        "## Notes",
        f"Scaffolded {today} from Yahoo data — every level is a formula output. Edit anything",
        "you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until",
        "you screen it in Zoya/Musaffa and record the result above.",
        "",
    ]
    return "\n".join(lines)


# ------------------------------------------------------------------ orchestration

def gather(ticker: str, cfg: dict, today: dt.date) -> dict:
    """Fetch everything once for a ticker. Offline-safe (fields degrade to None)."""
    tech = technicals.fetch(ticker, cfg)
    earnings_iso = discover.fetch_catalyst_date(ticker, today)
    adv = (tech or {}).get("avg_dollar_vol")
    mcap = fetch_mcap(ticker)
    liq_ok, _ = passes_liquidity(mcap, adv, cfg)
    liquidity = {"avg_dollar_vol": adv, "mcap": mcap, "ok": liq_ok}
    precheck = shariah.ratio_precheck(ticker)
    return {"tech": tech, "earnings_iso": earnings_iso, "liquidity": liquidity, "precheck": precheck}


def scaffold_one(ticker: str, cfg: dict, today: dt.date, setup_type: str | None,
                 force: bool, setups_dir: str = SETUPS_DIR) -> tuple[bool, str]:
    """Write setups/<ticker>.md. Returns (written, message)."""
    path = os.path.join(setups_dir, f"{ticker.lower()}.md")
    if os.path.exists(path) and not force:
        return False, f"{ticker}: card exists — use --force to overwrite (unchanged)"
    data = gather(ticker, cfg, today)
    cat_days = catalyst_days_out(data["earnings_iso"], today) if data["earnings_iso"] else None
    st = setup_type or pick_setup_type(data["tech"], cat_days, cfg)
    card = render_card(ticker, data["tech"], data["earnings_iso"], data["liquidity"],
                       data["precheck"], cfg, st, today)
    os.makedirs(setups_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(card)
    return True, f"{ticker}: scaffolded DRAFT ({st}) -> setups/{ticker.lower()}.md"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("ticker", nargs="?", help="ticker to scaffold (omit with --all-leads)")
    ap.add_argument("--setup-type", dest="setup_type", default=None,
                    choices=["breakout", "pullback", "earnings_run", "post_earnings_drift", "other"])
    ap.add_argument("--all-leads", dest="all_leads", action="store_true",
                    help="scaffold every LEAD ticker in leads.md (skips existing cards)")
    ap.add_argument("--force", action="store_true", help="overwrite an existing card")
    a = ap.parse_args()
    cfg = load_cfg()
    today = dt.date.today()

    if a.all_leads:
        tickers = _leads_tickers()
        if not tickers:
            print("no leads.md tickers found — run discover.py first (needs live Yahoo).")
            return
        for tk in tickers:
            _, msg = scaffold_one(tk, cfg, today, a.setup_type, a.force)
            print(msg)
        return

    if not a.ticker:
        ap.error("provide a TICKER or use --all-leads")
    _, msg = scaffold_one(a.ticker, cfg, today, a.setup_type, a.force)
    print(msg)


def _leads_tickers(path: str | None = None) -> list[str]:
    """Parse LEAD tickers out of leads.md (first column of each data row)."""
    path = path or discover.LEADS
    out = []
    if not os.path.exists(path):
        return out
    for line in open(path, encoding="utf-8"):
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        parts = [p.strip() for p in s.split("|")]
        if re.fullmatch(r"[A-Za-z][A-Za-z.\-]{0,9}", parts[0]):
            out.append(parts[0].upper())
    return out


if __name__ == "__main__":
    main()
