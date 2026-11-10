---
ticker: PSX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $267.14 holding the uptrend (no breakdown on volume)"
entry_price: 267.14
stop_price: 267.00
stop_logic: "chandelier trail: HH22 $299.39 - 3x ATR $10.80 = $267.00 — exit when decline exceeds ~3 average daily ranges"
target_price: 267.34
target_logic: "T1 $267.34 = entry $267.14 + 1.5x R (R=$0.14); T2 $267.55 = entry + 3x R; structure ceiling = 52w high $299.44"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $796.6M; pass"
invalidation: "loses EMA20 $267.14 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
