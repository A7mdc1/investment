---
ticker: STX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $877.76 holding the uptrend (no breakdown on volume)"
entry_price: 877.76
stop_price: 792.91
stop_logic: "chandelier trail: HH22 $1013.99 - 3x ATR $73.69 = $792.91 — exit when decline exceeds ~3 average daily ranges"
target_price: 1005.03
target_logic: "T1 $1005.03 = entry $877.76 + 1.5x R (R=$84.85); T2 $1132.30 = entry + 3x R; structure ceiling = 52w high $1144.59"
holding_window_days: 21
catalyst: "2026-10-27 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $4513.9M; pass"
invalidation: "loses EMA20 $877.76 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-18 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
