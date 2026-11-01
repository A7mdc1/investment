---
ticker: STLD
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $243.03 holding the uptrend (no breakdown on volume)"
entry_price: 243.03
stop_price: 229.12
stop_logic: "chandelier trail: HH22 $254.13 - 3x ATR $8.34 = $229.12 — exit when decline exceeds ~3 average daily ranges"
target_price: 263.89
target_logic: "T1 $263.89 = entry $243.03 + 1.5x R (R=$13.91); T2 $284.76 = entry + 3x R; structure ceiling = 52w high $287.29"
holding_window_days: 21
catalyst: "2027-01-25 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $237.9M; pass"
invalidation: "loses EMA20 $243.03 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-01 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
