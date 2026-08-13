---
ticker: TECK
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $62.81 holding the uptrend (no breakdown on volume)"
entry_price: 62.81
stop_price: 61.07
stop_logic: "chandelier trail: HH22 $68.10 - 3x ATR $2.34 = $61.07 — exit when decline exceeds ~3 average daily ranges"
target_price: 65.43
target_logic: "T1 $65.43 = entry $62.81 + 1.5x R (R=$1.74); T2 $68.04 = entry + 3x R; structure ceiling = 52w high $71.15"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $200.6M; pass"
invalidation: "loses EMA20 $62.81 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
