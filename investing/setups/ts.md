---
ticker: TS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $58.67 holding the uptrend (no breakdown on volume)"
entry_price: 58.67
stop_price: 55.98
stop_logic: "chandelier trail: HH22 $61.35 - 3x ATR $1.79 = $55.98 — exit when decline exceeds ~3 average daily ranges"
target_price: 62.70
target_logic: "T1 $62.70 = entry $58.67 + 1.5x R (R=$2.69); T2 $66.73 = entry + 3x R; structure ceiling = 52w high $64.59"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $66.8M; pass"
invalidation: "loses EMA20 $58.67 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
