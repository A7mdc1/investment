---
ticker: DDS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $627.68 holding the uptrend (no breakdown on volume)"
entry_price: 627.68
stop_price: 582.85
stop_logic: "chandelier trail: HH22 $661.99 - 3x ATR $26.38 = $582.85 — exit when decline exceeds ~3 average daily ranges"
target_price: 694.92
target_logic: "T1 $694.92 = entry $627.68 + 1.5x R (R=$44.83); T2 $762.17 = entry + 3x R; structure ceiling = 52w high $710.23"
holding_window_days: 21
catalyst: "2026-11-12 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $104.7M; pass"
invalidation: "loses EMA20 $627.68 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
