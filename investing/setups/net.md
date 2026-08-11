---
ticker: NET
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $324.60 (52w high) on >1.2x 20d avg volume"
entry_price: 324.60
stop_price: 275.31
stop_logic: "chandelier trail: HH22 $324.73 - 3x ATR $16.47 = $275.31 — exit when decline exceeds ~3 average daily ranges"
target_price: 398.53
target_logic: "T1 $398.53 = entry $324.60 + 1.5x R (R=$49.29); T2 $472.46 = entry + 3x R; structure ceiling = 52w high $324.60"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1087.7M; pass"
invalidation: "closes back below the breakout level $324.60 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
