---
ticker: ACGL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $113.66 (52w high) on >1.2x 20d avg volume"
entry_price: 113.66
stop_price: 105.98
stop_logic: "chandelier trail: HH22 $113.63 - 3x ATR $2.55 = $105.98 — exit when decline exceeds ~3 average daily ranges"
target_price: 125.19
target_logic: "T1 $125.19 = entry $113.66 + 1.5x R (R=$7.69); T2 $136.72 = entry + 3x R; structure ceiling = 52w high $113.66"
holding_window_days: 21
catalyst: "2027-02-08 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $227.7M; pass"
invalidation: "closes back below the breakout level $113.66 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check FLAGGED: industry 'Insurance - Diversified' matches 'insurance' — core business fails screen
---

## Notes
Scaffolded 2026-11-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
