---
ticker: IONQ
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $41.66 holding the uptrend (no breakdown on volume)"
entry_price: 41.66
stop_price: 39.57
stop_logic: "chandelier trail: HH22 $47.94 - 3x ATR $2.79 = $39.57 — exit when decline exceeds ~3 average daily ranges"
target_price: 44.79
target_logic: "T1 $44.79 = entry $41.66 + 1.5x R (R=$2.09); T2 $47.92 = entry + 3x R; structure ceiling = 52w high $84.58"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $810.9M; pass"
invalidation: "loses EMA20 $41.66 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
