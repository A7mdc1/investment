---
ticker: LLY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $1184.01 holding the uptrend (no breakdown on volume)"
entry_price: 1184.01
stop_price: 1117.25
stop_logic: "chandelier trail: HH22 $1238.33 - 3x ATR $40.36 = $1117.25 — exit when decline exceeds ~3 average daily ranges"
target_price: 1284.14
target_logic: "T1 $1284.14 = entry $1184.01 + 1.5x R (R=$66.76); T2 $1384.28 = entry + 3x R; structure ceiling = 52w high $1247.53"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $3133.7M; pass"
invalidation: "loses EMA20 $1184.01 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
