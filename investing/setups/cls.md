---
ticker: CLS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $333.71 holding the uptrend (no breakdown on volume)"
entry_price: 333.71
stop_price: 299.84
stop_logic: "chandelier trail: HH22 $378.99 - 3x ATR $26.38 = $299.84 — exit when decline exceeds ~3 average daily ranges"
target_price: 384.51
target_logic: "T1 $384.51 = entry $333.71 + 1.5x R (R=$33.87); T2 $435.31 = entry + 3x R; structure ceiling = 52w high $474.22"
holding_window_days: 21
catalyst: "2026-10-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1118.2M; pass"
invalidation: "loses EMA20 $333.71 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-18 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
