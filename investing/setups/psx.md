---
ticker: PSX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $274.03 holding the uptrend (no breakdown on volume)"
entry_price: 274.03
stop_price: 268.28
stop_logic: "chandelier trail: HH22 $299.39 - 3x ATR $10.37 = $268.28 — exit when decline exceeds ~3 average daily ranges"
target_price: 282.64
target_logic: "T1 $282.64 = entry $274.03 + 1.5x R (R=$5.74); T2 $291.25 = entry + 3x R; structure ceiling = 52w high $299.48"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $770.7M; pass"
invalidation: "loses EMA20 $274.03 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-05 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
