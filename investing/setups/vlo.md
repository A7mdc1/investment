---
ticker: VLO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $318.96 (52w high) on >1.2x 20d avg volume"
entry_price: 318.96
stop_price: 286.02
stop_logic: "chandelier trail: HH22 $319.01 - 3x ATR $10.99 = $286.02 — exit when decline exceeds ~3 average daily ranges"
target_price: 368.37
target_logic: "T1 $368.37 = entry $318.96 + 1.5x R (R=$32.94); T2 $417.77 = entry + 3x R; structure ceiling = 52w high $318.96"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $801.8M; pass"
invalidation: "closes back below the breakout level $318.96 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-01 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
