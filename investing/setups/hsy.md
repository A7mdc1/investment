---
ticker: HSY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $166.20 holding the uptrend (no breakdown on volume)"
entry_price: 166.20
stop_price: 163.94
stop_logic: "chandelier trail: HH22 $175.75 - 3x ATR $3.94 = $163.94 — exit when decline exceeds ~3 average daily ranges"
target_price: 169.59
target_logic: "T1 $169.59 = entry $166.20 + 1.5x R (R=$2.26); T2 $172.97 = entry + 3x R; structure ceiling = 52w high $235.91"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $267.8M; pass"
invalidation: "loses EMA20 $166.20 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-31 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
