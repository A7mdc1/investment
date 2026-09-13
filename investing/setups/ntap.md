---
ticker: NTAP
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $209.11 (52w high) on >1.2x 20d avg volume"
entry_price: 209.11
stop_price: 184.95
stop_logic: "chandelier trail: HH22 $209.06 - 3x ATR $8.04 = $184.95 — exit when decline exceeds ~3 average daily ranges"
target_price: 245.35
target_logic: "T1 $245.35 = entry $209.11 + 1.5x R (R=$24.16); T2 $281.59 = entry + 3x R; structure ceiling = 52w high $209.11"
holding_window_days: 21
catalyst: "2026-12-01 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $472.3M; pass"
invalidation: "closes back below the breakout level $209.11 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
