---
ticker: NTAP
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $188.90 holding the uptrend (no breakdown on volume)"
entry_price: 188.90
stop_price: 182.87
stop_logic: "chandelier trail: HH22 $207.96 - 3x ATR $8.36 = $182.87 — exit when decline exceeds ~3 average daily ranges"
target_price: 197.96
target_logic: "T1 $197.96 = entry $188.90 + 1.5x R (R=$6.04); T2 $207.02 = entry + 3x R; structure ceiling = 52w high $209.17"
holding_window_days: 21
catalyst: "2026-12-01 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $448.5M; pass"
invalidation: "loses EMA20 $188.90 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
