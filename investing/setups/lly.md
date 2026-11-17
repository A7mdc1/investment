---
ticker: LLY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $1475.50 (52w high) on >1.2x 20d avg volume"
entry_price: 1475.50
stop_price: 1335.65
stop_logic: "chandelier trail: HH22 $1475.25 - 3x ATR $46.53 = $1335.65 — exit when decline exceeds ~3 average daily ranges"
target_price: 1685.27
target_logic: "T1 $1685.27 = entry $1475.50 + 1.5x R (R=$139.85); T2 $1895.04 = entry + 3x R; structure ceiling = 52w high $1475.50"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $4065.0M; pass"
invalidation: "closes back below the breakout level $1475.50 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
