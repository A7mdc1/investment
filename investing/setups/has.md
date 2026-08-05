---
ticker: HAS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $88.72 holding the uptrend (no breakdown on volume)"
entry_price: 88.72
stop_price: 88.70
stop_logic: "chandelier trail: HH22 $97.00 - 3x ATR $2.77 = $88.70 — exit when decline exceeds ~3 average daily ranges"
target_price: 88.76
target_logic: "T1 $88.76 = entry $88.72 + 1.5x R (R=$0.03); T2 $88.80 = entry + 3x R; structure ceiling = 52w high $105.36"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $212.2M; pass"
invalidation: "loses EMA20 $88.72 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-05 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
