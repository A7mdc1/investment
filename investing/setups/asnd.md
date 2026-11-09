---
ticker: ASND
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $246.51 holding the uptrend (no breakdown on volume)"
entry_price: 246.51
stop_price: 240.66
stop_logic: "chandelier trail: HH22 $258.46 - 3x ATR $5.93 = $240.66 — exit when decline exceeds ~3 average daily ranges"
target_price: 255.27
target_logic: "T1 $255.27 = entry $246.51 + 1.5x R (R=$5.84); T2 $264.04 = entry + 3x R; structure ceiling = 52w high $282.08"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $147.2M; pass"
invalidation: "loses EMA20 $246.51 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-09 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
