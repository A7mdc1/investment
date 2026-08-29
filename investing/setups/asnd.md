---
ticker: ASND
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $251.86 holding the uptrend (no breakdown on volume)"
entry_price: 251.86
stop_price: 239.01
stop_logic: "chandelier trail: HH22 $261.61 - 3x ATR $7.53 = $239.01 — exit when decline exceeds ~3 average daily ranges"
target_price: 271.13
target_logic: "T1 $271.13 = entry $251.86 + 1.5x R (R=$12.85); T2 $290.40 = entry + 3x R; structure ceiling = 52w high $282.08"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $125.7M; pass"
invalidation: "loses EMA20 $251.86 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-29 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
