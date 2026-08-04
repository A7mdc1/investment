---
ticker: AEM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $147.60 holding the uptrend (no breakdown on volume)"
entry_price: 147.60
stop_price: 141.83
stop_logic: "chandelier trail: HH22 $158.07 - 3x ATR $5.41 = $141.83 — exit when decline exceeds ~3 average daily ranges"
target_price: 156.26
target_logic: "T1 $156.26 = entry $147.60 + 1.5x R (R=$5.77); T2 $164.92 = entry + 3x R; structure ceiling = 52w high $254.55"
holding_window_days: 21
catalyst: "2026-10-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $341.0M; pass"
invalidation: "loses EMA20 $147.60 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-04 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
