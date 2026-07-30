---
ticker: HBM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $22.54 holding the uptrend (no breakdown on volume)"
entry_price: 22.54
stop_price: 20.05
stop_logic: "chandelier trail: HH22 $24.01 - 3x ATR $1.32 = $20.05 — exit when decline exceeds ~3 average daily ranges"
target_price: 26.27
target_logic: "T1 $26.27 = entry $22.54 + 1.5x R (R=$2.49); T2 $30.01 = entry + 3x R; structure ceiling = 52w high $32.13"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $105.6M; pass"
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
