---
ticker: FSLR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $220.92 holding the uptrend (no breakdown on volume)"
entry_price: 220.92
stop_price: 219.81
stop_logic: "chandelier trail: HH22 $252.17 - 3x ATR $10.79 = $219.81 — exit when decline exceeds ~3 average daily ranges"
target_price: 222.58
target_logic: "T1 $222.58 = entry $220.92 + 1.5x R (R=$1.11); T2 $224.25 = entry + 3x R; structure ceiling = 52w high $320.80"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $457.5M; pass"
invalidation: "loses EMA20 $220.92 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-05 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
