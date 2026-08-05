---
ticker: AA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $47.01 holding the uptrend (no breakdown on volume)"
entry_price: 47.01
stop_price: 45.15
stop_logic: "chandelier trail: HH22 $50.86 - 3x ATR $1.91 = $45.15 — exit when decline exceeds ~3 average daily ranges"
target_price: 49.81
target_logic: "T1 $49.81 = entry $47.01 + 1.5x R (R=$1.87); T2 $52.61 = entry + 3x R; structure ceiling = 52w high $84.33"
holding_window_days: 21
catalyst: "2026-10-15 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $232.6M; pass"
invalidation: "loses EMA20 $47.01 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-05 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
