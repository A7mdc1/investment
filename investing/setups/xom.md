---
ticker: XOM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $153.72 holding the uptrend (no breakdown on volume)"
entry_price: 153.72
stop_price: 150.41
stop_logic: "chandelier trail: HH22 $161.67 - 3x ATR $3.75 = $150.41 — exit when decline exceeds ~3 average daily ranges"
target_price: 158.68
target_logic: "T1 $158.68 = entry $153.72 + 1.5x R (R=$3.31); T2 $163.65 = entry + 3x R; structure ceiling = 52w high $175.31"
holding_window_days: 21
catalyst: "2026-10-30 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2168.6M; pass"
invalidation: "loses EMA20 $153.72 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
