---
ticker: EXPE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $335.03 (52w high) on >1.2x 20d avg volume"
entry_price: 335.03
stop_price: 294.79
stop_logic: "chandelier trail: HH22 $335.00 - 3x ATR $13.40 = $294.79 — exit when decline exceeds ~3 average daily ranges"
target_price: 395.39
target_logic: "T1 $395.39 = entry $335.03 + 1.5x R (R=$40.24); T2 $455.76 = entry + 3x R; structure ceiling = 52w high $335.03"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $510.5M; pass"
invalidation: "closes back below the breakout level $335.03 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
