---
ticker: EXPE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $335.02 (52w high) on >1.2x 20d avg volume"
entry_price: 335.02
stop_price: 294.49
stop_logic: "chandelier trail: HH22 $335.00 - 3x ATR $13.50 = $294.49 — exit when decline exceeds ~3 average daily ranges"
target_price: 395.82
target_logic: "T1 $395.82 = entry $335.02 + 1.5x R (R=$40.53); T2 $456.62 = entry + 3x R; structure ceiling = 52w high $335.02"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $493.7M; pass"
invalidation: "closes back below the breakout level $335.02 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-20 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
