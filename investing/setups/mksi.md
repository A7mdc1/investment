---
ticker: MKSI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $313.84 holding the uptrend (no breakdown on volume)"
entry_price: 313.84
stop_price: 303.30
stop_logic: "chandelier trail: HH22 $374.12 - 3x ATR $23.61 = $303.30 — exit when decline exceeds ~3 average daily ranges"
target_price: 329.67
target_logic: "T1 $329.67 = entry $313.84 + 1.5x R (R=$10.55); T2 $345.49 = entry + 3x R; structure ceiling = 52w high $447.55"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $465.7M; pass"
invalidation: "loses EMA20 $313.84 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
