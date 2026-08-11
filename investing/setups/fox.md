---
ticker: FOX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $52.84 holding the uptrend (no breakdown on volume)"
entry_price: 52.84
stop_price: 52.64
stop_logic: "chandelier trail: HH22 $57.18 - 3x ATR $1.51 = $52.64 — exit when decline exceeds ~3 average daily ranges"
target_price: 53.13
target_logic: "T1 $53.13 = entry $52.84 + 1.5x R (R=$0.20); T2 $53.43 = entry + 3x R; structure ceiling = 52w high $67.84"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $61.4M; pass"
invalidation: "loses EMA20 $52.84 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
