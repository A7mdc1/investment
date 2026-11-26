---
ticker: AAPL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $360.99 (52w high) on >1.2x 20d avg volume"
entry_price: 360.99
stop_price: 333.35
stop_logic: "chandelier trail: HH22 $360.83 - 3x ATR $9.16 = $333.35 — exit when decline exceeds ~3 average daily ranges"
target_price: 402.46
target_logic: "T1 $402.46 = entry $360.99 + 1.5x R (R=$27.64); T2 $443.93 = entry + 3x R; structure ceiling = 52w high $360.99"
holding_window_days: 21
catalyst: "2027-01-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $17908.9M; pass"
invalidation: "closes back below the breakout level $360.99 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-26 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
