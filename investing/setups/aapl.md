---
ticker: AAPL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $361.01 (52w high) on >1.2x 20d avg volume"
entry_price: 361.01
stop_price: 336.52
stop_logic: "chandelier trail: HH22 $360.83 - 3x ATR $8.10 = $336.52 — exit when decline exceeds ~3 average daily ranges"
target_price: 397.75
target_logic: "T1 $397.75 = entry $361.01 + 1.5x R (R=$24.49); T2 $434.49 = entry + 3x R; structure ceiling = 52w high $361.01"
holding_window_days: 21
catalyst: "2027-01-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $16273.8M; pass"
invalidation: "closes back below the breakout level $361.01 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-18 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
