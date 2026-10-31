---
ticker: SNA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $362.04 holding the uptrend (no breakdown on volume)"
entry_price: 362.04
stop_price: 350.23
stop_logic: "chandelier trail: HH22 $372.26 - 3x ATR $7.34 = $350.23 — exit when decline exceeds ~3 average daily ranges"
target_price: 379.75
target_logic: "T1 $379.75 = entry $362.04 + 1.5x R (R=$11.81); T2 $397.46 = entry + 3x R; structure ceiling = 52w high $420.40"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $154.6M; pass"
invalidation: "loses EMA20 $362.04 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-31 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
