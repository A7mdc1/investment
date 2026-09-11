---
ticker: SMCIP
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $62.86 holding the uptrend (no breakdown on volume)"
entry_price: 62.86
stop_price: 59.94
stop_logic: "chandelier trail: HH22 $70.21 - 3x ATR $3.42 = $59.94 — exit when decline exceeds ~3 average daily ranges"
target_price: 67.25
target_logic: "T1 $67.25 = entry $62.86 + 1.5x R (R=$2.93); T2 $71.64 = entry + 3x R; structure ceiling = 52w high $70.21"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $34.0M; pass"
invalidation: "loses EMA20 $62.86 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check inconclusive (no market cap) — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
