---
ticker: EXPE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $341.39 (52w high) on >1.2x 20d avg volume"
entry_price: 341.39
stop_price: 303.09
stop_logic: "chandelier trail: HH22 $341.51 - 3x ATR $12.80 = $303.09 — exit when decline exceeds ~3 average daily ranges"
target_price: 398.83
target_logic: "T1 $398.83 = entry $341.39 + 1.5x R (R=$38.30); T2 $456.28 = entry + 3x R; structure ceiling = 52w high $341.39"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $496.3M; pass"
invalidation: "closes back below the breakout level $341.39 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-30 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
