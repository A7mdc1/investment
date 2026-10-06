---
ticker: JBL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $306.51 holding the uptrend (no breakdown on volume)"
entry_price: 306.51
stop_price: 294.02
stop_logic: "chandelier trail: HH22 $331.58 - 3x ATR $12.52 = $294.02 — exit when decline exceeds ~3 average daily ranges"
target_price: 325.25
target_logic: "T1 $325.25 = entry $306.51 + 1.5x R (R=$12.49); T2 $343.99 = entry + 3x R; structure ceiling = 52w high $428.72"
holding_window_days: 21
catalyst: "2026-12-16 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $445.7M; pass"
invalidation: "loses EMA20 $306.51 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
