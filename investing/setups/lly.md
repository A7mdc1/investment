---
ticker: LLY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $1373.23 holding the uptrend (no breakdown on volume)"
entry_price: 1373.23
stop_price: 1333.87
stop_logic: "chandelier trail: HH22 $1475.25 - 3x ATR $47.13 = $1333.87 — exit when decline exceeds ~3 average daily ranges"
target_price: 1432.27
target_logic: "T1 $1432.27 = entry $1373.23 + 1.5x R (R=$39.36); T2 $1491.31 = entry + 3x R; structure ceiling = 52w high $1474.81"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $4628.6M; pass"
invalidation: "loses EMA20 $1373.23 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-26 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
