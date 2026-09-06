---
ticker: NTAP
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $187.70 holding the uptrend (no breakdown on volume)"
entry_price: 187.70
stop_price: 184.30
stop_logic: "chandelier trail: HH22 $209.06 - 3x ATR $8.25 = $184.30 — exit when decline exceeds ~3 average daily ranges"
target_price: 192.79
target_logic: "T1 $192.79 = entry $187.70 + 1.5x R (R=$3.40); T2 $197.89 = entry + 3x R; structure ceiling = 52w high $209.00"
holding_window_days: 21
catalyst: "2026-12-01 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $498.7M; pass"
invalidation: "loses EMA20 $187.70 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
