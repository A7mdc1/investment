---
ticker: PNFP
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $99.79 holding the uptrend (no breakdown on volume)"
entry_price: 99.79
stop_price: 99.58
stop_logic: "chandelier trail: HH22 $107.10 - 3x ATR $2.51 = $99.58 — exit when decline exceeds ~3 average daily ranges"
target_price: 100.11
target_logic: "T1 $100.11 = entry $99.79 + 1.5x R (R=$0.21); T2 $100.43 = entry + 3x R; structure ceiling = 52w high $109.86"
holding_window_days: 21
catalyst: "2027-01-27 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $109.2M; pass"
invalidation: "loses EMA20 $99.79 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check FLAGGED: industry 'Banks - Regional' matches 'bank' — core business fails screen
---

## Notes
Scaffolded 2026-11-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
