---
ticker: PNFP
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $97.12 holding the uptrend (no breakdown on volume)"
entry_price: 97.12
stop_price: 95.25
stop_logic: "chandelier trail: HH22 $102.09 - 3x ATR $2.28 = $95.25 — exit when decline exceeds ~3 average daily ranges"
target_price: 99.93
target_logic: "T1 $99.93 = entry $97.12 + 1.5x R (R=$1.87); T2 $102.74 = entry + 3x R; structure ceiling = 52w high $109.80"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $112.2M; pass"
invalidation: "loses EMA20 $97.12 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-28 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
