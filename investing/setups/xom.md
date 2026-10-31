---
ticker: XOM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $188.57 (52w high) on >1.2x 20d avg volume"
entry_price: 188.57
stop_price: 176.88
stop_logic: "chandelier trail: HH22 $188.50 - 3x ATR $3.87 = $176.88 — exit when decline exceeds ~3 average daily ranges"
target_price: 206.11
target_logic: "T1 $206.11 = entry $188.57 + 1.5x R (R=$11.69); T2 $223.64 = entry + 3x R; structure ceiling = 52w high $188.57"
holding_window_days: 21
catalyst: "2027-01-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2125.6M; pass"
invalidation: "closes back below the breakout level $188.57 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-31 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
