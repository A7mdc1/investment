---
ticker: PSX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $270.98 holding the uptrend (no breakdown on volume)"
entry_price: 270.98
stop_price: 267.16
stop_logic: "chandelier trail: HH22 $299.39 - 3x ATR $10.74 = $267.16 — exit when decline exceeds ~3 average daily ranges"
target_price: 276.70
target_logic: "T1 $276.70 = entry $270.98 + 1.5x R (R=$3.81); T2 $282.42 = entry + 3x R; structure ceiling = 52w high $299.42"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $781.0M; pass"
invalidation: "loses EMA20 $270.98 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
