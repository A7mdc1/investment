---
ticker: AVT
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $92.72 holding the uptrend (no breakdown on volume)"
entry_price: 92.72
stop_price: 87.12
stop_logic: "chandelier trail: HH22 $100.00 - 3x ATR $4.29 = $87.12 — exit when decline exceeds ~3 average daily ranges"
target_price: 101.11
target_logic: "T1 $101.11 = entry $92.72 + 1.5x R (R=$5.60); T2 $109.51 = entry + 3x R; structure ceiling = 52w high $99.96"
holding_window_days: 21
catalyst: "2026-10-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $113.1M; pass"
invalidation: "loses EMA20 $92.72 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check inconclusive (no debt/cash rows in balance sheet — ratios unknow) — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
