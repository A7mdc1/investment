---
ticker: STX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $850.55 holding the uptrend (no breakdown on volume)"
entry_price: 850.55
stop_price: 764.26
stop_logic: "chandelier trail: HH22 $998.49 - 3x ATR $78.08 = $764.26 — exit when decline exceeds ~3 average daily ranges"
target_price: 979.98
target_logic: "T1 $979.98 = entry $850.55 + 1.5x R (R=$86.29); T2 $1109.42 = entry + 3x R; structure ceiling = 52w high $1144.49"
holding_window_days: 21
catalyst: "2026-10-27 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $4252.7M; pass"
invalidation: "loses EMA20 $850.55 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-29 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
