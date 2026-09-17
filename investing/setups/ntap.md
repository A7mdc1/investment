---
ticker: NTAP
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $208.98 (52w high) on >1.2x 20d avg volume"
entry_price: 208.98
stop_price: 182.51
stop_logic: "chandelier trail: HH22 $207.96 - 3x ATR $8.48 = $182.51 — exit when decline exceeds ~3 average daily ranges"
target_price: 248.68
target_logic: "T1 $248.68 = entry $208.98 + 1.5x R (R=$26.46); T2 $288.37 = entry + 3x R; structure ceiling = 52w high $208.98"
holding_window_days: 21
catalyst: "2026-12-01 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $441.1M; pass"
invalidation: "closes back below the breakout level $208.98 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
