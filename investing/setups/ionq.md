---
ticker: IONQ
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $41.15 holding the uptrend (no breakdown on volume)"
entry_price: 41.15
stop_price: 39.53
stop_logic: "chandelier trail: HH22 $47.95 - 3x ATR $2.81 = $39.53 — exit when decline exceeds ~3 average daily ranges"
target_price: 43.59
target_logic: "T1 $43.59 = entry $41.15 + 1.5x R (R=$1.62); T2 $46.02 = entry + 3x R; structure ceiling = 52w high $84.59"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $808.8M; pass"
invalidation: "loses EMA20 $41.15 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
