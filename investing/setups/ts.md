---
ticker: TS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $58.11 holding the uptrend (no breakdown on volume)"
entry_price: 58.11
stop_price: 56.18
stop_logic: "chandelier trail: HH22 $61.35 - 3x ATR $1.72 = $56.18 — exit when decline exceeds ~3 average daily ranges"
target_price: 60.99
target_logic: "T1 $60.99 = entry $58.11 + 1.5x R (R=$1.92); T2 $63.87 = entry + 3x R; structure ceiling = 52w high $64.57"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $61.0M; pass"
invalidation: "loses EMA20 $58.11 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-05 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
