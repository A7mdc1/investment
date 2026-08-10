---
ticker: NET
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $279.17 holding the uptrend (no breakdown on volume)"
entry_price: 279.17
stop_price: 276.78
stop_logic: "chandelier trail: HH22 $324.73 - 3x ATR $15.98 = $276.78 — exit when decline exceeds ~3 average daily ranges"
target_price: 282.75
target_logic: "T1 $282.75 = entry $279.17 + 1.5x R (R=$2.39); T2 $286.34 = entry + 3x R; structure ceiling = 52w high $324.65"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1022.4M; pass"
invalidation: "loses EMA20 $279.17 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
