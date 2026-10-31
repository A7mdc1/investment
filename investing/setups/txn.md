---
ticker: TXN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $289.43 holding the uptrend (no breakdown on volume)"
entry_price: 289.43
stop_price: 282.22
stop_logic: "chandelier trail: HH22 $311.55 - 3x ATR $9.78 = $282.22 — exit when decline exceeds ~3 average daily ranges"
target_price: 300.24
target_logic: "T1 $300.24 = entry $289.43 + 1.5x R (R=$7.21); T2 $311.04 = entry + 3x R; structure ceiling = 52w high $330.59"
holding_window_days: 21
catalyst: "2027-01-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2067.5M; pass"
invalidation: "loses EMA20 $289.43 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-31 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
