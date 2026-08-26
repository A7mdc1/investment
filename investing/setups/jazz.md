---
ticker: JAZZ
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $266.40 (52w high) on >1.2x 20d avg volume"
entry_price: 266.40
stop_price: 244.09
stop_logic: "chandelier trail: HH22 $266.38 - 3x ATR $7.43 = $244.09 — exit when decline exceeds ~3 average daily ranges"
target_price: 299.86
target_logic: "T1 $299.86 = entry $266.40 + 1.5x R (R=$22.31); T2 $333.33 = entry + 3x R; structure ceiling = 52w high $266.40"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $212.7M; pass"
invalidation: "closes back below the breakout level $266.40 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-26 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
