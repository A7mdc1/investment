---
ticker: ASTS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $67.94 holding the uptrend (no breakdown on volume)"
entry_price: 67.94
stop_price: 59.82
stop_logic: "chandelier trail: HH22 $75.08 - 3x ATR $5.09 = $59.82 — exit when decline exceeds ~3 average daily ranges"
target_price: 80.12
target_logic: "T1 $80.12 = entry $67.94 + 1.5x R (R=$8.12); T2 $92.29 = entry + 3x R; structure ceiling = 52w high $133.86"
holding_window_days: 21
catalyst: "2026-11-09 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $761.3M; pass"
invalidation: "loses EMA20 $67.94 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
