---
ticker: VICR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $229.72 holding the uptrend (no breakdown on volume)"
entry_price: 229.72
stop_price: 197.79
stop_logic: "chandelier trail: HH22 $255.74 - 3x ATR $19.32 = $197.79 — exit when decline exceeds ~3 average daily ranges"
target_price: 277.61
target_logic: "T1 $277.61 = entry $229.72 + 1.5x R (R=$31.93); T2 $325.49 = entry + 3x R; structure ceiling = 52w high $382.67"
holding_window_days: 21
catalyst: "2026-10-20 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $181.3M; pass"
invalidation: "loses EMA20 $229.72 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-18 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
