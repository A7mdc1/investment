---
ticker: NEM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $94.16 holding the uptrend (no breakdown on volume)"
entry_price: 94.16
stop_price: 89.00
stop_logic: "chandelier trail: HH22 $98.93 - 3x ATR $3.31 = $89.00 — exit when decline exceeds ~3 average daily ranges"
target_price: 101.90
target_logic: "T1 $101.90 = entry $94.16 + 1.5x R (R=$5.16); T2 $109.64 = entry + 3x R; structure ceiling = 52w high $134.34"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $654.6M; pass"
invalidation: "loses EMA20 $94.16 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-03 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
