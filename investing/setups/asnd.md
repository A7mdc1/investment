---
ticker: ASND
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $252.24 holding the uptrend (no breakdown on volume)"
entry_price: 252.24
stop_price: 237.64
stop_logic: "chandelier trail: HH22 $261.61 - 3x ATR $7.99 = $237.64 — exit when decline exceeds ~3 average daily ranges"
target_price: 274.13
target_logic: "T1 $274.13 = entry $252.24 + 1.5x R (R=$14.60); T2 $296.03 = entry + 3x R; structure ceiling = 52w high $282.03"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $133.8M; pass"
invalidation: "loses EMA20 $252.24 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-24 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
