---
ticker: AAPL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $360.65 (52w high) on >1.2x 20d avg volume"
entry_price: 360.65
stop_price: 336.11
stop_logic: "chandelier trail: HH22 $360.83 - 3x ATR $8.24 = $336.11 — exit when decline exceeds ~3 average daily ranges"
target_price: 397.47
target_logic: "T1 $397.47 = entry $360.65 + 1.5x R (R=$24.54); T2 $434.29 = entry + 3x R; structure ceiling = 52w high $360.65"
holding_window_days: 21
catalyst: "2027-01-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $15859.6M; pass"
invalidation: "closes back below the breakout level $360.65 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
