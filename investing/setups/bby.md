---
ticker: BBY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $95.77 (52w high) on >1.2x 20d avg volume"
entry_price: 95.77
stop_price: 85.40
stop_logic: "chandelier trail: HH22 $95.81 - 3x ATR $3.47 = $85.40 — exit when decline exceeds ~3 average daily ranges"
target_price: 111.34
target_logic: "T1 $111.34 = entry $95.77 + 1.5x R (R=$10.37); T2 $126.90 = entry + 3x R; structure ceiling = 52w high $95.77"
holding_window_days: 21
catalyst: "2026-11-24 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $363.0M; pass"
invalidation: "closes back below the breakout level $95.77 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
