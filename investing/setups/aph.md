---
ticker: APH
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $163.18 holding the uptrend (no breakdown on volume)"
entry_price: 163.18
stop_price: 154.56
stop_logic: "chandelier trail: HH22 $176.33 - 3x ATR $7.26 = $154.56 — exit when decline exceeds ~3 average daily ranges"
target_price: 176.12
target_logic: "T1 $176.12 = entry $163.18 + 1.5x R (R=$8.62); T2 $189.05 = entry + 3x R; structure ceiling = 52w high $178.54"
holding_window_days: 21
catalyst: "2026-10-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1064.9M; pass"
invalidation: "loses EMA20 $163.18 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
