---
ticker: ASND
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $242.77 holding the uptrend (no breakdown on volume)"
entry_price: 242.77
stop_price: 237.74
stop_logic: "chandelier trail: HH22 $255.61 - 3x ATR $5.96 = $237.74 — exit when decline exceeds ~3 average daily ranges"
target_price: 250.31
target_logic: "T1 $250.31 = entry $242.77 + 1.5x R (R=$5.03); T2 $257.86 = entry + 3x R; structure ceiling = 52w high $282.23"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $147.3M; pass"
invalidation: "loses EMA20 $242.77 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-04 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
