---
ticker: CORZ
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $22.54 holding the uptrend (no breakdown on volume)"
entry_price: 22.54
stop_price: 20.09
stop_logic: "chandelier trail: HH22 $26.07 - 3x ATR $1.99 = $20.09 — exit when decline exceeds ~3 average daily ranges"
target_price: 26.22
target_logic: "T1 $26.22 = entry $22.54 + 1.5x R (R=$2.45); T2 $29.90 = entry + 3x R; structure ceiling = 52w high $30.44"
holding_window_days: 21
catalyst: "2026-10-23 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $264.8M; pass"
invalidation: "loses EMA20 $22.54 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-30 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
