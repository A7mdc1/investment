---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $356.30 holding the uptrend (no breakdown on volume)"
entry_price: 356.30
stop_price: 333.44
stop_logic: "chandelier trail: HH22 $424.99 - 3x ATR $30.52 = $333.44 — exit when decline exceeds ~3 average daily ranges"
target_price: 390.58
target_logic: "T1 $390.58 = entry $356.30 + 1.5x R (R=$22.86); T2 $424.87 = entry + 3x R; structure ceiling = 52w high $749.33"
holding_window_days: 21
catalyst: "2027-02-01 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $404.8M; pass"
invalidation: "loses EMA20 $356.30 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
