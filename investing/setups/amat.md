---
ticker: AMAT
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $387.14 holding the uptrend (no breakdown on volume)"
entry_price: 387.14
stop_price: 355.05
stop_logic: "chandelier trail: HH22 $427.66 - 3x ATR $24.20 = $355.05 — exit when decline exceeds ~3 average daily ranges"
target_price: 435.27
target_logic: "T1 $435.27 = entry $387.14 + 1.5x R (R=$32.09); T2 $483.41 = entry + 3x R; structure ceiling = 52w high $738.73"
holding_window_days: 21
catalyst: "2027-02-11 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $3118.3M; pass"
invalidation: "loses EMA20 $387.14 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
