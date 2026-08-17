---
ticker: DDOG
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $254.16 holding the uptrend (no breakdown on volume)"
entry_price: 254.16
stop_price: 244.69
stop_logic: "chandelier trail: HH22 $292.72 - 3x ATR $16.01 = $244.69 — exit when decline exceeds ~3 average daily ranges"
target_price: 268.36
target_logic: "T1 $268.36 = entry $254.16 + 1.5x R (R=$9.47); T2 $282.56 = entry + 3x R; structure ceiling = 52w high $292.89"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1330.0M; pass"
invalidation: "loses EMA20 $254.16 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
