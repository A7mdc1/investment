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
from common import load_holdings, setups_by_ticker
from shariah import STALE_DAYS, ratio_precheck

# Setup-card fields that must be non-empty for the card to count as a real edge.
SETUP_REQUIRED_FIELDS = ("entry_trigger", "stop_logic", "target_logic",
                         "earnings_plan", "invalidation")
SETUP_ACTIVE_STATUS = ("planned", "live")
EARNINGS_PLAN_VALUES = ("exit_before", "hold_through_sized_down", "no_earnings_in_window")


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


def reward_risk(price, target, stop, atr=None, min_atr_frac=0.5):
    """upside/downside off a price, a target, and a downside stop. None if undefined.

    Degenerate-denominator guard: when price sits right on top of the stop
    (common with a chandelier trail after consolidation), (price - stop) -> 0
    and R:R explodes into artifacts (665:1 etc). If ATR is known, floor the
    downside at min_atr_frac * ATR — you cannot risk less than the noise."""
    if price is None or target is None or stop is None or price <= stop:
        return None
    downside = price - stop
    if atr is not None and atr > 0:
        downside = max(downside, min_atr_frac * atr)
    if downside <= 0:
        return None
    return (target - price) / downside


def technical_target_stop(tech: dict | None, price, cfg: dict | None = None):
    """Fallback target/stop from technicals when no DCF/initial_stop exists:
    target = 52w high (next overhead resistance), stop = chandelier trail.

    Sanity bound: for a crashed stock the 52w high is a different regime, not
    resistance (e.g. price $15, "target" $134 -> fake 8x upside). Cap the
    target at price + target_atr_mult * ATR — the far edge of what a swing
    horizon can plausibly reach."""
    if not tech or price is None:
        return None, None
    cfg = cfg or {}
    stop = tech.get("chandelier_stop")
    dist = tech.get("dist_52w_high_pct")
    target = price / (1 + dist / 100) if dist is not None else None
    atr = tech.get("atr")
    if target is not None and atr is not None and atr > 0:
        cap = price + float(cfg.get("target_atr_mult", 10.0)) * atr
        target = min(target, cap)
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


def evaluate_setup(setup: dict | None, today: dt.date, stale_days: int = STALE_DAYS) -> dict:
    """Assess a pre-trade setup card as the swing 'edge' (Change 1/2).

    Returns {found, complete, missing[], status, status_ok, shariah_ok,
    shariah_status, shariah_note, setup_type, earnings_plan, holding_window_days}.
    A card is a real edge only when every SETUP_REQUIRED_FIELD is non-empty,
    earnings_plan is a recognized value, and status is planned|live."""
    if not setup:
        return {"found": False, "complete": False,
                "missing": ["no setup card — create setups/<ticker>.md from _template.md"],
                "status": None, "status_ok": False, "shariah_ok": False,
                "shariah_status": None, "shariah_note": "no setup card",
                "setup_type": None, "earnings_plan": None, "holding_window_days": None}

    m = setup["meta"]
    missing = []
    for f in SETUP_REQUIRED_FIELDS:
        v = m.get(f)
        if v is None or (isinstance(v, str) and not v.strip()):
            missing.append(f)
    plan = m.get("earnings_plan")
    if plan is not None and plan not in EARNINGS_PLAN_VALUES:
        missing.append(f"earnings_plan (got '{plan}', expected one of {'/'.join(EARNINGS_PLAN_VALUES)})")
    status = m.get("status")
    status_ok = status in SETUP_ACTIVE_STATUS

    # Shariah freshness comes from the CARD's own screen, not the ratio pre-check:
    # a BUY-CANDIDATE needs a real compliant verdict recorded within stale_days.
    sh = m.get("shariah") or {}
    sh_status = sh.get("status", "unverified")
    screened = sh.get("screened")
    fresh, screen_note = False, "no screen date"
    if screened:
        try:
            age = (today - dt.date.fromisoformat(str(screened))).days
            fresh = age <= stale_days
            screen_note = f"screened {screened} ({age}d ago)" + ("" if fresh else " — STALE, re-screen")
        except ValueError:
            screen_note = f"unparseable screen date '{screened}'"
    shariah_ok = (sh_status == "compliant") and fresh
    if sh_status != "compliant":
        shariah_note = f"card Shariah status '{sh_status}' — verify compliant in Zoya/Musaffa"
    else:
        shariah_note = f"card Shariah compliant, {screen_note}"

    return {"found": True, "complete": not missing, "missing": missing,
            "status": status, "status_ok": status_ok,
            "shariah_ok": shariah_ok, "shariah_status": sh_status, "shariah_note": shariah_note,
            "setup_type": m.get("setup_type"), "earnings_plan": plan,
            "holding_window_days": m.get("holding_window_days")}


def gap_sizing(px, stop, cat_days, sg: dict, cfg: dict) -> dict:
    """Gap-aware sizing + earnings-plan check (Change 3).

    A stop does NOT execute through an overnight earnings gap, so for any trade
    whose earnings fall inside the holding window the record must price the gap
    instead of pretending the stop-distance math holds:
      - exit_before            -> flat before the print; stop-based sizing valid
      - hold_through_sized_down-> emit BOTH the stop-based max AND a gap-adjusted
                                  size (risk / assumed-gap), "size for the print"
      - anything else in-window-> GAP_PLAN_MISSING (blocks BUY-CANDIDATE)
    """
    risk = float(cfg.get("risk_per_trade_pct", 1.5))
    gap_pct = float(cfg.get("earnings_gap_assumption_pct", 25))
    window = sg.get("holding_window_days") or int(cfg.get("catalyst_horizon_days", 60))

    stop_based = None
    if px and stop and px > stop:
        stop_dist_pct = (px - stop) / px * 100
        if stop_dist_pct > 0:
            stop_based = round(risk / stop_dist_pct * 100, 1)

    earnings_in_window = cat_days is not None and 0 <= cat_days <= window
    plan = sg.get("earnings_plan")
    gap_adj, plan_missing = None, False

    if not earnings_in_window:
        note = "no earnings inside the holding window — stop-based sizing applies"
    elif plan == "exit_before":
        note = "earnings in window; plan is flat before the print — stop math valid"
    elif plan == "hold_through_sized_down":
        gap_adj = round(risk / gap_pct * 100, 1)
        note = (f"earnings in window, holding through — size for the print, not the stop: "
                f"gap-adjusted {gap_adj}% (assumes {gap_pct:.0f}% adverse gap)"
                + (f" vs stop-based {stop_based}%" if stop_based is not None else ""))
    else:
        plan_missing = True
        note = ("GAP_PLAN_MISSING: earnings inside the holding window but no valid "
                "earnings_plan (exit_before | hold_through_sized_down) — a stop does "
                "not execute through an overnight gap; state the plan on the card")

    return {"stop_based_position_pct": stop_based, "gap_adjusted_position_pct": gap_adj,
            "earnings_in_window": earnings_in_window, "gap_plan_missing": plan_missing,
            "gap_risk_note": note}


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
        target, _ = technical_target_stop(tech, px, cfg)
        tgt_method = "technical level (52w high, ATR-capped)"

    stop = m.get("initial_stop") or (tech.get("chandelier_stop") if tech else None)
    rr = reward_risk(px, target, stop, atr=tech.get("atr") if tech else None)
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


def idea_record(idea: dict, cfg: dict, today: dt.date, setups: dict | None = None) -> dict:
    ticker = idea["ticker"]
    tech = technicals.fetch(ticker, cfg)
    px = tech.get("price") if tech else None

    # Shariah: a ratio/business-activity knockout (banks etc.) is the only hard
    # AVOID for a new idea. Otherwise the CARD's recorded verdict gates BUY-CANDIDATE.
    pc = ratio_precheck(ticker)
    shariah_stat, shariah_note = shariah_gate_idea(ticker)

    # EDGE for a swing trade = a completed setup card (Change 1/2), not a `why` string.
    setup = (setups or {}).get(ticker.upper())
    sg = evaluate_setup(setup, today, STALE_DAYS)
    has_edge = sg["found"] and sg["complete"] and sg["status_ok"]

    target, stop = technical_target_stop(tech, px, cfg)
    rr = reward_risk(px, target, stop, atr=tech.get("atr") if tech else None)
    cat_days = catalyst_days_out(idea.get("catalyst_note"), today)
    horizon = int(cfg.get("catalyst_horizon_days", 60))
    floor = float(cfg.get("reward_risk_min_swing", 2.0))
    gap = gap_sizing(px, stop, cat_days, sg, cfg)  # Change 3: gap-aware sizing

    def edge_reasons():
        r = []
        if not sg["found"]:
            r.append("EDGE_GATE: no setup card — create setups/%s.md from _template.md" % ticker.lower())
        else:
            if sg["missing"]:
                r.append("EDGE_GATE: setup card incomplete — fill " + ", ".join(sg["missing"]))
            if not sg["status_ok"]:
                r.append(f"EDGE_GATE: setup status '{sg['status']}' — must be planned|live")
        return r

    verb, why = "RESEARCH", []
    if pc.get("ok") is False:
        verb = "AVOID"  # ratio/business knockout — the only hard AVOID for a new idea
        why.append(f"SHARIAH_KNOCKOUT: {shariah_note}")
    elif px is None:
        # Data gap, NOT a knockout: with no price we can't run the asymmetry gate,
        # so the idea stays RESEARCH ("not investable today"), not excluded. The
        # qualitative gates (edge, catalyst) still report so you see what's missing.
        why.append("DATA_GAP: no price feed — can't compute reward:risk; underwrite when data is available")
        why.extend(edge_reasons())
        if cat_days is None:
            why.append(f"CATALYST_GATE: no catalyst date given (state one within {horizon}d)")
        elif cat_days > horizon:
            why.append(f"CATALYST_GATE: catalyst {cat_days}d out > {horizon}d horizon")
    else:
        why.extend(edge_reasons())
        if rr is None:
            why.append("ASYMMETRY_GATE: no defined target/stop — can't compute reward:risk")
        elif rr < floor:
            why.append(f"ASYMMETRY_GATE: reward:risk {rr:.1f}:1 below swing floor {floor}:1")
        if cat_days is None:
            why.append(f"CATALYST_GATE: no catalyst date given (state one within {horizon}d)")
        elif cat_days > horizon:
            why.append(f"CATALYST_GATE: catalyst {cat_days}d out > {horizon}d horizon")
        # Shariah must be VERIFIED compliant + fresh on the card — UNVERIFIED can
        # never be BUY-CANDIDATE (the whole point of Change 2).
        if not sg["shariah_ok"]:
            why.append(f"SHARIAH_GATE: {sg['shariah_note']}")
        # A stop does not execute through an earnings gap — an in-window print with
        # no valid earnings_plan blocks BUY-CANDIDATE (Change 3).
        if gap["gap_plan_missing"]:
            why.append(gap["gap_risk_note"])
        if (has_edge and rr is not None and rr >= floor
                and cat_days is not None and 0 <= cat_days <= horizon
                and sg["shariah_ok"] and not gap["gap_plan_missing"]):
            verb = "BUY-CANDIDATE"
            why = [f"cleared setup/asymmetry/catalyst/Shariah gates ({sg['setup_type'] or 'setup'}); "
                   f"reward:risk {rr:.1f}:1, catalyst {cat_days}d out, {sg['shariah_note']}; "
                   f"{gap['gap_risk_note']}"]

    return {
        "ticker": ticker, "name": None, "kind": "idea",
        "verdict": verb,
        "conviction": "LOW" if verb != "BUY-CANDIDATE" else conviction(rr, has_edge, False)[0],
        "conviction_why": "; ".join(why) if why else "cleared setup/asymmetry/catalyst/Shariah gates",
        "shariah_status": shariah_stat, "shariah_note": shariah_note,
        "setup_card": sg["found"], "setup_type": sg["setup_type"],
        "setup_complete": sg["complete"] and sg["status_ok"],
        "setup_shariah_status": sg["shariah_status"],
        "earnings_plan": sg["earnings_plan"],
        "thesis_one_liner": idea.get("why"),
        "catalyst": idea.get("catalyst_note"),
        "target_price": target, "target_method": "technical level (52w high)" if target else None,
        "upside_pct": round((target - px) / px * 100, 1) if (target and px) else None,
        "downside_price": stop,
        "downside_pct": round((px - stop) / px * 100, 1) if (stop and px) else None,
        "reward_risk": round(rr, 2) if rr is not None else None,
        "time_horizon": "swing",
        "position_pct": gap["stop_based_position_pct"],
        "stop_based_position_pct": gap["stop_based_position_pct"],
        "gap_adjusted_position_pct": gap["gap_adjusted_position_pct"],
        "earnings_in_window": gap["earnings_in_window"],
        "gap_risk_note": gap["gap_risk_note"],
        "risk_per_trade_pct": cfg.get("risk_per_trade_pct"),
        "key_risks": None, "invalidation": (setup["meta"].get("invalidation") if setup else None),
        "stop": stop,
        "what_changes_mind": "a completed setup card, a verified compliant screen, or a dated catalyst appearing",
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
    setups = setups_by_ticker()
    ideas_out = [idea_record(i, cfg, today, setups) for i in ideas]

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
