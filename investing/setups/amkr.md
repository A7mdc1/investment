---
ticker: AMKR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $57.52 holding the uptrend (no breakdown on volume)"
entry_price: 57.52
stop_price: 56.82
stop_logic: "chandelier trail: HH22 $72.40 - 3x ATR $5.19 = $56.82 — exit when decline exceeds ~3 average daily ranges"
target_price: 58.58
target_logic: "T1 $58.58 = entry $57.52 + 1.5x R (R=$0.70); T2 $59.63 = entry + 3x R; structure ceiling = 52w high $96.73"
holding_window_days: 21
catalyst: "2026-10-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $321.3M; pass"
invalidation: "loses EMA20 $57.52 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
