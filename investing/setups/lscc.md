---
ticker: LSCC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $106.99 holding the uptrend (no breakdown on volume)"
entry_price: 106.99
stop_price: 102.94
stop_logic: "chandelier trail: HH22 $125.17 - 3x ATR $7.41 = $102.94 — exit when decline exceeds ~3 average daily ranges"
target_price: 113.06
target_logic: "T1 $113.06 = entry $106.99 + 1.5x R (R=$4.05); T2 $119.12 = entry + 3x R; structure ceiling = 52w high $156.97"
holding_window_days: 21
catalyst: "2027-02-08 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $294.4M; pass"
invalidation: "loses EMA20 $106.99 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
