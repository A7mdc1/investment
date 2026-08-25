---
ticker: EXPE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $341.01 (52w high) on >1.2x 20d avg volume"
entry_price: 341.01
stop_price: 299.85
stop_logic: "chandelier trail: HH22 $341.09 - 3x ATR $13.75 = $299.85 — exit when decline exceeds ~3 average daily ranges"
target_price: 402.73
target_logic: "T1 $402.73 = entry $341.01 + 1.5x R (R=$41.15); T2 $464.46 = entry + 3x R; structure ceiling = 52w high $341.01"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $503.8M; pass"
invalidation: "closes back below the breakout level $341.01 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-25 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
