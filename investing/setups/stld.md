---
ticker: STLD
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $237.57 holding the uptrend (no breakdown on volume)"
entry_price: 237.57
stop_price: 228.31
stop_logic: "chandelier trail: HH22 $259.24 - 3x ATR $10.31 = $228.31 — exit when decline exceeds ~3 average daily ranges"
target_price: 251.47
target_logic: "T1 $251.47 = entry $237.57 + 1.5x R (R=$9.26); T2 $265.36 = entry + 3x R; structure ceiling = 52w high $287.51"
holding_window_days: 21
catalyst: "2027-01-25 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $252.0M; pass"
invalidation: "loses EMA20 $237.57 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
