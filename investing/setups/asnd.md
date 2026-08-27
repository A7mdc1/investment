---
ticker: ASND
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $251.83 holding the uptrend (no breakdown on volume)"
entry_price: 251.83
stop_price: 239.03
stop_logic: "chandelier trail: HH22 $261.61 - 3x ATR $7.53 = $239.03 — exit when decline exceeds ~3 average daily ranges"
target_price: 271.02
target_logic: "T1 $271.02 = entry $251.83 + 1.5x R (R=$12.80); T2 $290.21 = entry + 3x R; structure ceiling = 52w high $282.04"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $124.2M; pass"
invalidation: "loses EMA20 $251.83 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
