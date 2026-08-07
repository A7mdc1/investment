---
ticker: UTHR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $529.13 holding the uptrend (no breakdown on volume)"
entry_price: 529.13
stop_price: 516.75
stop_logic: "chandelier trail: HH22 $556.26 - 3x ATR $13.17 = $516.75 — exit when decline exceeds ~3 average daily ranges"
target_price: 547.70
target_logic: "T1 $547.70 = entry $529.13 + 1.5x R (R=$12.38); T2 $566.27 = entry + 3x R; structure ceiling = 52w high $609.35"
holding_window_days: 21
catalyst: "2026-10-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $253.0M; pass"
invalidation: "loses EMA20 $529.13 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
