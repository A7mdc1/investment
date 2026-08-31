---
ticker: ASND
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $252.63 holding the uptrend (no breakdown on volume)"
entry_price: 252.63
stop_price: 245.09
stop_logic: "chandelier trail: HH22 $268.98 - 3x ATR $7.96 = $245.09 — exit when decline exceeds ~3 average daily ranges"
target_price: 263.96
target_logic: "T1 $263.96 = entry $252.63 + 1.5x R (R=$7.55); T2 $275.28 = entry + 3x R; structure ceiling = 52w high $282.22"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $123.4M; pass"
invalidation: "loses EMA20 $252.63 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-31 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
