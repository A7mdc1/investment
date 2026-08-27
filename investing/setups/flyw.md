---
ticker: FLYW
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $19.73 (52w high) on >1.2x 20d avg volume"
entry_price: 19.73
stop_price: 17.65
stop_logic: "chandelier trail: HH22 $19.73 - 3x ATR $0.69 = $17.65 — exit when decline exceeds ~3 average daily ranges"
target_price: 22.84
target_logic: "T1 $22.84 = entry $19.73 + 1.5x R (R=$2.07); T2 $25.95 = entry + 3x R; structure ceiling = 52w high $19.73"
holding_window_days: 21
catalyst: "2026-11-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $36.2M; pass"
invalidation: "closes back below the breakout level $19.73 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
