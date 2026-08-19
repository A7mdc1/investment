---
ticker: DINO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $96.76 (52w high) on >1.2x 20d avg volume"
entry_price: 96.76
stop_price: 85.69
stop_logic: "chandelier trail: HH22 $96.76 - 3x ATR $3.69 = $85.69 — exit when decline exceeds ~3 average daily ranges"
target_price: 113.36
target_logic: "T1 $113.36 = entry $96.76 + 1.5x R (R=$11.07); T2 $129.96 = entry + 3x R; structure ceiling = 52w high $96.76"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $257.8M; pass"
invalidation: "closes back below the breakout level $96.76 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
