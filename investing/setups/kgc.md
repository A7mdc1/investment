---
ticker: KGC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $24.94 holding the uptrend (no breakdown on volume)"
entry_price: 24.94
stop_price: 24.62
stop_logic: "chandelier trail: HH22 $27.66 - 3x ATR $1.01 = $24.62 — exit when decline exceeds ~3 average daily ranges"
target_price: 25.42
target_logic: "T1 $25.42 = entry $24.94 + 1.5x R (R=$0.32); T2 $25.91 = entry + 3x R; structure ceiling = 52w high $39.00"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $185.5M; pass"
invalidation: "loses EMA20 $24.94 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
