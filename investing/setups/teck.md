---
ticker: TECK
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $62.58 holding the uptrend (no breakdown on volume)"
entry_price: 62.58
stop_price: 59.10
stop_logic: "chandelier trail: HH22 $66.64 - 3x ATR $2.51 = $59.10 — exit when decline exceeds ~3 average daily ranges"
target_price: 67.80
target_logic: "T1 $67.80 = entry $62.58 + 1.5x R (R=$3.48); T2 $73.02 = entry + 3x R; structure ceiling = 52w high $72.43"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $175.0M; pass"
invalidation: "loses EMA20 $62.58 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
