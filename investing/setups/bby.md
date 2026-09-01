---
ticker: BBY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $84.51 holding the uptrend (no breakdown on volume)"
entry_price: 84.51
stop_price: 80.27
stop_logic: "chandelier trail: HH22 $90.26 - 3x ATR $3.33 = $80.27 — exit when decline exceeds ~3 average daily ranges"
target_price: 90.87
target_logic: "T1 $90.87 = entry $84.51 + 1.5x R (R=$4.24); T2 $97.24 = entry + 3x R; structure ceiling = 52w high $91.30"
holding_window_days: 21
catalyst: "2026-11-24 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $314.7M; pass"
invalidation: "loses EMA20 $84.51 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-01 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
