---
ticker: ASND
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $282.26 (52w high) on >1.2x 20d avg volume"
entry_price: 282.26
stop_price: 254.63
stop_logic: "chandelier trail: HH22 $278.56 - 3x ATR $7.98 = $254.63 — exit when decline exceeds ~3 average daily ranges"
target_price: 323.71
target_logic: "T1 $323.71 = entry $282.26 + 1.5x R (R=$27.63); T2 $365.15 = entry + 3x R; structure ceiling = 52w high $282.26"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $187.4M; pass"
invalidation: "closes back below the breakout level $282.26 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-25 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
