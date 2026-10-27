---
ticker: ORCL-PD
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $41.91 holding the uptrend (no breakdown on volume)"
entry_price: 41.91
stop_price: 40.91
stop_logic: "chandelier trail: HH22 $45.35 - 3x ATR $1.48 = $40.91 — exit when decline exceeds ~3 average daily ranges"
target_price: 43.41
target_logic: "T1 $43.41 = entry $41.91 + 1.5x R (R=$1.00); T2 $44.90 = entry + 3x R; structure ceiling = 52w high $67.97"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $18.2M; pass"
invalidation: "loses EMA20 $41.91 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check inconclusive (no market cap) — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
