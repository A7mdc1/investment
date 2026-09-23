---
ticker: HPE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $63.89 (52w high) on >1.2x 20d avg volume"
entry_price: 63.89
stop_price: 53.48
stop_logic: "chandelier trail: HH22 $63.86 - 3x ATR $3.46 = $53.48 — exit when decline exceeds ~3 average daily ranges"
target_price: 79.51
target_logic: "T1 $79.51 = entry $63.89 + 1.5x R (R=$10.41); T2 $95.12 = entry + 3x R; structure ceiling = 52w high $63.89"
holding_window_days: 21
catalyst: "2026-12-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1503.1M; pass"
invalidation: "closes back below the breakout level $63.89 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
