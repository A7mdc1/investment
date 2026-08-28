---
ticker: AAPL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $312.86 holding the uptrend (no breakdown on volume)"
entry_price: 312.86
stop_price: 311.22
stop_logic: "chandelier trail: HH22 $334.46 - 3x ATR $7.75 = $311.22 — exit when decline exceeds ~3 average daily ranges"
target_price: 315.33
target_logic: "T1 $315.33 = entry $312.86 + 1.5x R (R=$1.64); T2 $317.79 = entry + 3x R; structure ceiling = 52w high $344.36"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $13026.1M; pass"
invalidation: "loses EMA20 $312.86 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-28 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
