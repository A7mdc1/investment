---
ticker: FSLR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $223.73 holding the uptrend (no breakdown on volume)"
entry_price: 223.73
stop_price: 218.36
stop_logic: "chandelier trail: HH22 $253.00 - 3x ATR $11.55 = $218.36 — exit when decline exceeds ~3 average daily ranges"
target_price: 231.79
target_logic: "T1 $231.79 = entry $223.73 + 1.5x R (R=$5.37); T2 $239.84 = entry + 3x R; structure ceiling = 52w high $321.11"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $485.9M; pass"
invalidation: "loses EMA20 $223.73 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
