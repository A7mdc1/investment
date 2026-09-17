---
ticker: HPE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $64.06 (52w high) on >1.2x 20d avg volume"
entry_price: 64.06
stop_price: 51.57
stop_logic: "chandelier trail: HH22 $62.15 - 3x ATR $3.53 = $51.57 — exit when decline exceeds ~3 average daily ranges"
target_price: 82.80
target_logic: "T1 $82.80 = entry $64.06 + 1.5x R (R=$12.49); T2 $101.54 = entry + 3x R; structure ceiling = 52w high $64.06"
holding_window_days: 21
catalyst: "2026-12-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1370.7M; pass"
invalidation: "closes back below the breakout level $64.06 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
