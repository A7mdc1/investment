---
ticker: WDC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $500.77 holding the uptrend (no breakdown on volume)"
entry_price: 500.77
stop_price: 439.67
stop_logic: "chandelier trail: HH22 $580.00 - 3x ATR $46.78 = $439.67 — exit when decline exceeds ~3 average daily ranges"
target_price: 592.42
target_logic: "T1 $592.42 = entry $500.77 + 1.5x R (R=$61.10); T2 $684.07 = entry + 3x R; structure ceiling = 52w high $800.12"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $4083.0M; pass"
invalidation: "loses EMA20 $500.77 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-18 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
