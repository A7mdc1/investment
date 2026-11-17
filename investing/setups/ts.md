---
ticker: TS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $59.25 holding the uptrend (no breakdown on volume)"
entry_price: 59.25
stop_price: 56.89
stop_logic: "chandelier trail: HH22 $62.22 - 3x ATR $1.78 = $56.89 — exit when decline exceeds ~3 average daily ranges"
target_price: 62.79
target_logic: "T1 $62.79 = entry $59.25 + 1.5x R (R=$2.36); T2 $66.33 = entry + 3x R; structure ceiling = 52w high $64.62"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $63.9M; pass"
invalidation: "loses EMA20 $59.25 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
