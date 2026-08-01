---
ticker: AEM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $147.08 holding the uptrend (no breakdown on volume)"
entry_price: 147.08
stop_price: 143.96
stop_logic: "chandelier trail: HH22 $160.55 - 3x ATR $5.53 = $143.96 — exit when decline exceeds ~3 average daily ranges"
target_price: 151.77
target_logic: "T1 $151.77 = entry $147.08 + 1.5x R (R=$3.13); T2 $156.46 = entry + 3x R; structure ceiling = 52w high $254.41"
holding_window_days: 21
catalyst: "2026-10-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $357.5M; pass"
invalidation: "loses EMA20 $147.08 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-01 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
