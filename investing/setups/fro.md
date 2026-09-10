---
ticker: FRO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $48.73 (52w high) on >1.2x 20d avg volume"
entry_price: 48.73
stop_price: 44.10
stop_logic: "chandelier trail: HH22 $48.71 - 3x ATR $1.53 = $44.10 — exit when decline exceeds ~3 average daily ranges"
target_price: 55.67
target_logic: "T1 $55.67 = entry $48.73 + 1.5x R (R=$4.63); T2 $62.61 = entry + 3x R; structure ceiling = 52w high $48.73"
holding_window_days: 21
catalyst: "2026-11-30 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $106.4M; pass"
invalidation: "closes back below the breakout level $48.73 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
