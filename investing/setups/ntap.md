---
ticker: NTAP
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $209.01 (52w high) on >1.2x 20d avg volume"
entry_price: 209.01
stop_price: 179.76
stop_logic: "chandelier trail: HH22 $204.42 - 3x ATR $8.22 = $179.76 — exit when decline exceeds ~3 average daily ranges"
target_price: 252.89
target_logic: "T1 $252.89 = entry $209.01 + 1.5x R (R=$29.25); T2 $296.77 = entry + 3x R; structure ceiling = 52w high $209.01"
holding_window_days: 21
catalyst: "2026-12-01 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $481.9M; pass"
invalidation: "closes back below the breakout level $209.01 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-28 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
