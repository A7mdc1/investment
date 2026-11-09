---
ticker: PNFP
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $109.22 (52w high) on >1.2x 20d avg volume"
entry_price: 109.22
stop_price: 98.94
stop_logic: "chandelier trail: HH22 $106.57 - 3x ATR $2.55 = $98.94 — exit when decline exceeds ~3 average daily ranges"
target_price: 124.65
target_logic: "T1 $124.65 = entry $109.22 + 1.5x R (R=$10.29); T2 $140.08 = entry + 3x R; structure ceiling = 52w high $109.22"
holding_window_days: 21
catalyst: "2027-01-27 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $113.8M; pass"
invalidation: "closes back below the breakout level $109.22 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-09 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
