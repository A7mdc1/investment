---
ticker: TRV
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $395.27 holding the uptrend (no breakdown on volume)"
entry_price: 395.27
stop_price: 392.30
stop_logic: "chandelier trail: HH22 $418.00 - 3x ATR $8.57 = $392.30 — exit when decline exceeds ~3 average daily ranges"
target_price: 399.72
target_logic: "T1 $399.72 = entry $395.27 + 1.5x R (R=$2.97); T2 $404.18 = entry + 3x R; structure ceiling = 52w high $418.17"
holding_window_days: 21
catalyst: "2027-01-20 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $580.0M; pass"
invalidation: "loses EMA20 $395.27 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
