---
ticker: NTAP
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $187.53 holding the uptrend (no breakdown on volume)"
entry_price: 187.53
stop_price: 185.13
stop_logic: "chandelier trail: HH22 $209.06 - 3x ATR $7.98 = $185.13 — exit when decline exceeds ~3 average daily ranges"
target_price: 191.13
target_logic: "T1 $191.13 = entry $187.53 + 1.5x R (R=$2.40); T2 $194.73 = entry + 3x R; structure ceiling = 52w high $209.17"
holding_window_days: 21
catalyst: "2026-12-01 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $465.5M; pass"
invalidation: "loses EMA20 $187.53 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-08 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
