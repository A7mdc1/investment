---
ticker: TECK
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $62.89 holding the uptrend (no breakdown on volume)"
entry_price: 62.89
stop_price: 61.26
stop_logic: "chandelier trail: HH22 $68.10 - 3x ATR $2.28 = $61.26 — exit when decline exceeds ~3 average daily ranges"
target_price: 65.35
target_logic: "T1 $65.35 = entry $62.89 + 1.5x R (R=$1.64); T2 $67.80 = entry + 3x R; structure ceiling = 52w high $71.18"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $196.7M; pass"
invalidation: "loses EMA20 $62.89 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
