---
ticker: PR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $24.08 (52w high) on >1.2x 20d avg volume"
entry_price: 24.08
stop_price: 22.10
stop_logic: "chandelier trail: HH22 $24.09 - 3x ATR $0.66 = $22.10 — exit when decline exceeds ~3 average daily ranges"
target_price: 27.05
target_logic: "T1 $27.05 = entry $24.08 + 1.5x R (R=$1.98); T2 $30.02 = entry + 3x R; structure ceiling = 52w high $24.08"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $207.0M; pass"
invalidation: "closes back below the breakout level $24.08 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-04 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
