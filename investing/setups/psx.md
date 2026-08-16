---
ticker: PSX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $236.21 (52w high) on >1.2x 20d avg volume"
entry_price: 236.21
stop_price: 214.88
stop_logic: "chandelier trail: HH22 $236.14 - 3x ATR $7.09 = $214.88 — exit when decline exceeds ~3 average daily ranges"
target_price: 268.20
target_logic: "T1 $268.20 = entry $236.21 + 1.5x R (R=$21.33); T2 $300.19 = entry + 3x R; structure ceiling = 52w high $236.21"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $551.6M; pass"
invalidation: "closes back below the breakout level $236.21 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
