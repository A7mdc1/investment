---
ticker: FRO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $54.39 (52w high) on >1.2x 20d avg volume"
entry_price: 54.39
stop_price: 49.38
stop_logic: "chandelier trail: HH22 $54.39 - 3x ATR $1.67 = $49.38 — exit when decline exceeds ~3 average daily ranges"
target_price: 61.92
target_logic: "T1 $61.92 = entry $54.39 + 1.5x R (R=$5.02); T2 $69.44 = entry + 3x R; structure ceiling = 52w high $54.39"
holding_window_days: 21
catalyst: "2026-11-30 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $135.1M; pass"
invalidation: "closes back below the breakout level $54.39 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
