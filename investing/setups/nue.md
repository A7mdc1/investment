---
ticker: NUE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $287.62 (52w high) on >1.2x 20d avg volume"
entry_price: 287.62
stop_price: 262.64
stop_logic: "chandelier trail: HH22 $287.70 - 3x ATR $8.35 = $262.64 — exit when decline exceeds ~3 average daily ranges"
target_price: 325.08
target_logic: "T1 $325.08 = entry $287.62 + 1.5x R (R=$24.98); T2 $362.54 = entry + 3x R; structure ceiling = 52w high $287.62"
holding_window_days: 21
catalyst: "2027-01-25 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $337.1M; pass"
invalidation: "closes back below the breakout level $287.62 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-03 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
