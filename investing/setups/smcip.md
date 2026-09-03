---
ticker: SMCIP
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $60.72 holding the uptrend (no breakdown on volume)"
entry_price: 60.72
stop_price: 60.27
stop_logic: "chandelier trail: HH22 $70.21 - 3x ATR $3.31 = $60.27 — exit when decline exceeds ~3 average daily ranges"
target_price: 61.39
target_logic: "T1 $61.39 = entry $60.72 + 1.5x R (R=$0.45); T2 $62.07 = entry + 3x R; structure ceiling = 52w high $70.20"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $35.9M; pass"
invalidation: "loses EMA20 $60.72 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check inconclusive (no market cap) — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-03 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
