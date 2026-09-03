---
ticker: FRO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $45.96 (52w high) on >1.2x 20d avg volume"
entry_price: 45.96
stop_price: 41.28
stop_logic: "chandelier trail: HH22 $45.95 - 3x ATR $1.56 = $41.28 — exit when decline exceeds ~3 average daily ranges"
target_price: 52.97
target_logic: "T1 $52.97 = entry $45.96 + 1.5x R (R=$4.68); T2 $59.99 = entry + 3x R; structure ceiling = 52w high $45.96"
holding_window_days: 21
catalyst: "2026-11-30 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $89.3M; pass"
invalidation: "closes back below the breakout level $45.96 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-03 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
