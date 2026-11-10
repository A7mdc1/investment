---
ticker: FTI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $67.05 holding the uptrend (no breakdown on volume)"
entry_price: 67.05
stop_price: 64.51
stop_logic: "chandelier trail: HH22 $72.36 - 3x ATR $2.62 = $64.51 — exit when decline exceeds ~3 average daily ranges"
target_price: 70.87
target_logic: "T1 $70.87 = entry $67.05 + 1.5x R (R=$2.54); T2 $74.68 = entry + 3x R; structure ceiling = 52w high $80.75"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $206.0M; pass"
invalidation: "loses EMA20 $67.05 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
