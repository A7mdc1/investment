---
ticker: EVR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $279.77 holding the uptrend (no breakdown on volume)"
entry_price: 279.77
stop_price: 278.41
stop_logic: "chandelier trail: HH22 $315.00 - 3x ATR $12.20 = $278.41 — exit when decline exceeds ~3 average daily ranges"
target_price: 281.82
target_logic: "T1 $281.82 = entry $279.77 + 1.5x R (R=$1.36); T2 $283.86 = entry + 3x R; structure ceiling = 52w high $385.67"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $171.7M; pass"
invalidation: "loses EMA20 $279.77 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check FLAGGED: industry 'Capital Markets' matches 'capital markets' — core business fails screen
---

## Notes
Scaffolded 2026-11-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
