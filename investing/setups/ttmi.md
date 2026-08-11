---
ticker: TTMI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $133.67 holding the uptrend (no breakdown on volume)"
entry_price: 133.67
stop_price: 112.59
stop_logic: "chandelier trail: HH22 $150.20 - 3x ATR $12.54 = $112.59 — exit when decline exceeds ~3 average daily ranges"
target_price: 165.28
target_logic: "T1 $165.28 = entry $133.67 + 1.5x R (R=$21.08); T2 $196.89 = entry + 3x R; structure ceiling = 52w high $223.67"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $382.3M; pass"
invalidation: "loses EMA20 $133.67 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
