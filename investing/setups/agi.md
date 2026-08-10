---
ticker: AGI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $30.38 holding the uptrend (no breakdown on volume)"
entry_price: 30.38
stop_price: 30.01
stop_logic: "chandelier trail: HH22 $33.76 - 3x ATR $1.25 = $30.01 — exit when decline exceeds ~3 average daily ranges"
target_price: 30.94
target_logic: "T1 $30.94 = entry $30.38 + 1.5x R (R=$0.37); T2 $31.50 = entry + 3x R; structure ceiling = 52w high $55.33"
holding_window_days: 21
catalyst: "2026-10-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $147.5M; pass"
invalidation: "loses EMA20 $30.38 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
