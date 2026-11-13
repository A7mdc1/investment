---
ticker: AEM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $183.27 holding the uptrend (no breakdown on volume)"
entry_price: 183.27
stop_price: 177.96
stop_logic: "chandelier trail: HH22 $202.24 - 3x ATR $8.09 = $177.96 — exit when decline exceeds ~3 average daily ranges"
target_price: 191.23
target_logic: "T1 $191.23 = entry $183.27 + 1.5x R (R=$5.31); T2 $199.19 = entry + 3x R; structure ceiling = 52w high $254.04"
holding_window_days: 21
catalyst: "2027-02-11 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $349.9M; pass"
invalidation: "loses EMA20 $183.27 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
