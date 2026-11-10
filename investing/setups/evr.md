---
ticker: EVR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $282.20 holding the uptrend (no breakdown on volume)"
entry_price: 282.20
stop_price: 277.27
stop_logic: "chandelier trail: HH22 $315.00 - 3x ATR $12.58 = $277.27 — exit when decline exceeds ~3 average daily ranges"
target_price: 289.60
target_logic: "T1 $289.60 = entry $282.20 + 1.5x R (R=$4.94); T2 $297.01 = entry + 3x R; structure ceiling = 52w high $385.30"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $167.4M; pass"
invalidation: "loses EMA20 $282.20 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check FLAGGED: industry 'Capital Markets' matches 'capital markets' — core business fails screen
---

## Notes
Scaffolded 2026-11-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
