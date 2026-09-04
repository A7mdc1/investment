---
ticker: APA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $45.14 (52w high) on >1.2x 20d avg volume"
entry_price: 45.14
stop_price: 40.53
stop_logic: "chandelier trail: HH22 $45.13 - 3x ATR $1.53 = $40.53 — exit when decline exceeds ~3 average daily ranges"
target_price: 52.05
target_logic: "T1 $52.05 = entry $45.14 + 1.5x R (R=$4.61); T2 $58.96 = entry + 3x R; structure ceiling = 52w high $45.14"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $216.1M; pass"
invalidation: "closes back below the breakout level $45.14 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-04 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
