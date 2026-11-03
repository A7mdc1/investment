---
ticker: HSY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $166.75 holding the uptrend (no breakdown on volume)"
entry_price: 166.75
stop_price: 163.22
stop_logic: "chandelier trail: HH22 $175.75 - 3x ATR $4.18 = $163.22 — exit when decline exceeds ~3 average daily ranges"
target_price: 172.04
target_logic: "T1 $172.04 = entry $166.75 + 1.5x R (R=$3.53); T2 $177.33 = entry + 3x R; structure ceiling = 52w high $235.77"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $265.5M; pass"
invalidation: "loses EMA20 $166.75 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-03 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
