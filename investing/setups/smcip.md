---
ticker: SMCIP
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $70.22 (52w high) on >1.2x 20d avg volume"
entry_price: 70.22
stop_price: 59.93
stop_logic: "chandelier trail: HH22 $70.21 - 3x ATR $3.43 = $59.93 — exit when decline exceeds ~3 average daily ranges"
target_price: 85.66
target_logic: "T1 $85.66 = entry $70.22 + 1.5x R (R=$10.29); T2 $101.10 = entry + 3x R; structure ceiling = 52w high $70.22"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $35.4M; pass"
invalidation: "closes back below the breakout level $70.22 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check inconclusive (no market cap) — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
