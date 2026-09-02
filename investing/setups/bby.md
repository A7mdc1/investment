---
ticker: BBY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $91.24 (52w high) on >1.2x 20d avg volume"
entry_price: 91.24
stop_price: 79.70
stop_logic: "chandelier trail: HH22 $90.26 - 3x ATR $3.52 = $79.70 — exit when decline exceeds ~3 average daily ranges"
target_price: 108.55
target_logic: "T1 $108.55 = entry $91.24 + 1.5x R (R=$11.54); T2 $125.86 = entry + 3x R; structure ceiling = 52w high $91.24"
holding_window_days: 21
catalyst: "2026-11-24 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $328.1M; pass"
invalidation: "closes back below the breakout level $91.24 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-02 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
