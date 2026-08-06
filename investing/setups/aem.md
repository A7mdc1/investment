---
ticker: AEM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $150.90 holding the uptrend (no breakdown on volume)"
entry_price: 150.90
stop_price: 150.85
stop_logic: "chandelier trail: HH22 $168.18 - 3x ATR $5.78 = $150.85 — exit when decline exceeds ~3 average daily ranges"
target_price: 150.97
target_logic: "T1 $150.97 = entry $150.90 + 1.5x R (R=$0.05); T2 $151.04 = entry + 3x R; structure ceiling = 52w high $254.75"
holding_window_days: 21
catalyst: "2026-10-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $375.1M; pass"
invalidation: "loses EMA20 $150.90 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
