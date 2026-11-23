---
ticker: UI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $631.62 holding the uptrend (no breakdown on volume)"
entry_price: 631.62
stop_price: 585.02
stop_logic: "chandelier trail: HH22 $698.46 - 3x ATR $37.81 = $585.02 — exit when decline exceeds ~3 average daily ranges"
target_price: 701.52
target_logic: "T1 $701.52 = entry $631.62 + 1.5x R (R=$46.60); T2 $771.42 = entry + 3x R; structure ceiling = 52w high $1094.81"
holding_window_days: 21
catalyst: "2027-02-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $57.2M; pass"
invalidation: "loses EMA20 $631.62 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
