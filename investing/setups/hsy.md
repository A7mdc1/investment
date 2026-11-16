---
ticker: HSY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $171.95 holding the uptrend (no breakdown on volume)"
entry_price: 171.95
stop_price: 164.38
stop_logic: "chandelier trail: HH22 $179.83 - 3x ATR $5.15 = $164.38 — exit when decline exceeds ~3 average daily ranges"
target_price: 183.30
target_logic: "T1 $183.30 = entry $171.95 + 1.5x R (R=$7.57); T2 $194.66 = entry + 3x R; structure ceiling = 52w high $235.81"
holding_window_days: 21
catalyst: "2027-02-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $336.4M; pass"
invalidation: "loses EMA20 $171.95 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
