---
ticker: ANET
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $182.51 holding the uptrend (no breakdown on volume)"
entry_price: 182.51
stop_price: 170.59
stop_logic: "chandelier trail: HH22 $205.20 - 3x ATR $11.54 = $170.59 — exit when decline exceeds ~3 average daily ranges"
target_price: 200.38
target_logic: "T1 $200.38 = entry $182.51 + 1.5x R (R=$11.92); T2 $218.26 = entry + 3x R; structure ceiling = 52w high $217.51"
holding_window_days: 21
catalyst: "2027-02-09 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1467.8M; pass"
invalidation: "loses EMA20 $182.51 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
