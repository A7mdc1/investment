---
ticker: FRO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $47.06 (52w high) on >1.2x 20d avg volume"
entry_price: 47.06
stop_price: 42.31
stop_logic: "chandelier trail: HH22 $47.04 - 3x ATR $1.58 = $42.31 — exit when decline exceeds ~3 average daily ranges"
target_price: 54.19
target_logic: "T1 $54.19 = entry $47.06 + 1.5x R (R=$4.75); T2 $61.32 = entry + 3x R; structure ceiling = 52w high $47.06"
holding_window_days: 21
catalyst: "2026-11-30 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $100.2M; pass"
invalidation: "closes back below the breakout level $47.06 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
