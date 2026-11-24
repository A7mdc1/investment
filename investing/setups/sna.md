---
ticker: SNA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $360.21 holding the uptrend (no breakdown on volume)"
entry_price: 360.21
stop_price: 351.17
stop_logic: "chandelier trail: HH22 $375.13 - 3x ATR $7.99 = $351.17 — exit when decline exceeds ~3 average daily ranges"
target_price: 373.79
target_logic: "T1 $373.79 = entry $360.21 + 1.5x R (R=$9.05); T2 $387.36 = entry + 3x R; structure ceiling = 52w high $417.32"
holding_window_days: 21
catalyst: "2027-02-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $157.9M; pass"
invalidation: "loses EMA20 $360.21 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-24 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
