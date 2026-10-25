---
ticker: STLD
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $239.56 holding the uptrend (no breakdown on volume)"
entry_price: 239.56
stop_price: 226.07
stop_logic: "chandelier trail: HH22 $248.96 - 3x ATR $7.63 = $226.07 — exit when decline exceeds ~3 average daily ranges"
target_price: 259.79
target_logic: "T1 $259.79 = entry $239.56 + 1.5x R (R=$13.49); T2 $280.02 = entry + 3x R; structure ceiling = 52w high $287.54"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $227.1M; pass"
invalidation: "loses EMA20 $239.56 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-25 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
