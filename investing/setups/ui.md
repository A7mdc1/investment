---
ticker: UI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $627.14 holding the uptrend (no breakdown on volume)"
entry_price: 627.14
stop_price: 604.56
stop_logic: "chandelier trail: HH22 $698.46 - 3x ATR $31.30 = $604.56 — exit when decline exceeds ~3 average daily ranges"
target_price: 661.00
target_logic: "T1 $661.00 = entry $627.14 + 1.5x R (R=$22.58); T2 $694.86 = entry + 3x R; structure ceiling = 52w high $1095.26"
holding_window_days: 21
catalyst: "2027-02-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $53.4M; pass"
invalidation: "loses EMA20 $627.14 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
