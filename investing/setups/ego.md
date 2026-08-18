---
ticker: EGO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $36.01 holding the uptrend (no breakdown on volume)"
entry_price: 36.01
stop_price: 35.89
stop_logic: "chandelier trail: HH22 $41.68 - 3x ATR $1.93 = $35.89 — exit when decline exceeds ~3 average daily ranges"
target_price: 36.21
target_logic: "T1 $36.21 = entry $36.01 + 1.5x R (R=$0.13); T2 $36.40 = entry + 3x R; structure ceiling = 52w high $50.98"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $86.9M; pass"
invalidation: "loses EMA20 $36.01 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-18 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
