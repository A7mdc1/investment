---
ticker: COHR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $212.70 holding the uptrend (no breakdown on volume)"
entry_price: 212.70
stop_price: 172.13
stop_logic: "chandelier trail: HH22 $246.90 - 3x ATR $24.92 = $172.13 — exit when decline exceeds ~3 average daily ranges"
target_price: 273.56
target_logic: "T1 $273.56 = entry $212.70 + 1.5x R (R=$40.57); T2 $334.42 = entry + 3x R; structure ceiling = 52w high $439.62"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2167.0M; pass"
invalidation: "loses EMA20 $212.70 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-25 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
