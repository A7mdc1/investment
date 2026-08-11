---
ticker: IONQ
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $40.13 holding the uptrend (no breakdown on volume)"
entry_price: 40.13
stop_price: 36.23
stop_logic: "chandelier trail: HH22 $44.61 - 3x ATR $2.79 = $36.23 — exit when decline exceeds ~3 average daily ranges"
target_price: 45.97
target_logic: "T1 $45.97 = entry $40.13 + 1.5x R (R=$3.89); T2 $51.81 = entry + 3x R; structure ceiling = 52w high $84.64"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $790.7M; pass"
invalidation: "loses EMA20 $40.13 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
