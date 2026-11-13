---
ticker: LLY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $1460.30 (52w high) on >1.2x 20d avg volume"
entry_price: 1460.30
stop_price: 1318.74
stop_logic: "chandelier trail: HH22 $1460.00 - 3x ATR $47.09 = $1318.74 — exit when decline exceeds ~3 average daily ranges"
target_price: 1672.65
target_logic: "T1 $1672.65 = entry $1460.30 + 1.5x R (R=$141.56); T2 $1884.99 = entry + 3x R; structure ceiling = 52w high $1460.30"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $3979.2M; pass"
invalidation: "closes back below the breakout level $1460.30 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
