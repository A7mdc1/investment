---
ticker: WDC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $501.46 holding the uptrend (no breakdown on volume)"
entry_price: 501.46
stop_price: 437.94
stop_logic: "chandelier trail: HH22 $589.65 - 3x ATR $50.57 = $437.94 — exit when decline exceeds ~3 average daily ranges"
target_price: 596.74
target_logic: "T1 $596.74 = entry $501.46 + 1.5x R (R=$63.52); T2 $692.01 = entry + 3x R; structure ceiling = 52w high $800.26"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $4124.9M; pass"
invalidation: "loses EMA20 $501.46 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
