---
ticker: WDC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $497.80 holding the uptrend (no breakdown on volume)"
entry_price: 497.80
stop_price: 438.48
stop_logic: "chandelier trail: HH22 $580.00 - 3x ATR $47.17 = $438.48 — exit when decline exceeds ~3 average daily ranges"
target_price: 586.77
target_logic: "T1 $586.77 = entry $497.80 + 1.5x R (R=$59.31); T2 $675.74 = entry + 3x R; structure ceiling = 52w high $800.46"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $4142.0M; pass"
invalidation: "loses EMA20 $497.80 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
