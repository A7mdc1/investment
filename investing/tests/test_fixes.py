"""Offline regression tests for the 2026-07-06 pipeline fixes.

Run: python tests/test_fixes.py   (from the investing/ directory)
No network needed — everything is exercised with synthetic inputs.

Covers:
  1. reward_risk ATR floor  — kills the 600:1 stop-a-cent-below-price artifact
  2. technical_target_stop  — caps the 52w-high target on crashed stocks (BMNR)
  3. rank_and_select        — winsorized R:R: one outlier can't flatten the field
  4. business_precheck      — banks are a hard knockout; missing data is unknown
  5. classify               — zero-edge ideas held to the 3:1 floor
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import discover
import recommend
import shariah


def test_reward_risk_atr_floor():
    # BTG-like artifact: price $4.048, stop $4.04, target $6.23, ATR ~$0.18.
    # Old math: (6.23-4.048)/0.008 = 272:1. New: downside floored at 0.5*ATR.
    rr = recommend.reward_risk(4.048, 6.23, 4.04, atr=0.18)
    assert rr is not None and rr < 30, f"artifact not killed: {rr}"
    expected = (6.23 - 4.048) / (0.5 * 0.18)
    assert abs(rr - expected) < 1e-9, (rr, expected)

    # Healthy setup untouched: downside (1.00) > 0.5*ATR (0.25)
    rr = recommend.reward_risk(10.0, 13.0, 9.0, atr=0.5)
    assert abs(rr - 3.0) < 1e-9, rr

    # Backward compatible without ATR; None cases still None
    assert recommend.reward_risk(10.0, 13.0, 9.0) == 3.0
    assert recommend.reward_risk(10.0, 13.0, 10.5) is None      # price <= stop
    assert recommend.reward_risk(None, 13.0, 9.0) is None
    print("ok  reward_risk ATR floor")


def test_target_cap_on_crashed_stock():
    # BMNR-like: price $15.5, 52w high $134 (dist -88.43%), ATR $1.2.
    tech = {"chandelier_stop": 14.26, "dist_52w_high_pct": -88.43, "atr": 1.2}
    target, stop = recommend.technical_target_stop(tech, 15.5, {"target_atr_mult": 10.0})
    assert stop == 14.26
    assert target is not None and abs(target - (15.5 + 12.0)) < 1e-9, target  # capped, not $134
    # Near its high, the 52w-high target survives untouched
    tech = {"chandelier_stop": 95.0, "dist_52w_high_pct": -3.0, "atr": 2.0}
    target, _ = recommend.technical_target_stop(tech, 100.0, {"target_atr_mult": 10.0})
    assert abs(target - 100.0 / 0.97) < 1e-6, target
    print("ok  technical_target_stop ATR cap")


def test_rank_winsorization():
    cfg = {"discover_w_rr": 1.0, "discover_w_score": 0.0, "discover_w_catalyst": 0.0,
           "discover_rr_cap": 10.0, "discover_top_n": 20, "catalyst_horizon_days": 60}
    records = [
        {"ticker": "ARTIFACT", "reward_risk": 665.0, "score": 50, "catalyst_days": 30},
        {"ticker": "REAL_A",   "reward_risk": 3.9,   "score": 50, "catalyst_days": 30},
        {"ticker": "REAL_B",   "reward_risk": 3.2,   "score": 50, "catalyst_days": 30},
        {"ticker": "THIN",     "reward_risk": 0.3,   "score": 50, "catalyst_days": 30},
    ]
    top = discover.rank_and_select(records, cfg)
    b = {r["ticker"]: r["benefit"] for r in top}
    # Pre-fix: 3.9:1 normalized against 665 -> benefit ~0.005, indistinguishable
    # from the 0.3:1 junk. Post-fix (capped at 10): it must clearly separate.
    assert b["REAL_A"] > 0.3, b
    assert b["REAL_A"] - b["THIN"] > 0.25, b
    assert b["ARTIFACT"] == max(b.values())  # still first, but no longer nukes the scale
    print("ok  rank_and_select winsorized R:R")


def test_business_precheck_knockouts():
    bank = shariah.business_precheck("X", info={"sector": "Financial Services",
                                                "industry": "Banks - Diversified"})
    assert bank["ok"] is False and bank["flags"], bank

    insurer = shariah.business_precheck("X", info={"sector": "Financial Services",
                                                   "industry": "Insurance - Property & Casualty"})
    assert insurer["ok"] is False, insurer

    tech = shariah.business_precheck("X", info={"sector": "Technology",
                                                "industry": "Semiconductors"})
    assert tech["ok"] is True and not tech["flags"], tech

    brewer = shariah.business_precheck("X", info={"sector": "Consumer Defensive",
                                                  "industry": "Beverages - Brewers"})
    assert brewer["ok"] is False, brewer

    unknown = shariah.business_precheck("X", info={})
    assert unknown["ok"] is None, unknown  # missing metadata = UNKNOWN, never a pass
    print("ok  business_precheck knockouts")


def test_classify_stricter_floor():
    # 2.5:1 with a dated catalyst: BUY-CANDIDATE under the old 2.0 swing floor,
    # RESEARCH under the 3.0 zero-edge floor.
    v, why = discover.classify(True, 2.5, 20, horizon=60, rr_floor=3.0)
    assert v == "RESEARCH" and "ASYMMETRY_GATE" in why, (v, why)
    v, _ = discover.classify(True, 3.9, 20, horizon=60, rr_floor=3.0)
    assert v == "LEAD", v  # discovery emits LEAD, never BUY-CANDIDATE (Change 2)
    v, _ = discover.classify(False, 3.9, 20, horizon=60, rr_floor=3.0)
    assert v == "AVOID", v
    print("ok  classify 3:1 floor for zero-edge ideas")


if __name__ == "__main__":
    test_reward_risk_atr_floor()
    test_target_cap_on_crashed_stock()
    test_rank_winsorization()
    test_business_precheck_knockouts()
    test_classify_stricter_floor()
    print("\nall fixes verified offline")
