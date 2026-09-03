---
ticker: ASND
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $282.23 (52w high) on >1.2x 20d avg volume"
entry_price: 282.23
stop_price: 244.70
stop_logic: "chandelier trail: HH22 $269.45 - 3x ATR $8.25 = $244.70 — exit when decline exceeds ~3 average daily ranges"
target_price: 338.52
target_logic: "T1 $338.52 = entry $282.23 + 1.5x R (R=$37.53); T2 $394.82 = entry + 3x R; structure ceiling = 52w high $282.23"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $127.4M; pass"
invalidation: "closes back below the breakout level $282.23 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-03 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
