---
ticker: YUMC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $47.14 holding the uptrend (no breakdown on volume)"
entry_price: 47.14
stop_price: 46.61
stop_logic: "chandelier trail: HH22 $49.73 - 3x ATR $1.04 = $46.61 — exit when decline exceeds ~3 average daily ranges"
target_price: 47.95
target_logic: "T1 $47.95 = entry $47.14 + 1.5x R (R=$0.54); T2 $48.76 = entry + 3x R; structure ceiling = 52w high $57.72"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $71.8M; pass"
invalidation: "loses EMA20 $47.14 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-22 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
