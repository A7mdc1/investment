---
ticker: CLS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $338.23 holding the uptrend (no breakdown on volume)"
entry_price: 338.23
stop_price: 296.90
stop_logic: "chandelier trail: HH22 $378.99 - 3x ATR $27.36 = $296.90 — exit when decline exceeds ~3 average daily ranges"
target_price: 400.21
target_logic: "T1 $400.21 = entry $338.23 + 1.5x R (R=$41.32); T2 $462.19 = entry + 3x R; structure ceiling = 52w high $474.37"
holding_window_days: 21
catalyst: "2026-10-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1056.1M; pass"
invalidation: "loses EMA20 $338.23 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-09 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
