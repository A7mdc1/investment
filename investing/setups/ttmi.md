---
ticker: TTMI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $134.98 holding the uptrend (no breakdown on volume)"
entry_price: 134.98
stop_price: 113.34
stop_logic: "chandelier trail: HH22 $150.20 - 3x ATR $12.29 = $113.34 — exit when decline exceeds ~3 average daily ranges"
target_price: 167.44
target_logic: "T1 $167.44 = entry $134.98 + 1.5x R (R=$21.64); T2 $199.90 = entry + 3x R; structure ceiling = 52w high $223.79"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $387.0M; pass"
invalidation: "loses EMA20 $134.98 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
