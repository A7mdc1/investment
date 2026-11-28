---
ticker: ASND
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $282.02 (52w high) on >1.2x 20d avg volume"
entry_price: 282.02
stop_price: 255.36
stop_logic: "chandelier trail: HH22 $279.75 - 3x ATR $8.13 = $255.36 — exit when decline exceeds ~3 average daily ranges"
target_price: 322.00
target_logic: "T1 $322.00 = entry $282.02 + 1.5x R (R=$26.65); T2 $361.98 = entry + 3x R; structure ceiling = 52w high $282.02"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $189.6M; pass"
invalidation: "closes back below the breakout level $282.02 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-28 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
