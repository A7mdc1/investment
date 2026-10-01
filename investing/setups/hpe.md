---
ticker: HPE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $67.13 (52w high) on >1.2x 20d avg volume"
entry_price: 67.13
stop_price: 55.18
stop_logic: "chandelier trail: HH22 $67.10 - 3x ATR $3.97 = $55.18 — exit when decline exceeds ~3 average daily ranges"
target_price: 85.04
target_logic: "T1 $85.04 = entry $67.13 + 1.5x R (R=$11.94); T2 $102.96 = entry + 3x R; structure ceiling = 52w high $67.13"
holding_window_days: 21
catalyst: "2026-12-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1489.9M; pass"
invalidation: "closes back below the breakout level $67.13 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-01 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
