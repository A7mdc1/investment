---
ticker: UTHR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $525.01 holding the uptrend (no breakdown on volume)"
entry_price: 525.01
stop_price: 502.11
stop_logic: "chandelier trail: HH22 $543.56 - 3x ATR $13.82 = $502.11 — exit when decline exceeds ~3 average daily ranges"
target_price: 559.35
target_logic: "T1 $559.35 = entry $525.01 + 1.5x R (R=$22.90); T2 $593.70 = entry + 3x R; structure ceiling = 52w high $609.61"
holding_window_days: 21
catalyst: "2026-10-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $262.6M; pass"
invalidation: "loses EMA20 $525.01 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
