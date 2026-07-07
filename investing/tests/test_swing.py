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
import journal
import recommend
import scaffold
import common

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


def test_gap_sizing():
    cfg = {"risk_per_trade_pct": 1.5, "earnings_gap_assumption_pct": 25,
           "catalyst_horizon_days": 60}

    # earnings in window + exit_before -> stop-based sizing, no gap adjustment
    g = recommend.gap_sizing(100.0, 90.0, 20,
                             {"holding_window_days": 30, "earnings_plan": "exit_before"}, cfg)
    assert g["earnings_in_window"] and not g["gap_plan_missing"], g
    assert g["stop_based_position_pct"] == 15.0, g       # 1.5 / 10% * 100
    assert g["gap_adjusted_position_pct"] is None, g
    assert "stop math valid" in g["gap_risk_note"], g

    # hold_through_sized_down -> gap-adjusted = risk / gap_pct = 1.5/25*100 = 6.0
    g = recommend.gap_sizing(100.0, 90.0, 20,
                             {"holding_window_days": 30, "earnings_plan": "hold_through_sized_down"}, cfg)
    assert g["gap_adjusted_position_pct"] == 6.0, g
    assert g["stop_based_position_pct"] == 15.0, g       # both numbers emitted

    # earnings in window but plan can't cover it -> GAP_PLAN_MISSING
    g = recommend.gap_sizing(100.0, 90.0, 20,
                             {"holding_window_days": 30, "earnings_plan": "no_earnings_in_window"}, cfg)
    assert g["gap_plan_missing"] and "GAP_PLAN_MISSING" in g["gap_risk_note"], g

    # earnings OUTSIDE the holding window -> stop-based applies, not missing
    g = recommend.gap_sizing(100.0, 90.0, 90,
                             {"holding_window_days": 30, "earnings_plan": "exit_before"}, cfg)
    assert not g["earnings_in_window"] and not g["gap_plan_missing"], g
    print("ok  gap_sizing exit_before / hold_through / missing / out-of-window")


def test_gap_plan_missing_blocks_buy_candidate():
    cfg = {"reward_risk_min_swing": 2.0, "catalyst_horizon_days": 60,
           "risk_per_trade_pct": 1.5, "earnings_gap_assumption_pct": 25, "target_atr_mult": 10.0}
    idea = {"ticker": "TEST", "why": None, "catalyst_note": "2026-07-27 earnings"}  # 20d out
    restore = _patch(monkey_tech=_synthetic_tech(), ratio_ok=True)
    try:
        # Card asserts "no earnings in window" but a catalyst lands 20d out -> blocked
        conflict = recommend.idea_record(
            idea, cfg, TODAY,
            {"TEST": _card(holding_window_days=30, earnings_plan="no_earnings_in_window")})
        assert conflict["verdict"] == "RESEARCH", conflict["verdict"]
        assert "GAP_PLAN_MISSING" in conflict["conviction_why"], conflict["conviction_why"]

        # hold_through_sized_down clears and emits the gap-adjusted size
        ok = recommend.idea_record(
            idea, cfg, TODAY,
            {"TEST": _card(holding_window_days=30, earnings_plan="hold_through_sized_down")})
        assert ok["verdict"] == "BUY-CANDIDATE", (ok["verdict"], ok["conviction_why"])
        assert ok["gap_adjusted_position_pct"] == 6.0, ok
    finally:
        restore()
    print("ok  GAP_PLAN_MISSING blocks BUY-CANDIDATE; hold_through emits gap size")


def test_discover_never_buy_candidate():
    v, _ = discover.classify(True, 4.0, 15, horizon=60, rr_floor=3.0)
    assert v == "LEAD", v
    v, _ = discover.classify(True, 1.0, 15, horizon=60, rr_floor=3.0)
    assert v == "RESEARCH", v
    v, _ = discover.classify(False, 4.0, 15, horizon=60, rr_floor=3.0)
    assert v == "AVOID", v
    print("ok  discover.classify emits LEAD, never BUY-CANDIDATE")


def test_liquidity_floor():
    cfg = {"screen_min_mcap": 500e6, "screen_min_avg_dollar_vol": 5e6}
    ok, why = discover.passes_liquidity(300e6, 20e6, cfg)   # mcap too small
    assert not ok and "mcap" in why, why
    ok, why = discover.passes_liquidity(2e9, 1e6, cfg)      # $vol too thin
    assert not ok and "$vol" in why, why
    ok, _ = discover.passes_liquidity(2e9, 20e6, cfg)       # both fine
    assert ok
    ok, _ = discover.passes_liquidity(None, None, cfg)      # unknown != fail
    assert ok
    print("ok  liquidity floor drops small-cap / thin-volume leads")


def test_discover_writes_leads_not_watchlist(tmp_path=None):
    import os as _os
    leads = discover.leads_text(["FOO | auto note | earnings 2026-08-01"], TODAY)
    assert "AUTO-GENERATED" in leads and "OVERWRITTEN" in leads, leads
    assert "watchlist.md instead" in leads, leads
    # discover writes LEADS, and no longer has a watchlist writer
    assert hasattr(discover, "write_leads")
    assert not hasattr(discover, "write_watchlist"), "watchlist writer must be gone"
    # write to a scratch path and confirm it lands, watchlist path untouched
    scratch = _os.path.join(_os.path.dirname(discover.LEADS), ".leads_test.md")
    try:
        discover.write_leads([], TODAY, {}, path=scratch)
        assert _os.path.exists(scratch)
    finally:
        if _os.path.exists(scratch):
            _os.remove(scratch)
    print("ok  discover writes leads.md; watchlist.md untouched by scripts")


def test_journal_expectancy():
    # 4 closed trades across 2 setup types; shares/entry/stop chosen for round R.
    def sell(setup, entry, exitp, stop, sh, pl, days, reason, be, bx, r):
        return {"action": "sell", "ticker": "X", "setup_type": setup,
                "entry_price": entry, "exit_price": exitp, "stop": stop, "shares": sh,
                "realized_pl": pl, "holding_days": days, "exit_reason": reason,
                "realized_r": r, "benchmark_entry": be, "benchmark_exit": bx}
    rows = [
        {"action": "buy", "ticker": "X", "setup_type": "breakout"},  # ignored by report
        sell("breakout", 100, 130, 90, 10, 300, 20, "target", 50, 55, 3.0),
        sell("breakout", 100, 88, 90, 10, -120, 8, "stop", 50, 52, -1.2),
        sell("pullback", 50, 60, 45, 20, 100, 15, "target", 50, 53, 2.0),
        sell("pullback", 50, 47, 45, 20, -30, 6, "stop", 50, 49, -0.6),
    ]
    rep = journal.report(rows, {"journal_min_trades": 20})

    ov = rep["overall"]
    assert ov["trades"] == 4 and ov["hit_rate"] == 0.5, ov
    assert ov["avg_win_r"] == 2.5 and ov["avg_loss_r"] == -0.9, ov
    assert ov["expectancy_r"] == 0.8 and ov["expectancy_currency"] == 62.5, ov
    assert ov["total_pl"] == 250, ov
    assert rep["sample_note"] and "too small" in rep["sample_note"], rep["sample_note"]

    bs = rep["by_setup_type"]
    assert set(bs) == {"breakout", "pullback"}, bs
    assert bs["breakout"]["expectancy_r"] == 0.9 and bs["breakout"]["total_pl"] == 180, bs["breakout"]
    assert bs["pullback"]["expectancy_r"] == 0.7 and bs["pullback"]["total_pl"] == 70, bs["pullback"]

    # slippage on stops: (90-88)=2 and (45-47)=-2 -> avg 0 over 2 stops
    sl = rep["slippage_on_stops"]
    assert sl["stopped_trades"] == 2 and sl["avg_stop_minus_exit"] == 0.0, sl

    # benchmark counterfactual: capital*bench_return summed = 100+40+60-20 = 180
    cf = rep["benchmark_counterfactual"]
    assert cf["trades_covered"] == 4 and cf["benchmark_pl"] == 180.0, cf
    assert cf["trade_pl"] == 250.0 and cf["excess_vs_benchmark"] == 70.0, cf
    print("ok  journal per-setup expectancy + slippage + benchmark counterfactual")


SCAFFOLD_CFG = {"atr_stop_mult": 3.0, "t1_r": 1.5, "t2_r": 3.0,
                "catalyst_horizon_days": 60, "duration_days_swing": 21,
                "screen_min_avg_dollar_vol": 5e6, "reward_risk_min_swing": 2.0,
                "risk_per_trade_pct": 1.5, "earnings_gap_assumption_pct": 25,
                "target_atr_mult": 10.0}
FULL_TECH = {"price": 445.10, "atr": 4.10, "ema_fast": 430.0, "ema_slow": 400.0,
             "chandelier_stop": 438.90, "dist_52w_high_pct": -1.0, "avg_dollar_vol": 120e6}


def _parse_card(text):
    import yaml
    return yaml.safe_load(text.split("---", 2)[1])


def test_scaffold_render_full_card():
    st = scaffold.pick_setup_type(FULL_TECH, None, SCAFFOLD_CFG)
    card = scaffold.render_card("NOW", FULL_TECH, "2026-08-05",
                                {"avg_dollar_vol": 120e6, "ok": True}, {"ok": True, "flags": []},
                                SCAFFOLD_CFG, st, TODAY)
    m = _parse_card(card)
    # Every plan field non-empty; status draft; shariah unverified even when clean.
    for f in ("entry_trigger", "stop_logic", "target_logic", "invalidation"):
        assert m[f] and str(m[f]).strip(), (f, m[f])
    for f in ("entry_price", "stop_price", "target_price", "holding_window_days"):
        assert m[f] is not None, (f, m[f])
    assert m["status"] == "draft", m["status"]
    assert m["shariah"]["status"] == "unverified", m["shariah"]

    # Parses via load_setups() from a temp dir
    import tempfile
    d = tempfile.mkdtemp()
    open(os.path.join(d, "now.md"), "w").write(card)
    loaded = common.load_setups(d)
    assert len(loaded) == 1 and loaded[0]["meta"]["status"] == "draft"
    print("ok  scaffold render: full draft card, unverified, parses via load_setups")


def test_scaffold_setup_type_heuristic():
    # earnings within horizon -> earnings_run (even if near a high)
    assert scaffold.pick_setup_type(FULL_TECH, 20, SCAFFOLD_CFG) == "earnings_run"
    # near the 52w high, no near catalyst -> breakout
    assert scaffold.pick_setup_type({"dist_52w_high_pct": -2.0}, None, SCAFFOLD_CFG) == "breakout"
    # well below the high, no catalyst -> pullback
    assert scaffold.pick_setup_type({"dist_52w_high_pct": -30.0}, None, SCAFFOLD_CFG) == "pullback"
    # entry/trigger/invalidation text varies per type
    pull = _parse_card(scaffold.render_card("X", {"price": 50, "atr": 1.0, "ema_fast": 48.0,
                       "chandelier_stop": 46.0, "dist_52w_high_pct": -30.0, "avg_dollar_vol": 9e6},
                       None, {"avg_dollar_vol": 9e6, "ok": True}, {"ok": True}, SCAFFOLD_CFG, "pullback", TODAY))
    assert "EMA20" in pull["entry_trigger"] and "EMA20" in pull["invalidation"], pull
    print("ok  scaffold setup-type heuristic + per-type text")


def test_scaffold_missing_data():
    # No technicals at all -> a valid, parseable card with unavailable comments.
    card = scaffold.render_card("ZZZ", None, None, {"avg_dollar_vol": None, "ok": True},
                                {"ok": None, "note": "no data"}, SCAFFOLD_CFG, "breakout", TODAY)
    m = _parse_card(card)
    assert m["entry_price"] is None and m["stop_price"] is None and m["target_price"] is None, m
    assert m["status"] == "draft" and m["shariah"]["status"] == "unverified"
    assert "scaffold:" in card and "unavailable" in card
    print("ok  scaffold missing-data path writes a valid null card")


def test_scaffold_draft_gate_and_refuse_overwrite():
    # A fully-filled DRAFT card caps at RESEARCH with the review-and-approve message.
    draft = _card(status="draft")
    sg = recommend.evaluate_setup(draft, TODAY)
    assert sg["is_draft"] is True and sg["status_ok"] is False and sg["complete"] is True, sg

    cfg = {"reward_risk_min_swing": 2.0, "catalyst_horizon_days": 60,
           "risk_per_trade_pct": 1.5, "earnings_gap_assumption_pct": 25, "target_atr_mult": 10.0}
    idea = {"ticker": "TEST", "why": None, "catalyst_note": "2026-07-27 earnings"}
    restore = _patch(monkey_tech=_synthetic_tech(), ratio_ok=True)
    try:
        rec = recommend.idea_record(idea, cfg, TODAY, {"TEST": draft})
        assert rec["verdict"] == "RESEARCH", rec["verdict"]
        assert "machine-filled DRAFT" in rec["conviction_why"], rec["conviction_why"]
        # Owner approves: flip to planned -> BUY-CANDIDATE (card already compliant+fresh)
        approved = recommend.idea_record(idea, cfg, TODAY, {"TEST": _card(status="planned")})
        assert approved["verdict"] == "BUY-CANDIDATE", (approved["verdict"], approved["conviction_why"])
    finally:
        restore()

    # Refuse to overwrite an existing card without --force.
    import tempfile
    d = tempfile.mkdtemp()
    p = os.path.join(d, "aaa.md")
    open(p, "w").write("existing\n")
    written, msg = scaffold.scaffold_one("AAA", SCAFFOLD_CFG, TODAY, "breakout", force=False, setups_dir=d)
    assert written is False and "exists" in msg, msg
    assert open(p).read() == "existing\n", "file must be unchanged"
    print("ok  draft gate caps at RESEARCH; approval flips; overwrite refused without --force")


if __name__ == "__main__":
    test_evaluate_setup()
    test_idea_record_buy_candidate_gate()
    test_gap_sizing()
    test_gap_plan_missing_blocks_buy_candidate()
    test_discover_never_buy_candidate()
    test_liquidity_floor()
    test_discover_writes_leads_not_watchlist()
    test_journal_expectancy()
    test_scaffold_render_full_card()
    test_scaffold_setup_type_heuristic()
    test_scaffold_missing_data()
    test_scaffold_draft_gate_and_refuse_overwrite()
    print("\nall swing-refactor changes verified offline")
