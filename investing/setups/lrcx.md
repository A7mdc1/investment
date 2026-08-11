---
ticker: LRCX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $310.81 holding the uptrend (no breakdown on volume)"
entry_price: 310.81
stop_price: 287.38
stop_logic: "chandelier trail: HH22 $357.25 - 3x ATR $23.29 = $287.38 — exit when decline exceeds ~3 average daily ranges"
target_price: 345.97
target_logic: "T1 $345.97 = entry $310.81 + 1.5x R (R=$23.44); T2 $381.12 = entry + 3x R; structure ceiling = 52w high $438.50"
holding_window_days: 21
catalyst: "2026-10-21 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $3288.3M; pass"
invalidation: "loses EMA20 $310.81 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
