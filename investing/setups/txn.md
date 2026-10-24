---
ticker: TXN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $280.59 holding the uptrend (no breakdown on volume)"
entry_price: 280.59
stop_price: 272.55
stop_logic: "chandelier trail: HH22 $298.75 - 3x ATR $8.73 = $272.55 — exit when decline exceeds ~3 average daily ranges"
target_price: 292.65
target_logic: "T1 $292.65 = entry $280.59 + 1.5x R (R=$8.04); T2 $304.71 = entry + 3x R; structure ceiling = 52w high $332.19"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1760.5M; pass"
invalidation: "loses EMA20 $280.59 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-24 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
