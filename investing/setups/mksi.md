---
ticker: MKSI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $314.38 holding the uptrend (no breakdown on volume)"
entry_price: 314.38
stop_price: 303.15
stop_logic: "chandelier trail: HH22 $374.12 - 3x ATR $23.66 = $303.15 — exit when decline exceeds ~3 average daily ranges"
target_price: 331.24
target_logic: "T1 $331.24 = entry $314.38 + 1.5x R (R=$11.24); T2 $348.09 = entry + 3x R; structure ceiling = 52w high $447.74"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $484.3M; pass"
invalidation: "loses EMA20 $314.38 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
