---
ticker: DDOG
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $254.38 holding the uptrend (no breakdown on volume)"
entry_price: 254.38
stop_price: 244.07
stop_logic: "chandelier trail: HH22 $292.72 - 3x ATR $16.22 = $244.07 — exit when decline exceeds ~3 average daily ranges"
target_price: 269.84
target_logic: "T1 $269.84 = entry $254.38 + 1.5x R (R=$10.31); T2 $285.31 = entry + 3x R; structure ceiling = 52w high $292.85"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1316.5M; pass"
invalidation: "loses EMA20 $254.38 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
