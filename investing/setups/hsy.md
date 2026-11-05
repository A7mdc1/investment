---
ticker: HSY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $168.07 holding the uptrend (no breakdown on volume)"
entry_price: 168.07
stop_price: 165.02
stop_logic: "chandelier trail: HH22 $178.55 - 3x ATR $4.51 = $165.02 — exit when decline exceeds ~3 average daily ranges"
target_price: 172.64
target_logic: "T1 $172.64 = entry $168.07 + 1.5x R (R=$3.05); T2 $177.21 = entry + 3x R; structure ceiling = 52w high $235.65"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $279.0M; pass"
invalidation: "loses EMA20 $168.07 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-05 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
