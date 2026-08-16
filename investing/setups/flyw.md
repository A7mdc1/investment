---
ticker: FLYW
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $18.98 (52w high) on >1.2x 20d avg volume"
entry_price: 18.98
stop_price: 16.80
stop_logic: "chandelier trail: HH22 $18.98 - 3x ATR $0.73 = $16.80 — exit when decline exceeds ~3 average daily ranges"
target_price: 22.26
target_logic: "T1 $22.26 = entry $18.98 + 1.5x R (R=$2.18); T2 $25.54 = entry + 3x R; structure ceiling = 52w high $18.98"
holding_window_days: 21
catalyst: "2026-11-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $38.7M; pass"
invalidation: "closes back below the breakout level $18.98 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
