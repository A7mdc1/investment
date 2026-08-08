---
ticker: JAZZ
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $265.04 (52w high) on >1.2x 20d avg volume"
entry_price: 265.04
stop_price: 243.21
stop_logic: "chandelier trail: HH22 $265.05 - 3x ATR $7.28 = $243.21 — exit when decline exceeds ~3 average daily ranges"
target_price: 297.78
target_logic: "T1 $297.78 = entry $265.04 + 1.5x R (R=$21.83); T2 $330.53 = entry + 3x R; structure ceiling = 52w high $265.04"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $198.5M; pass"
invalidation: "closes back below the breakout level $265.04 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-08 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
