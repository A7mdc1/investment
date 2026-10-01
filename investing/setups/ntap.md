---
ticker: NTAP
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $216.79 (52w high) on >1.2x 20d avg volume"
entry_price: 216.79
stop_price: 191.67
stop_logic: "chandelier trail: HH22 $216.81 - 3x ATR $8.38 = $191.67 — exit when decline exceeds ~3 average daily ranges"
target_price: 254.47
target_logic: "T1 $254.47 = entry $216.79 + 1.5x R (R=$25.12); T2 $292.15 = entry + 3x R; structure ceiling = 52w high $216.79"
holding_window_days: 21
catalyst: "2026-12-01 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $487.6M; pass"
invalidation: "closes back below the breakout level $216.79 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-01 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
