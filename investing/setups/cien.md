---
ticker: CIEN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $463.43 holding the uptrend (no breakdown on volume)"
entry_price: 463.43
stop_price: 426.06
stop_logic: "chandelier trail: HH22 $525.15 - 3x ATR $33.03 = $426.06 — exit when decline exceeds ~3 average daily ranges"
target_price: 519.49
target_logic: "T1 $519.49 = entry $463.43 + 1.5x R (R=$37.37); T2 $575.55 = entry + 3x R; structure ceiling = 52w high $637.79"
holding_window_days: 21
catalyst: "2026-09-09 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1595.1M; pass"
invalidation: "loses EMA20 $463.43 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-08 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
