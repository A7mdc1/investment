---
ticker: HST
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $26.20 (52w high) on >1.2x 20d avg volume"
entry_price: 26.20
stop_price: 24.35
stop_logic: "chandelier trail: HH22 $26.19 - 3x ATR $0.61 = $24.35 — exit when decline exceeds ~3 average daily ranges"
target_price: 28.98
target_logic: "T1 $28.98 = entry $26.20 + 1.5x R (R=$1.85); T2 $31.75 = entry + 3x R; structure ceiling = 52w high $26.20"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $234.8M; pass"
invalidation: "closes back below the breakout level $26.20 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-09 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
