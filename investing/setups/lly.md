---
ticker: LLY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $1449.43 (52w high) on >1.2x 20d avg volume"
entry_price: 1449.43
stop_price: 1321.97
stop_logic: "chandelier trail: HH22 $1449.68 - 3x ATR $42.57 = $1321.97 — exit when decline exceeds ~3 average daily ranges"
target_price: 1640.61
target_logic: "T1 $1640.61 = entry $1449.43 + 1.5x R (R=$127.45); T2 $1831.79 = entry + 3x R; structure ceiling = 52w high $1449.43"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $3202.3M; pass"
invalidation: "closes back below the breakout level $1449.43 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-01 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
