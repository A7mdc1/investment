---
ticker: FSLR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $217.14 holding the uptrend (no breakdown on volume)"
entry_price: 217.14
stop_price: 209.66
stop_logic: "chandelier trail: HH22 $242.17 - 3x ATR $10.84 = $209.66 — exit when decline exceeds ~3 average daily ranges"
target_price: 228.36
target_logic: "T1 $228.36 = entry $217.14 + 1.5x R (R=$7.48); T2 $239.58 = entry + 3x R; structure ceiling = 52w high $321.07"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $409.3M; pass"
invalidation: "loses EMA20 $217.14 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-03 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
