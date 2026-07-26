---
ticker: NEM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $94.72 holding the uptrend (no breakdown on volume)"
entry_price: 94.72
stop_price: 89.07
stop_logic: "chandelier trail: HH22 $98.93 - 3x ATR $3.29 = $89.07 — exit when decline exceeds ~3 average daily ranges"
target_price: 103.20
target_logic: "T1 $103.20 = entry $94.72 + 1.5x R (R=$5.65); T2 $111.68 = entry + 3x R; structure ceiling = 52w high $134.28"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $739.5M; pass"
invalidation: "loses EMA20 $94.72 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-26 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
