---
ticker: ORCL-PD
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $40.46 holding the uptrend (no breakdown on volume)"
entry_price: 40.46
stop_price: 39.51
stop_logic: "chandelier trail: HH22 $45.25 - 3x ATR $1.91 = $39.51 — exit when decline exceeds ~3 average daily ranges"
target_price: 41.87
target_logic: "T1 $41.87 = entry $40.46 + 1.5x R (R=$0.94); T2 $43.29 = entry + 3x R; structure ceiling = 52w high $67.92"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $30.9M; pass"
invalidation: "loses EMA20 $40.46 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check inconclusive (no market cap) — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
