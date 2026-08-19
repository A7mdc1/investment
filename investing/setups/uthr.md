---
ticker: UTHR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $521.19 holding the uptrend (no breakdown on volume)"
entry_price: 521.19
stop_price: 502.93
stop_logic: "chandelier trail: HH22 $543.56 - 3x ATR $13.54 = $502.93 — exit when decline exceeds ~3 average daily ranges"
target_price: 548.58
target_logic: "T1 $548.58 = entry $521.19 + 1.5x R (R=$18.26); T2 $575.97 = entry + 3x R; structure ceiling = 52w high $609.06"
holding_window_days: 21
catalyst: "2026-10-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $264.7M; pass"
invalidation: "loses EMA20 $521.19 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
