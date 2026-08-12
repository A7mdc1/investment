---
ticker: LRCX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $312.56 holding the uptrend (no breakdown on volume)"
entry_price: 312.56
stop_price: 288.11
stop_logic: "chandelier trail: HH22 $357.25 - 3x ATR $23.05 = $288.11 — exit when decline exceeds ~3 average daily ranges"
target_price: 349.24
target_logic: "T1 $349.24 = entry $312.56 + 1.5x R (R=$24.46); T2 $385.93 = entry + 3x R; structure ceiling = 52w high $438.29"
holding_window_days: 21
catalyst: "2026-10-21 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $3239.7M; pass"
invalidation: "loses EMA20 $312.56 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
