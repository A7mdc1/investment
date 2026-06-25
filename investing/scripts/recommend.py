"""recommend.py — PM-grade recommendation engine.

Encodes the decision pipeline from the PM decision-logic note (see
docs/Portfolio_Manager_Decision_Logic...md): Shariah knockout -> edge/thesis
check -> asymmetry (reward:risk) gate -> catalyst-within-horizon gate ->
sizing. Emits ONE structured record per holding/watchlist idea (the schema
from that note's section 7), not a score or a tip.

What this automates: gate math (ratios, reward:risk, position sizing). What
it can NOT do: supply a genuine analytical edge, a true conviction call, or a
pre-mortem — those require YOUR variant view. Where that input is missing the
engine says so plainly and caps the verdict at RESEARCH rather than faking it.

Holdings -> SELL | TRIM | REVIEW | HOLD (delegates the gate-firing/precedence
to verdict.py, which already encodes Stage 1/3/4 of rules.md, and layers the
PM-grade fields on top).
Watchlist ideas -> BUY-CANDIDATE | RESEARCH | AVOID (the new-idea funnel).
"""
from __future__ import annotations
import datetime as dt
import json
import os
import re
import sys
import yaml

import dcf as dcf_mod
import technicals
import verdict as verdict_mod
from common import load_holdings
from shariah import STALE_DAYS, ratio_precheck


def first_thesis_line(thesis_text: str) -> str | None:
    """First non-heading, non-blank line of the markdown thesis body."""
    for line in thesis_text.splitlines():
        s = line.strip()
        if s and not s.startswith("#"):
            return s[:200]
    return None

HERE = os.path.dirname(__file__)
WATCHLIST = os.path.join(HERE, "..", "watchlist.md")


def load_cfg() -> dict:
    return verdict_mod.load_cfg()


def load_watchlist() -> list[dict]:
    """Parse 'TICKER | why it's interesting | catalyst date' rows (skips comments/blank)."""
    out = []
    if not os.path.exists(WATCHLIST):
        return out
    for line in open(WATCHLIST, encoding="utf-8"):
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        parts = [p.strip() for p in s.split("|")]
        if not re.fullmatch(r"[A-Za-z][A-Za-z.\-]{0,9}", parts[0]):
            continue
        out.append({
            "ticker": parts[0].upper(),
            "why": parts[1] if len(parts) > 1 and parts[1] else None,
            "catalyst_note": parts[2] if len(parts) > 2 and parts[2] else None,
        })
    return out


def catalyst_days_out(note: str | None, today: dt.date):
    """Best-effort: pull an ISO date (YYYY-MM-DD) out of a catalyst note."""
    if not note:
        return None
    m = re.search(r"\d{4}-\d{2}-\d{2}", note)
    if not m:
        return None
    try:
        return (dt.date.fromisoformat(m.group(0)) - today).days
    except ValueError:
        return None


def reward_risk(price, target, stop):
    """upside/downside off a price, a target, and a downside stop. None if undefined."""
    if price is None or target is None or stop is None or price <= stop:
        return None
    downside = price - stop
    if downside <= 0:
        return None
    return (target - price) / downside


def technical_target_stop(tech: dict | None, price):
    """Fallback target/stop from technicals when no DCF/initial_stop exists:
    target = 52w high (next overhead resistance), stop = chandelier trail."""
    if not tech or price is None:
        return None, None
    stop = tech.get("chandelier_stop")
    dist = tech.get("dist_52w_high_pct")
    target = price / (1 + dist / 100) if dist is not None else None
    return target, stop


def shariah_gate_holding(meta: dict, today: dt.date):
    s = meta.get("shariah") or {}
    status = s.get("status", "unknown")
    screened = s.get("screened")
    stale = False
    if screened:
        d = screened if isinstance(screened, dt.date) else dt.date.fromisoformat(str(screened))
        stale = (today - d).days > STALE_DAYS
    if status == "non-compliant":
        return "FAIL", f"recorded non-compliant (screened {screened}) — exit per mandate"
    if status == "compliant" and not stale:
        return "PASS", f"recorded compliant (screened {screened})"
    if status == "compliant" and stale:
        return "REVIEW", f"recorded compliant but screen is >{STALE_DAYS}d old — re-screen"
    return "REVIEW", f"status '{status}' — verify in Zoya/Musaffa"


def shariah_gate_idea(ticker: str):
    """No recorded broker-app status for a watchlist idea — ratio pre-check only.
    The business-activity screen can't be done programmatically, so (per
    rules.md's screen_weight_compliance convention) that gap is informational,
    not a knockout — only an explicit ratio-test FLAG demotes the verdict."""
    pc = ratio_precheck(ticker)
    if pc.get("ok") is False:
        return "REVIEW", f"ratio pre-check flags: {', '.join(pc.get('flags', []))} — screen before any add"
    if pc.get("ok") is True:
        return "UNVERIFIED", "ratio pre-check clean, but business-activity screen unverified — confirm in Zoya/Musaffa"
    return "UNVERIFIED", f"ratio pre-check unavailable ({pc.get('note', 'no data')}) — must screen in Zoya/Musaffa"


def conviction(rr, has_thesis: bool, broken: bool):
    """Heuristic proxy only — a real conviction call needs YOUR variant view."""
    if broken:
        return "LOW", "thesis flagged broken"
    if rr is None or not has_thesis:
        return "LOW", "missing reward:risk or a stated thesis — cannot self-assess conviction"
    if rr >= 3 and has_thesis:
        return "HIGH", f"reward:risk {rr:.1f}:1 with a stated thesis"
    if rr >= 1.5:
        return "MEDIUM", f"reward:risk {rr:.1f}:1 — moderate skew"
    return "LOW", f"reward:risk {rr:.1f}:1 — skew too thin"


def holding_record(h: dict, vdict: dict, cfg: dict, today: dt.date) -> dict:
    m = h["meta"]
    ticker = m["ticker"]
    px = vdict.get("price")
    tech = technicals.fetch(ticker, cfg)
    shariah_stat, shariah_note = shariah_gate_holding(m, today)

    a = {**dcf_mod.DEFAULTS, **(m.get("dcf") or {})}
    dcf_res = dcf_mod.dcf(ticker, a)
    tgt_method = "DCF intrinsic value"
    target = dcf_res.get("intrinsic_value") if dcf_res.get("ok") else None
    if target is None:
        target, _ = technical_target_stop(tech, px)
        tgt_method = "technical level (52w high)"

    stop = m.get("initial_stop") or (tech.get("chandelier_stop") if tech else None)
    rr = reward_risk(px, target, stop)
    thesis_text = h.get("thesis", "")
    has_thesis = bool(thesis_text and len(thesis_text) > 40)
    broken = bool(m.get("thesis_broken"))
    conv, conv_why = conviction(rr, has_thesis, broken)

    verdict = vdict["verdict"]
    if shariah_stat == "FAIL":
        verdict = "SELL"  # compliance overrides everything else, regardless of skew

    return {
        "ticker": ticker, "name": m.get("name"), "kind": "holding",
        "verdict": verdict,
        "conviction": conv, "conviction_why": conv_why,
        "shariah_status": shariah_stat, "shariah_note": shariah_note,
        "thesis_one_liner": first_thesis_line(thesis_text) if thesis_text else None,
        "catalyst": None,
        "target_price": target, "target_method": tgt_method if target is not None else None,
        "upside_pct": round((target - px) / px * 100, 1) if (target and px) else None,
        "downside_price": stop,
        "downside_pct": round((px - stop) / px * 100, 1) if (stop and px) else None,
        "reward_risk": round(rr, 2) if rr is not None else None,
        "time_horizon": m.get("trade_type", "core"),
        "position_pct": vdict.get("weight_pct"),
        "risk_per_trade_pct": cfg.get("risk_per_trade_pct"),
        "key_risks": None,
        "invalidation": "thesis_broken: true (front-matter)" if not broken else "ALREADY FIRED",
        "stop": stop,
        "what_changes_mind": "thesis_broken flag, a SELL technical trigger, or the Shariah screen flipping",
        "would_buy_today": (verdict in ("HOLD",) and not broken),
        "drivers": vdict.get("drivers"),
        "r_multiple": vdict.get("r_multiple"),
    }


def idea_record(idea: dict, cfg: dict, today: dt.date) -> dict:
    ticker = idea["ticker"]
    tech = technicals.fetch(ticker, cfg)
    px = tech.get("price") if tech else None
    shariah_stat, shariah_note = shariah_gate_idea(ticker)

    target, stop = technical_target_stop(tech, px)
    rr = reward_risk(px, target, stop)
    cat_days = catalyst_days_out(idea.get("catalyst_note"), today)
    horizon = int(cfg.get("catalyst_horizon_days", 60))
    has_edge = bool(idea.get("why"))

    verb, why = "RESEARCH", []
    if shariah_stat == "FAIL" or px is None:
        verb = "AVOID"
        why.append("no price data" if px is None else shariah_note)
    else:
        if not has_edge:
            why.append("EDGE_GATE: no stated reason the market is wrong — supply `why` in watchlist.md")
        if rr is None:
            why.append("ASYMMETRY_GATE: no defined target/stop — can't compute reward:risk")
        elif rr < float(cfg.get("reward_risk_min_swing", 2.0)):
            why.append(f"ASYMMETRY_GATE: reward:risk {rr:.1f}:1 below swing floor "
                       f"{cfg.get('reward_risk_min_swing', 2.0)}:1")
        if cat_days is None:
            why.append(f"CATALYST_GATE: no catalyst date given (state one within {horizon}d)")
        elif cat_days > horizon:
            why.append(f"CATALYST_GATE: catalyst {cat_days}d out > {horizon}d horizon")
        if shariah_stat == "REVIEW":
            why.append(shariah_note)
        if (has_edge and rr is not None and rr >= float(cfg.get("reward_risk_min_swing", 2.0))
                and cat_days is not None and 0 <= cat_days <= horizon
                and shariah_stat != "REVIEW"):
            verb = "BUY-CANDIDATE"
            why.append(f"compliance: {shariah_note}")

    return {
        "ticker": ticker, "name": None, "kind": "idea",
        "verdict": verb,
        "conviction": "LOW" if verb != "BUY-CANDIDATE" else conviction(rr, has_edge, False)[0],
        "conviction_why": "; ".join(why) if why else "cleared edge/asymmetry/catalyst gates",
        "shariah_status": shariah_stat, "shariah_note": shariah_note,
        "thesis_one_liner": idea.get("why"),
        "catalyst": idea.get("catalyst_note"),
        "target_price": target, "target_method": "technical level (52w high)" if target else None,
        "upside_pct": round((target - px) / px * 100, 1) if (target and px) else None,
        "downside_price": stop,
        "downside_pct": round((px - stop) / px * 100, 1) if (stop and px) else None,
        "reward_risk": round(rr, 2) if rr is not None else None,
        "time_horizon": "swing", "position_pct": None,
        "risk_per_trade_pct": cfg.get("risk_per_trade_pct"),
        "key_risks": None, "invalidation": None, "stop": stop,
        "what_changes_mind": "a stated thesis, a defined stop/target, or a dated catalyst appearing",
        "would_buy_today": verb == "BUY-CANDIDATE",
        "drivers": None, "r_multiple": None,
    }


def main() -> None:
    cfg = load_cfg()
    today = dt.date.today()

    hs = load_holdings()
    vresult = verdict_mod.compute(cfg, hs)
    vmap = {v["ticker"]: v for v in vresult["verdicts"]}
    holdings_out = [holding_record(h, vmap[h["meta"]["ticker"]], cfg, today)
                    for h in hs if h["meta"]["ticker"] in vmap]

    ideas = load_watchlist()
    ideas_out = [idea_record(i, cfg, today) for i in ideas]

    print(json.dumps({
        "note": vresult.get("note"),
        "portfolio_notes": vresult.get("portfolio_notes"),
        "disclaimer": ("Decision support, not advice. CONVICTION/ASYMMETRY/EDGE fields are "
                       "mechanical proxies — they cannot replace your own variant view. "
                       "Shariah status must be verified in Zoya/Musaffa."),
        "holdings": holdings_out,
        "ideas": ideas_out,
    }, indent=2, default=str))


if __name__ == "__main__":
    main()
