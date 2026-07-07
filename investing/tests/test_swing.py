"""Offline regression tests for the swing-first refactor (REFACTOR_SPEC_SWING.md).

Run: python tests/test_swing.py   (from the investing/ directory)
No network — technicals.fetch and ratio_precheck are monkeypatched.

Covers (acceptance checklist items 1-3):
  1. evaluate_setup  — a complete planned card is an edge; missing required
     fields fail EDGE_GATE and are named.
  2. idea_record     — complete card + fresh compliant Shariah + R:R >= floor +
     catalyst in window -> BUY-CANDIDATE; the same card UNVERIFIED -> RESEARCH.
  3. discover.classify never returns BUY-CANDIDATE; returns LEAD.
"""
import datetime as dt
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import discover
import recommend

TODAY = dt.date(2026, 7, 7)


def _card(**over):
    """A complete, planned, freshly-compliant setup card (meta dict)."""
    meta = {
        "ticker": "TEST", "status": "planned", "setup_type": "breakout",
        "entry_trigger": "close > 101 on 2x avg volume", "entry_price": 100,
        "stop_price": 90, "stop_logic": "below the breakout base / prior swing low",
        "target_price": 140, "target_logic": "measured move = base height",
        "holding_window_days": 30, "catalyst": "2026-07-27 earnings",
        "earnings_plan": "exit_before",
        "invalidation": "loses the breakout level intraday / volume dries up",
        "shariah": {"status": "compliant", "source": "zoya", "screened": "2026-06-20"},
    }
    meta.update(over)
    return {"meta": meta, "thesis": "notes", "path": "setups/test.md"}


def _synthetic_tech(price=100.0, atr=5.0, stop=90.0, dist_52w_high_pct=-30.0):
    return {"price": price, "atr": atr, "chandelier_stop": stop,
            "dist_52w_high_pct": dist_52w_high_pct}


def _patch(monkey_tech=None, ratio_ok=True):
    """Swap network calls for synthetic values; return a restore() thunk."""
    orig_fetch = recommend.technicals.fetch
    orig_ratio = recommend.ratio_precheck
    recommend.technicals.fetch = lambda tk, cfg: monkey_tech
    recommend.ratio_precheck = lambda tk: {"ok": ratio_ok}

    def restore():
        recommend.technicals.fetch = orig_fetch
        recommend.ratio_precheck = orig_ratio
    return restore


def test_evaluate_setup():
    ok = recommend.evaluate_setup(_card(), TODAY)
    assert ok["found"] and ok["complete"] and ok["status_ok"], ok
    assert ok["shariah_ok"] is True, ok

    missing = recommend.evaluate_setup(
        _card(entry_trigger="", stop_logic="   ", invalidation=None), TODAY)
    assert missing["complete"] is False
    for f in ("entry_trigger", "stop_logic", "invalidation"):
        assert f in missing["missing"], (f, missing["missing"])

    # A bad earnings_plan value is flagged; a live card with no card at all fails found.
    badplan = recommend.evaluate_setup(_card(earnings_plan="maybe"), TODAY)
    assert any("earnings_plan" in x for x in badplan["missing"]), badplan
    assert recommend.evaluate_setup(None, TODAY)["found"] is False

    # Stale screen -> not shariah_ok even though status is compliant.
    stale = recommend.evaluate_setup(
        _card(shariah={"status": "compliant", "source": "zoya", "screened": "2025-01-01"}), TODAY)
    assert stale["shariah_ok"] is False, stale
    print("ok  evaluate_setup completeness + shariah freshness")


def test_idea_record_buy_candidate_gate():
    cfg = {"reward_risk_min_swing": 2.0, "catalyst_horizon_days": 60,
           "risk_per_trade_pct": 1.5, "target_atr_mult": 10.0}
    idea = {"ticker": "TEST", "why": None, "catalyst_note": "2026-07-27 earnings"}

    restore = _patch(monkey_tech=_synthetic_tech(), ratio_ok=True)
    try:
        # Complete + fresh compliant card -> BUY-CANDIDATE
        rec = recommend.idea_record(idea, cfg, TODAY, {"TEST": _card()})
        assert rec["verdict"] == "BUY-CANDIDATE", (rec["verdict"], rec["conviction_why"])
        assert rec["would_buy_today"] is True
        assert rec["reward_risk"] and rec["reward_risk"] >= 2.0

        # Same card but Shariah UNVERIFIED -> can never be BUY-CANDIDATE
        unv = recommend.idea_record(idea, cfg, TODAY,
                                    {"TEST": _card(shariah={"status": "unverified"})})
        assert unv["verdict"] == "RESEARCH", unv["verdict"]
        assert "SHARIAH_GATE" in unv["conviction_why"], unv["conviction_why"]

        # No setup card at all -> RESEARCH, EDGE_GATE names the fix
        nocard = recommend.idea_record(idea, cfg, TODAY, {})
        assert nocard["verdict"] == "RESEARCH", nocard["verdict"]
        assert "EDGE_GATE" in nocard["conviction_why"], nocard["conviction_why"]

        # Incomplete card -> RESEARCH, EDGE_GATE names the missing field
        incomplete = recommend.idea_record(idea, cfg, TODAY,
                                           {"TEST": _card(target_logic="")})
        assert incomplete["verdict"] == "RESEARCH"
        assert "target_logic" in incomplete["conviction_why"], incomplete["conviction_why"]
    finally:
        restore()

    # Ratio/business knockout -> hard AVOID regardless of the card
    restore = _patch(monkey_tech=_synthetic_tech(), ratio_ok=False)
    try:
        avoid = recommend.idea_record(idea, cfg, TODAY, {"TEST": _card()})
        assert avoid["verdict"] == "AVOID", avoid["verdict"]
    finally:
        restore()
    print("ok  idea_record BUY-CANDIDATE requires card + verified Shariah")


def test_discover_never_buy_candidate():
    v, _ = discover.classify(True, 4.0, 15, horizon=60, rr_floor=3.0)
    assert v == "LEAD", v
    v, _ = discover.classify(True, 1.0, 15, horizon=60, rr_floor=3.0)
    assert v == "RESEARCH", v
    v, _ = discover.classify(False, 4.0, 15, horizon=60, rr_floor=3.0)
    assert v == "AVOID", v
    print("ok  discover.classify emits LEAD, never BUY-CANDIDATE")


if __name__ == "__main__":
    test_evaluate_setup()
    test_idea_record_buy_candidate_gate()
    test_discover_never_buy_candidate()
    print("\nall swing-refactor changes verified offline")
