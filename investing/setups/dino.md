---
ticker: DINO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $95.32 (52w high) on >1.2x 20d avg volume"
entry_price: 95.32
stop_price: 84.14
stop_logic: "chandelier trail: HH22 $95.36 - 3x ATR $3.74 = $84.14 — exit when decline exceeds ~3 average daily ranges"
target_price: 112.09
target_logic: "T1 $112.09 = entry $95.32 + 1.5x R (R=$11.18); T2 $128.86 = entry + 3x R; structure ceiling = 52w high $95.32"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $257.4M; pass"
invalidation: "closes back below the breakout level $95.32 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
