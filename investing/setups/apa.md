---
ticker: APA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $45.11 (52w high) on >1.2x 20d avg volume"
entry_price: 45.11
stop_price: 40.44
stop_logic: "chandelier trail: HH22 $45.13 - 3x ATR $1.56 = $40.44 — exit when decline exceeds ~3 average daily ranges"
target_price: 52.12
target_logic: "T1 $52.12 = entry $45.11 + 1.5x R (R=$4.67); T2 $59.14 = entry + 3x R; structure ceiling = 52w high $45.11"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $227.5M; pass"
invalidation: "closes back below the breakout level $45.11 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-03 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
