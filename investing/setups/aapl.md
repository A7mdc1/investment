---
ticker: AAPL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $355.43 (52w high) on >1.2x 20d avg volume"
entry_price: 355.43
stop_price: 331.34
stop_logic: "chandelier trail: HH22 $355.38 - 3x ATR $8.01 = $331.34 — exit when decline exceeds ~3 average daily ranges"
target_price: 391.55
target_logic: "T1 $391.55 = entry $355.43 + 1.5x R (R=$24.08); T2 $427.68 = entry + 3x R; structure ceiling = 52w high $355.43"
holding_window_days: 21
catalyst: "2027-01-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $15862.1M; pass"
invalidation: "closes back below the breakout level $355.43 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-05 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
