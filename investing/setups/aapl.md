---
ticker: AAPL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $360.81 (52w high) on >1.2x 20d avg volume"
entry_price: 360.81
stop_price: 336.47
stop_logic: "chandelier trail: HH22 $360.83 - 3x ATR $8.12 = $336.47 — exit when decline exceeds ~3 average daily ranges"
target_price: 397.32
target_logic: "T1 $397.32 = entry $360.81 + 1.5x R (R=$24.34); T2 $433.84 = entry + 3x R; structure ceiling = 52w high $360.81"
holding_window_days: 21
catalyst: "2027-01-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $16153.0M; pass"
invalidation: "closes back below the breakout level $360.81 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
