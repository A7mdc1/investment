---
ticker: SMTC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $146.84 holding the uptrend (no breakdown on volume)"
entry_price: 146.84
stop_price: 135.05
stop_logic: "chandelier trail: HH22 $170.43 - 3x ATR $11.79 = $135.05 — exit when decline exceeds ~3 average daily ranges"
target_price: 164.52
target_logic: "T1 $164.52 = entry $146.84 + 1.5x R (R=$11.79); T2 $182.20 = entry + 3x R; structure ceiling = 52w high $177.31"
holding_window_days: 21
catalyst: "2026-11-23 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $473.6M; pass"
invalidation: "loses EMA20 $146.84 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
