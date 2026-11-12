---
ticker: LSCC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $109.49 holding the uptrend (no breakdown on volume)"
entry_price: 109.49
stop_price: 99.56
stop_logic: "chandelier trail: HH22 $123.18 - 3x ATR $7.87 = $99.56 — exit when decline exceeds ~3 average daily ranges"
target_price: 124.37
target_logic: "T1 $124.37 = entry $109.49 + 1.5x R (R=$9.92); T2 $139.26 = entry + 3x R; structure ceiling = 52w high $157.06"
holding_window_days: 21
catalyst: "2027-02-08 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $300.2M; pass"
invalidation: "loses EMA20 $109.49 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
