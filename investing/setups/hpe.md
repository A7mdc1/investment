---
ticker: HPE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $65.63 (52w high) on >1.2x 20d avg volume"
entry_price: 65.63
stop_price: 54.77
stop_logic: "chandelier trail: HH22 $65.65 - 3x ATR $3.63 = $54.77 — exit when decline exceeds ~3 average daily ranges"
target_price: 81.91
target_logic: "T1 $81.91 = entry $65.63 + 1.5x R (R=$10.86); T2 $98.20 = entry + 3x R; structure ceiling = 52w high $65.63"
holding_window_days: 21
catalyst: "2026-12-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1593.4M; pass"
invalidation: "closes back below the breakout level $65.63 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
