---
ticker: TTMI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $134.99 holding the uptrend (no breakdown on volume)"
entry_price: 134.99
stop_price: 117.83
stop_logic: "chandelier trail: HH22 $154.81 - 3x ATR $12.33 = $117.83 — exit when decline exceeds ~3 average daily ranges"
target_price: 160.74
target_logic: "T1 $160.74 = entry $134.99 + 1.5x R (R=$17.16); T2 $186.48 = entry + 3x R; structure ceiling = 52w high $223.91"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $354.4M; pass"
invalidation: "loses EMA20 $134.99 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
