---
ticker: UTHR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $520.83 holding the uptrend (no breakdown on volume)"
entry_price: 520.83
stop_price: 502.19
stop_logic: "chandelier trail: HH22 $543.56 - 3x ATR $13.79 = $502.19 — exit when decline exceeds ~3 average daily ranges"
target_price: 548.80
target_logic: "T1 $548.80 = entry $520.83 + 1.5x R (R=$18.64); T2 $576.76 = entry + 3x R; structure ceiling = 52w high $609.20"
holding_window_days: 21
catalyst: "2026-10-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $268.3M; pass"
invalidation: "loses EMA20 $520.83 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
