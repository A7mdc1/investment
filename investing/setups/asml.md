---
ticker: ASML
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $1553.87 holding the uptrend (no breakdown on volume)"
entry_price: 1553.87
stop_price: 1491.75
stop_logic: "chandelier trail: HH22 $1690.10 - 3x ATR $66.12 = $1491.75 — exit when decline exceeds ~3 average daily ranges"
target_price: 1647.05
target_logic: "T1 $1647.05 = entry $1553.87 + 1.5x R (R=$62.12); T2 $1740.23 = entry + 3x R; structure ceiling = 52w high $1993.55"
holding_window_days: 21
catalyst: "2027-01-27 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2574.9M; pass"
invalidation: "loses EMA20 $1553.87 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
