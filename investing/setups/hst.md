---
ticker: HST
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $26.19 (52w high) on >1.2x 20d avg volume"
entry_price: 26.19
stop_price: 24.25
stop_logic: "chandelier trail: HH22 $26.19 - 3x ATR $0.65 = $24.25 — exit when decline exceeds ~3 average daily ranges"
target_price: 29.11
target_logic: "T1 $29.11 = entry $26.19 + 1.5x R (R=$1.94); T2 $32.02 = entry + 3x R; structure ceiling = 52w high $26.19"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $235.9M; pass"
invalidation: "closes back below the breakout level $26.19 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
