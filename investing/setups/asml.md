---
ticker: ASML
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $1568.90 holding the uptrend (no breakdown on volume)"
entry_price: 1568.90
stop_price: 1525.28
stop_logic: "chandelier trail: HH22 $1732.21 - 3x ATR $68.98 = $1525.28 — exit when decline exceeds ~3 average daily ranges"
target_price: 1634.33
target_logic: "T1 $1634.33 = entry $1568.90 + 1.5x R (R=$43.62); T2 $1699.76 = entry + 3x R; structure ceiling = 52w high $1994.64"
holding_window_days: 21
catalyst: "2027-01-27 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2603.3M; pass"
invalidation: "loses EMA20 $1568.90 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
