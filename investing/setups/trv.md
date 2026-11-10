---
ticker: TRV
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $418.08 (52w high) on >1.2x 20d avg volume"
entry_price: 418.08
stop_price: 390.52
stop_logic: "chandelier trail: HH22 $418.00 - 3x ATR $9.16 = $390.52 — exit when decline exceeds ~3 average daily ranges"
target_price: 459.41
target_logic: "T1 $459.41 = entry $418.08 + 1.5x R (R=$27.56); T2 $500.75 = entry + 3x R; structure ceiling = 52w high $418.08"
holding_window_days: 21
catalyst: "2027-01-20 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $643.0M; pass"
invalidation: "closes back below the breakout level $418.08 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check FLAGGED: industry 'Insurance - Property & Casualty' matches 'insurance' — core business fails screen
---

## Notes
Scaffolded 2026-11-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
