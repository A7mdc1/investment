---
ticker: VICR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $225.96 holding the uptrend (no breakdown on volume)"
entry_price: 225.96
stop_price: 188.30
stop_logic: "chandelier trail: HH22 $249.81 - 3x ATR $20.50 = $188.30 — exit when decline exceeds ~3 average daily ranges"
target_price: 282.44
target_logic: "T1 $282.44 = entry $225.96 + 1.5x R (R=$37.65); T2 $338.92 = entry + 3x R; structure ceiling = 52w high $382.92"
holding_window_days: 21
catalyst: "2026-10-20 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $188.5M; pass"
invalidation: "loses EMA20 $225.96 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
