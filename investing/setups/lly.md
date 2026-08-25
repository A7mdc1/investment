---
ticker: LLY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $1292.82 (52w high) on >1.2x 20d avg volume"
entry_price: 1292.82
stop_price: 1168.26
stop_logic: "chandelier trail: HH22 $1292.65 - 3x ATR $41.46 = $1168.26 — exit when decline exceeds ~3 average daily ranges"
target_price: 1479.67
target_logic: "T1 $1479.67 = entry $1292.82 + 1.5x R (R=$124.56); T2 $1666.51 = entry + 3x R; structure ceiling = 52w high $1292.82"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $3316.7M; pass"
invalidation: "closes back below the breakout level $1292.82 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-25 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
