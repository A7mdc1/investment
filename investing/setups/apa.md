---
ticker: APA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: breakout
entry_trigger: "close above $45.04 (52w high) on >1.2x 20d avg volume"
entry_price: 45.04
stop_price: 40.31
stop_logic: "chandelier trail: HH22 $45.05 - 3x ATR $1.58 = $40.31 — exit when decline exceeds ~3 average daily ranges"
target_price: 52.13
target_logic: "T1 $52.13 = entry $45.04 + 1.5x R (R=$4.73); T2 $59.22 = entry + 3x R; structure ceiling = 52w high $45.04"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $227.0M; pass"
invalidation: "closes back below the breakout level $45.04 within 2 sessions, or breakout volume < 1.2x average"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-02 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
