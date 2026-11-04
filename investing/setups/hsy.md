---
ticker: HSY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $167.57 holding the uptrend (no breakdown on volume)"
entry_price: 167.57
stop_price: 162.62
stop_logic: "chandelier trail: HH22 $175.75 - 3x ATR $4.38 = $162.62 — exit when decline exceeds ~3 average daily ranges"
target_price: 175.00
target_logic: "T1 $175.00 = entry $167.57 + 1.5x R (R=$4.95); T2 $182.42 = entry + 3x R; structure ceiling = 52w high $235.88"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $272.2M; pass"
invalidation: "loses EMA20 $167.57 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-04 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
