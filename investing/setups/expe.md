---
ticker: EXPE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $338.07 (52w high) on >1.2x 20d avg volume"
entry_price: 338.07
stop_price: 297.01
stop_logic: "chandelier trail: HH22 $338.11 - 3x ATR $13.70 = $297.01 — exit when decline exceeds ~3 average daily ranges"
target_price: 399.67
target_logic: "T1 $399.67 = entry $338.07 + 1.5x R (R=$41.06); T2 $461.27 = entry + 3x R; structure ceiling = 52w high $338.07"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $500.8M; pass"
invalidation: "closes back below the breakout level $338.07 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-24 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
