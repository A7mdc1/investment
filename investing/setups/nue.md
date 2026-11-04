---
ticker: NUE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $263.72 holding the uptrend (no breakdown on volume)"
entry_price: 263.72
stop_price: 262.11
stop_logic: "chandelier trail: HH22 $287.70 - 3x ATR $8.53 = $262.11 — exit when decline exceeds ~3 average daily ranges"
target_price: 266.14
target_logic: "T1 $266.14 = entry $263.72 + 1.5x R (R=$1.61); T2 $268.56 = entry + 3x R; structure ceiling = 52w high $287.83"
holding_window_days: 21
catalyst: "2027-01-25 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $346.3M; pass"
invalidation: "loses EMA20 $263.72 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-04 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
