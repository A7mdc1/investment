---
ticker: KGC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $23.77 holding the uptrend (no breakdown on volume)"
entry_price: 23.77
stop_price: 22.15
stop_logic: "chandelier trail: HH22 $25.12 - 3x ATR $0.99 = $22.15 — exit when decline exceeds ~3 average daily ranges"
target_price: 26.19
target_logic: "T1 $26.19 = entry $23.77 + 1.5x R (R=$1.61); T2 $28.61 = entry + 3x R; structure ceiling = 52w high $39.01"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $172.8M; pass"
invalidation: "loses EMA20 $23.77 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-31 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
