---
ticker: ASND
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $238.48 holding the uptrend (no breakdown on volume)"
entry_price: 238.48
stop_price: 237.08
stop_logic: "chandelier trail: HH22 $254.20 - 3x ATR $5.71 = $237.08 — exit when decline exceeds ~3 average daily ranges"
target_price: 240.58
target_logic: "T1 $240.58 = entry $238.48 + 1.5x R (R=$1.40); T2 $242.69 = entry + 3x R; structure ceiling = 52w high $282.31"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $160.2M; pass"
invalidation: "loses EMA20 $238.48 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-29 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
