---
ticker: STX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $861.16 holding the uptrend (no breakdown on volume)"
entry_price: 861.16
stop_price: 760.97
stop_logic: "chandelier trail: HH22 $990.61 - 3x ATR $76.55 = $760.97 — exit when decline exceeds ~3 average daily ranges"
target_price: 1011.44
target_logic: "T1 $1011.44 = entry $861.16 + 1.5x R (R=$100.19); T2 $1161.72 = entry + 3x R; structure ceiling = 52w high $1143.88"
holding_window_days: 21
catalyst: "2026-10-27 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $4649.3M; pass"
invalidation: "loses EMA20 $861.16 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
