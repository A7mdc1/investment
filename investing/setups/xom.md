---
ticker: XOM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $174.16 (52w high) on >1.2x 20d avg volume"
entry_price: 174.16
stop_price: 157.13
stop_logic: "chandelier trail: HH22 $168.64 - 3x ATR $3.84 = $157.13 — exit when decline exceeds ~3 average daily ranges"
target_price: 199.70
target_logic: "T1 $199.70 = entry $174.16 + 1.5x R (R=$17.03); T2 $225.24 = entry + 3x R; structure ceiling = 52w high $174.16"
holding_window_days: 21
catalyst: "2026-10-30 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2178.0M; pass"
invalidation: "closes back below the breakout level $174.16 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-21 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
