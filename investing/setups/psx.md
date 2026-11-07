---
ticker: PSX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $270.68 holding the uptrend (no breakdown on volume)"
entry_price: 270.68
stop_price: 267.15
stop_logic: "chandelier trail: HH22 $299.39 - 3x ATR $10.75 = $267.15 — exit when decline exceeds ~3 average daily ranges"
target_price: 275.98
target_logic: "T1 $275.98 = entry $270.68 + 1.5x R (R=$3.53); T2 $281.28 = entry + 3x R; structure ceiling = 52w high $299.29"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $807.2M; pass"
invalidation: "loses EMA20 $270.68 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
