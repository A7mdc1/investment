"""discover.py — auto-discover candidate ideas, refresh watchlist.md.

Each run (local; needs live Yahoo data) builds a candidate POOL automatically,
runs the PM decision-logic pipeline over it, and writes the top-N by "max
benefit" into watchlist.md so recommend.py / the report ingest them — no manual
curation. This is the deliberate exception to the repo's "never invent tickers"
rule, scoped to discovery; every downstream gate and the "verify in Zoya/Musaffa
+ not advice" rails stay intact.

Pipeline (decision-logic doc, in order):
  1. Pool  = merge(halal-ETF holdings, yfinance screener results), deduped.
  2. Shariah knockout FIRST — ratio_precheck; a ratio FLAG (ok is False) is an
     absolute AVOID and is dropped from the shortlist. Clean/unknown stay
     UNVERIFIED (business screen still needs Zoya/Musaffa).
  3. Technicals (price/ATR/EMA/momentum/52w/chandelier) via technicals.fetch.
  4. Catalyst — next earnings date via yfinance, auto-filling the CATALYST_GATE.
  5. Asymmetry — reward:risk from a technical target/stop.
  6. Verdict — BUY-CANDIDATE on mechanics alone (clean ratios + reward:risk >=
     floor + catalyst within horizon); else RESEARCH; ratio-flagged -> AVOID.
     EDGE is ALWAYS flagged NOT SUPPLIED: a mechanical BUY-CANDIDATE is never
     dressed up as an edge-backed conviction call — that variant view is yours.
  7. Max-benefit rank -> keep top discover_top_n (asymmetry-led composite).

All knobs live in rules.md. Network failures degrade gracefully (skip + warn),
never fabricate.
"""
from __future__ import annotations
import datetime as dt
import json
import os
import re
import sys

import recommend
import screener
import shariah
import technicals

HERE = os.path.dirname(__file__)
WATCHLIST = os.path.join(HERE, "..", "watchlist.md")
TICKER_RE = re.compile(r"[A-Za-z][A-Za-z.\-]{0,9}")


def load_cfg() -> dict:
    return screener.load_cfg()


# ---------------------------------------------------------------- pool building

def _valid(tk) -> bool:
    return bool(tk) and bool(TICKER_RE.fullmatch(str(tk)))


def _extract_symbols(res) -> list[str]:
    """Pull tickers out of yf.screen()'s result (dict-of-quotes or DataFrame)."""
    syms: list[str] = []
    try:
        if isinstance(res, dict):
            for q in (res.get("quotes") or res.get("records") or []):
                s = q.get("symbol") or q.get("ticker") if isinstance(q, dict) else None
                if s:
                    syms.append(str(s).upper())
        elif hasattr(res, "columns"):  # pandas DataFrame
            for col in ("symbol", "ticker", "Symbol", "Ticker"):
                if col in res.columns:
                    syms = [str(x).upper() for x in res[col].tolist()]
                    break
            else:
                syms = [str(x).upper() for x in res.index.tolist()]
    except Exception as e:
        print(f"[warn] extract symbols: {e}", file=sys.stderr)
    return syms


def _screen_tickers(name: str, count: int) -> list[str]:
    try:
        import yfinance as yf
        return _extract_symbols(yf.screen(name, count=count))
    except Exception as e:
        print(f"[warn] screen '{name}': {e}", file=sys.stderr)
        return []


def _etf_holdings(etf: str) -> list[str]:
    """Constituent symbols of an ETF (e.g. a halal ETF like SPUS) — pre-screened
    for business activity by the fund, so a Shariah-friendlier base than a raw
    screener. Defensive across yfinance funds_data shapes."""
    syms: list[str] = []
    try:
        import yfinance as yf
        fd = yf.Ticker(etf).funds_data
        for obj in (getattr(fd, "top_holdings", None), getattr(fd, "equity_holdings", None)):
            if obj is None:
                continue
            if hasattr(obj, "index"):           # DataFrame keyed by symbol
                syms += [str(x).upper() for x in obj.index.tolist()]
            elif isinstance(obj, (list, tuple)):
                syms += [str(x).upper() for x in obj]
    except Exception as e:
        print(f"[warn] etf holdings '{etf}': {e}", file=sys.stderr)
    return syms


def discover_pool(cfg: dict) -> list[tuple[str, str]]:
    """Merge halal-ETF holdings + yfinance screens, deduped. -> [(ticker, source)]."""
    etfs = cfg.get("discover_etfs") or ["SPUS"]
    screens = cfg.get("discover_screens") or [
        "growth_technology_stocks", "undervalued_large_caps", "most_actives"]
    count = int(cfg.get("discover_screen_count", 100))

    seen: set[str] = set()
    out: list[tuple[str, str]] = []
    for etf in etfs:
        for tk in _etf_holdings(etf):
            if _valid(tk) and tk not in seen:
                seen.add(tk)
                out.append((tk, f"{etf} holding"))
    for sc in screens:
        for tk in _screen_tickers(sc, count):
            if _valid(tk) and tk not in seen:
                seen.add(tk)
                out.append((tk, f"screen:{sc}"))
    return out


# ------------------------------------------------------------------- catalysts

def fetch_catalyst_date(ticker: str, today: dt.date) -> str | None:
    """Next earnings date (>= today) as ISO YYYY-MM-DD, best-effort."""
    try:
        import yfinance as yf
        df = yf.Ticker(ticker).get_earnings_dates(limit=12)
        if df is not None and len(df) > 0:
            for idx in sorted(df.index):
                d = idx.date() if hasattr(idx, "date") else None
                if d and d >= today:
                    return d.isoformat()
    except Exception as e:
        print(f"[warn] earnings date {ticker}: {e}", file=sys.stderr)
    try:
        import yfinance as yf
        cal = yf.Ticker(ticker).calendar or {}
        ed = cal.get("Earnings Date") if isinstance(cal, dict) else None
        if isinstance(ed, (list, tuple)) and ed:
            d = ed[0]
            d = d.date() if hasattr(d, "date") else d
            if isinstance(d, dt.date) and d >= today:
                return d.isoformat()
    except Exception:
        pass
    return None


# --------------------------------------------------------------------- verdict

def classify(pc_ok, rr, cat_days, horizon: int, rr_floor: float):
    """Choice 3B: BUY-CANDIDATE on mechanics alone; edge is flagged separately.
    A ratio FLAG is the only hard AVOID for a discovered idea."""
    if pc_ok is False:
        return "AVOID", "Shariah ratio pre-check FLAGGED — absolute exclusion (knockout)"
    cat_ok = cat_days is not None and 0 <= cat_days <= horizon
    rr_ok = rr is not None and rr >= rr_floor
    if rr_ok and cat_ok:
        return "BUY-CANDIDATE", (f"mechanical pass: reward:risk {rr:.1f}:1, catalyst {cat_days}d out "
                                 f"(EDGE NOT SUPPLIED — add your variant view)")
    reasons = []
    if not rr_ok:
        reasons.append(f"ASYMMETRY_GATE: reward:risk {f'{rr:.1f}:1' if rr is not None else 'n/a'} "
                       f"< {rr_floor:.1f}")
    if not cat_ok:
        reasons.append("CATALYST_GATE: no earnings date found" if cat_days is None
                       else f"CATALYST_GATE: catalyst {cat_days}d out > {horizon}d")
    return "RESEARCH", "; ".join(reasons)


def build_record(ticker, source, tech, pc, cat_iso, cat_days, score, cfg, horizon, rr_floor) -> dict:
    px = tech.get("price")
    target, stop = recommend.technical_target_stop(tech, px)
    rr = recommend.reward_risk(px, target, stop)
    verdict, why = classify(pc.get("ok"), rr, cat_days, horizon, rr_floor)
    if pc.get("ok") is True:
        sh_note = "ratio pre-check clean — confirm business screen in Zoya/Musaffa"
    else:
        sh_note = f"ratio pre-check unavailable ({pc.get('note', 'no data')}) — verify in Zoya/Musaffa"
    return {
        "ticker": ticker, "source": source, "verdict": verdict, "why": why,
        "score": score,
        "shariah_status": "UNVERIFIED", "shariah_note": sh_note,
        "edge": "NOT SUPPLIED — mechanical pass; add your variant view",
        "target_price": round(target, 2) if target is not None else None,
        "stop": round(stop, 2) if stop is not None else None,
        "reward_risk": round(rr, 2) if rr is not None else None,
        "catalyst_iso": cat_iso, "catalyst_days": cat_days,
        "time_horizon": "swing",
        "risk_per_trade_pct": cfg.get("risk_per_trade_pct"),
    }


# ------------------------------------------------------------- ranking + output

def rank_and_select(records: list[dict], cfg: dict) -> list[dict]:
    """Max-benefit composite: asymmetry-led, then signal score, then catalyst
    proximity. Returns the top discover_top_n."""
    w_rr = float(cfg.get("discover_w_rr", 0.5))
    w_sc = float(cfg.get("discover_w_score", 0.3))
    w_cat = float(cfg.get("discover_w_catalyst", 0.2))
    horizon = int(cfg.get("catalyst_horizon_days", 60))
    top_n = int(cfg.get("discover_top_n", 20))

    rr_n = screener._norm([r.get("reward_risk") for r in records])
    sc_n = screener._norm([r.get("score") for r in records])
    for i, r in enumerate(records):
        cd = r.get("catalyst_days")
        prox = 0.0 if cd is None or cd < 0 else max(0.0, 1 - cd / horizon)
        r["benefit"] = round(w_rr * rr_n[i] + w_sc * sc_n[i] + w_cat * prox, 4)
    records.sort(key=lambda r: r["benefit"], reverse=True)
    return records[:top_n]


def render_rows(records: list[dict]) -> list[str]:
    """`TICKER | why (auto note) | catalyst` — parseable by recommend.load_watchlist.
    The note must contain no '|' (the column delimiter)."""
    rows = []
    for r in records:
        cat = r.get("catalyst_iso")
        catcol = f"earnings {cat}" if cat else "no dated catalyst found"
        rr = f"{r['reward_risk']:.1f}:1" if r.get("reward_risk") is not None else "n/a"
        note = (f"auto ({r['source']}); {r['verdict']}; reward-risk {rr}; score {r.get('score')}; "
                f"EDGE: add your variant view; VERIFY Shariah in Zoya/Musaffa")
        rows.append(f"{r['ticker']} | {note} | {catcol}")
    return rows


def rewrite_watchlist_text(old_text: str, rows: list[str], today: dt.date) -> str:
    """Replace ONLY the '## Tickers to track' block; preserve header/themes/rules."""
    marker = "## Tickers to track"
    block = [
        marker,
        f"# AUTO-GENERATED by discover.py on {today} — top {len(rows)} by max-benefit rank.",
        "# Re-run discovery to refresh. Edit a `why` to add YOUR variant view; these are",
        "# leads to verify in Zoya/Musaffa, NOT buys. Shariah here is UNVERIFIED.",
        "# ticker | why (auto note — add your edge) | catalyst (dated)",
        *rows,
        "",
    ]
    lines = old_text.splitlines()
    start = next((i for i, l in enumerate(lines) if l.strip() == marker), None)
    if start is None:
        return old_text.rstrip() + "\n\n" + "\n".join(block) + "\n"
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if lines[j].startswith("## "):
            end = j
            break
    return "\n".join(lines[:start] + block + lines[end:]).rstrip() + "\n"


def write_watchlist(records: list[dict], today: dt.date, path: str = WATCHLIST) -> None:
    old = open(path, encoding="utf-8").read() if os.path.exists(path) else "# Watchlist\n"
    open(path, "w", encoding="utf-8").write(rewrite_watchlist_text(old, render_rows(records), today))


def main() -> None:
    cfg = load_cfg()
    today = dt.date.today()
    horizon = int(cfg.get("catalyst_horizon_days", 60))
    rr_floor = float(cfg.get("reward_risk_min_swing", 2.0))

    pool = discover_pool(cfg)
    print(f"[info] discovered pool: {len(pool)} names", file=sys.stderr)
    if not pool:
        print(json.dumps({"error": "empty pool — no data (needs live Yahoo access; "
                                    "blocked in sandboxes). Run locally.", "ideas": []}, indent=2))
        return

    rows = [{"ticker": tk, "tech": technicals.fetch(tk, cfg), "source": src} for tk, src in pool]
    scored = {s["ticker"]: s.get("score") for s in screener.score_universe(rows, cfg)}

    records, excluded, no_price = [], 0, 0
    for row in rows:
        tk, tech = row["ticker"], row["tech"]
        if not tech or tech.get("price") is None:
            no_price += 1
            continue
        pc = shariah.ratio_precheck(tk)
        if pc.get("ok") is False:
            excluded += 1
            continue
        cat_iso = fetch_catalyst_date(tk, today)
        cat_days = recommend.catalyst_days_out(cat_iso, today) if cat_iso else None
        records.append(build_record(tk, row["source"], tech, pc, cat_iso, cat_days,
                                    scored.get(tk), cfg, horizon, rr_floor))

    top = rank_and_select(records, cfg)
    write_watchlist(top, today)

    counts = {"BUY-CANDIDATE": 0, "RESEARCH": 0}
    for r in top:
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
    print(json.dumps({
        "generated": str(today),
        "pool_size": len(pool),
        "dropped_no_price": no_price,
        "excluded_shariah_ratio_flag": excluded,
        "selected": len(top),
        "verdict_counts": counts,
        "watchlist_written": os.path.abspath(WATCHLIST),
        "disclaimer": ("Auto-discovered LEADS, not buys or advice. Verdicts are mechanical: "
                       "EDGE is NOT supplied (your variant view is required), and Shariah is "
                       "UNVERIFIED — confirm every name in Zoya/Musaffa before any add."),
        "ideas": top,
    }, indent=2, default=str))


if __name__ == "__main__":
    main()
