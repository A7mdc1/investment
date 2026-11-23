---
ticker: TXN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $291.97 holding the uptrend (no breakdown on volume)"
entry_price: 291.97
stop_price: 270.73
stop_logic: "chandelier trail: HH22 $317.20 - 3x ATR $15.49 = $270.73 — exit when decline exceeds ~3 average daily ranges"
target_price: 323.82
target_logic: "T1 $323.82 = entry $291.97 + 1.5x R (R=$21.23); T2 $355.67 = entry + 3x R; structure ceiling = 52w high $330.63"
holding_window_days: 21
catalyst: "2027-01-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2583.7M; pass"
invalidation: "loses EMA20 $291.97 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
