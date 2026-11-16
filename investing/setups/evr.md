---
ticker: EVR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $286.45 holding the uptrend (no breakdown on volume)"
entry_price: 286.45
stop_price: 279.42
stop_logic: "chandelier trail: HH22 $315.00 - 3x ATR $11.86 = $279.42 — exit when decline exceeds ~3 average daily ranges"
target_price: 297.00
target_logic: "T1 $297.00 = entry $286.45 + 1.5x R (R=$7.03); T2 $307.55 = entry + 3x R; structure ceiling = 52w high $385.74"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $151.0M; pass"
invalidation: "loses EMA20 $286.45 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check FLAGGED: industry 'Capital Markets' matches 'capital markets' — core business fails screen
---

## Notes
Scaffolded 2026-11-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
