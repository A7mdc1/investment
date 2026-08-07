---
ticker: VICR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $229.00 holding the uptrend (no breakdown on volume)"
entry_price: 229.00
stop_price: 221.81
stop_logic: "chandelier trail: HH22 $289.80 - 3x ATR $22.66 = $221.81 — exit when decline exceeds ~3 average daily ranges"
target_price: 239.77
target_logic: "T1 $239.77 = entry $229.00 + 1.5x R (R=$7.19); T2 $250.55 = entry + 3x R; structure ceiling = 52w high $382.46"
holding_window_days: 21
catalyst: "2026-10-20 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $189.1M; pass"
invalidation: "loses EMA20 $229.00 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
