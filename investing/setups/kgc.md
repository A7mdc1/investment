---
ticker: KGC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $24.69 holding the uptrend (no breakdown on volume)"
entry_price: 24.69
stop_price: 24.61
stop_logic: "chandelier trail: HH22 $27.65 - 3x ATR $1.01 = $24.61 — exit when decline exceeds ~3 average daily ranges"
target_price: 24.81
target_logic: "T1 $24.81 = entry $24.69 + 1.5x R (R=$0.08); T2 $24.93 = entry + 3x R; structure ceiling = 52w high $39.00"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $183.3M; pass"
invalidation: "loses EMA20 $24.69 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
