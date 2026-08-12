---
ticker: MKSI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $314.07 holding the uptrend (no breakdown on volume)"
entry_price: 314.07
stop_price: 301.88
stop_logic: "chandelier trail: HH22 $374.12 - 3x ATR $24.08 = $301.88 — exit when decline exceeds ~3 average daily ranges"
target_price: 332.35
target_logic: "T1 $332.35 = entry $314.07 + 1.5x R (R=$12.19); T2 $350.63 = entry + 3x R; structure ceiling = 52w high $447.45"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $466.1M; pass"
invalidation: "loses EMA20 $314.07 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
