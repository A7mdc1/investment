---
ticker: EXPE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $335.17 (52w high) on >1.2x 20d avg volume"
entry_price: 335.17
stop_price: 294.86
stop_logic: "chandelier trail: HH22 $335.00 - 3x ATR $13.38 = $294.86 — exit when decline exceeds ~3 average daily ranges"
target_price: 395.62
target_logic: "T1 $395.62 = entry $335.17 + 1.5x R (R=$40.30); T2 $456.08 = entry + 3x R; structure ceiling = 52w high $335.17"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $494.3M; pass"
invalidation: "closes back below the breakout level $335.17 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-21 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
