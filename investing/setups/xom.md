---
ticker: XOM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $177.34 holding the uptrend (no breakdown on volume)"
entry_price: 177.34
stop_price: 176.30
stop_logic: "chandelier trail: HH22 $188.50 - 3x ATR $4.07 = $176.30 — exit when decline exceeds ~3 average daily ranges"
target_price: 178.92
target_logic: "T1 $178.92 = entry $177.34 + 1.5x R (R=$1.05); T2 $180.49 = entry + 3x R; structure ceiling = 52w high $188.52"
holding_window_days: 21
catalyst: "2027-01-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2134.0M; pass"
invalidation: "loses EMA20 $177.34 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-03 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
