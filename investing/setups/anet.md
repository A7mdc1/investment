---
ticker: ANET
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $185.90 holding the uptrend (no breakdown on volume)"
entry_price: 185.90
stop_price: 176.96
stop_logic: "chandelier trail: HH22 $212.16 - 3x ATR $11.73 = $176.96 — exit when decline exceeds ~3 average daily ranges"
target_price: 199.29
target_logic: "T1 $199.29 = entry $185.90 + 1.5x R (R=$8.93); T2 $212.69 = entry + 3x R; structure ceiling = 52w high $217.33"
holding_window_days: 21
catalyst: "2027-02-09 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1523.0M; pass"
invalidation: "loses EMA20 $185.90 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
