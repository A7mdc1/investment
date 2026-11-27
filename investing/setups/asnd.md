---
ticker: ASND
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $282.01 (52w high) on >1.2x 20d avg volume"
entry_price: 282.01
stop_price: 254.94
stop_logic: "chandelier trail: HH22 $279.25 - 3x ATR $8.10 = $254.94 — exit when decline exceeds ~3 average daily ranges"
target_price: 322.62
target_logic: "T1 $322.62 = entry $282.01 + 1.5x R (R=$27.07); T2 $363.23 = entry + 3x R; structure ceiling = 52w high $282.01"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $188.8M; pass"
invalidation: "closes back below the breakout level $282.01 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
