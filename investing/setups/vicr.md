---
ticker: VICR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $231.37 holding the uptrend (no breakdown on volume)"
entry_price: 231.37
stop_price: 218.99
stop_logic: "chandelier trail: HH22 $289.80 - 3x ATR $23.60 = $218.99 — exit when decline exceeds ~3 average daily ranges"
target_price: 249.93
target_logic: "T1 $249.93 = entry $231.37 + 1.5x R (R=$12.37); T2 $268.49 = entry + 3x R; structure ceiling = 52w high $382.90"
holding_window_days: 21
catalyst: "2026-10-20 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $191.8M; pass"
invalidation: "loses EMA20 $231.37 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-05 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
