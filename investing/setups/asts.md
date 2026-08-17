---
ticker: ASTS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $68.37 holding the uptrend (no breakdown on volume)"
entry_price: 68.37
stop_price: 59.51
stop_logic: "chandelier trail: HH22 $75.08 - 3x ATR $5.19 = $59.51 — exit when decline exceeds ~3 average daily ranges"
target_price: 81.67
target_logic: "T1 $81.67 = entry $68.37 + 1.5x R (R=$8.87); T2 $94.97 = entry + 3x R; structure ceiling = 52w high $133.77"
holding_window_days: 21
catalyst: "2026-11-09 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $805.8M; pass"
invalidation: "loses EMA20 $68.37 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
