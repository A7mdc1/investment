---
ticker: SMCI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $30.28 holding the uptrend (no breakdown on volume)"
entry_price: 30.28
stop_price: 30.10
stop_logic: "chandelier trail: HH22 $37.23 - 3x ATR $2.38 = $30.10 — exit when decline exceeds ~3 average daily ranges"
target_price: 30.54
target_logic: "T1 $30.54 = entry $30.28 + 1.5x R (R=$0.18); T2 $30.81 = entry + 3x R; structure ceiling = 52w high $58.82"
holding_window_days: 21
catalyst: "2026-11-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1597.1M; pass"
invalidation: "loses EMA20 $30.28 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
