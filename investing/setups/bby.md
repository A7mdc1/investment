---
ticker: BBY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $91.27 (52w high) on >1.2x 20d avg volume"
entry_price: 91.27
stop_price: 80.56
stop_logic: "chandelier trail: HH22 $90.82 - 3x ATR $3.42 = $80.56 — exit when decline exceeds ~3 average daily ranges"
target_price: 107.34
target_logic: "T1 $107.34 = entry $91.27 + 1.5x R (R=$10.71); T2 $123.40 = entry + 3x R; structure ceiling = 52w high $91.27"
holding_window_days: 21
catalyst: "2026-11-24 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $346.1M; pass"
invalidation: "closes back below the breakout level $91.27 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
