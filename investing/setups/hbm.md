---
ticker: HBM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $22.84 holding the uptrend (no breakdown on volume)"
entry_price: 22.84
stop_price: 21.20
stop_logic: "chandelier trail: HH22 $25.22 - 3x ATR $1.34 = $21.20 — exit when decline exceeds ~3 average daily ranges"
target_price: 25.29
target_logic: "T1 $25.29 = entry $22.84 + 1.5x R (R=$1.64); T2 $27.75 = entry + 3x R; structure ceiling = 52w high $32.14"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $106.1M; pass"
invalidation: "loses EMA20 $22.84 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-04 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
