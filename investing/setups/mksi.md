---
ticker: MKSI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $313.74 holding the uptrend (no breakdown on volume)"
entry_price: 313.74
stop_price: 283.54
stop_logic: "chandelier trail: HH22 $349.02 - 3x ATR $21.83 = $283.54 — exit when decline exceeds ~3 average daily ranges"
target_price: 359.04
target_logic: "T1 $359.04 = entry $313.74 + 1.5x R (R=$30.20); T2 $404.35 = entry + 3x R; structure ceiling = 52w high $447.81"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $454.1M; pass"
invalidation: "loses EMA20 $313.74 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
