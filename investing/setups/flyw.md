---
ticker: FLYW
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $21.62 (52w high) on >1.2x 20d avg volume"
entry_price: 21.62
stop_price: 19.47
stop_logic: "chandelier trail: HH22 $21.62 - 3x ATR $0.72 = $19.47 — exit when decline exceeds ~3 average daily ranges"
target_price: 24.84
target_logic: "T1 $24.84 = entry $21.62 + 1.5x R (R=$2.15); T2 $28.06 = entry + 3x R; structure ceiling = 52w high $21.62"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $27.0M; pass"
invalidation: "closes back below the breakout level $21.62 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-04 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
