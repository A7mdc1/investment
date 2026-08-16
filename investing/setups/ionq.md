---
ticker: IONQ
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $41.59 holding the uptrend (no breakdown on volume)"
entry_price: 41.59
stop_price: 39.57
stop_logic: "chandelier trail: HH22 $47.94 - 3x ATR $2.79 = $39.57 — exit when decline exceeds ~3 average daily ranges"
target_price: 44.63
target_logic: "T1 $44.63 = entry $41.59 + 1.5x R (R=$2.02); T2 $47.66 = entry + 3x R; structure ceiling = 52w high $84.57"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $825.7M; pass"
invalidation: "loses EMA20 $41.59 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
