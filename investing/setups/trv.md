---
ticker: TRV
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $392.62 holding the uptrend (no breakdown on volume)"
entry_price: 392.62
stop_price: 390.74
stop_logic: "chandelier trail: HH22 $418.00 - 3x ATR $9.09 = $390.74 — exit when decline exceeds ~3 average daily ranges"
target_price: 395.45
target_logic: "T1 $395.45 = entry $392.62 + 1.5x R (R=$1.88); T2 $398.27 = entry + 3x R; structure ceiling = 52w high $418.05"
holding_window_days: 21
catalyst: "2027-01-20 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $629.9M; pass"
invalidation: "loses EMA20 $392.62 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-09 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
