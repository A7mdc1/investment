---
ticker: ASND
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $234.79 holding the uptrend (no breakdown on volume)"
entry_price: 234.79
stop_price: 228.74
stop_logic: "chandelier trail: HH22 $246.40 - 3x ATR $5.89 = $228.74 — exit when decline exceeds ~3 average daily ranges"
target_price: 243.86
target_logic: "T1 $243.86 = entry $234.79 + 1.5x R (R=$6.05); T2 $252.93 = entry + 3x R; structure ceiling = 52w high $282.11"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $167.6M; pass"
invalidation: "loses EMA20 $234.79 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-26 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
