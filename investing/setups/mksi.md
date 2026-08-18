---
ticker: MKSI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $313.27 holding the uptrend (no breakdown on volume)"
entry_price: 313.27
stop_price: 303.59
stop_logic: "chandelier trail: HH22 $374.12 - 3x ATR $23.51 = $303.59 — exit when decline exceeds ~3 average daily ranges"
target_price: 327.79
target_logic: "T1 $327.79 = entry $313.27 + 1.5x R (R=$9.68); T2 $342.31 = entry + 3x R; structure ceiling = 52w high $447.90"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $469.4M; pass"
invalidation: "loses EMA20 $313.27 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-18 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
