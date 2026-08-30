---
ticker: PR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $22.22 holding the uptrend (no breakdown on volume)"
entry_price: 22.22
stop_price: 22.02
stop_logic: "chandelier trail: HH22 $24.09 - 3x ATR $0.69 = $22.02 — exit when decline exceeds ~3 average daily ranges"
target_price: 22.51
target_logic: "T1 $22.51 = entry $22.22 + 1.5x R (R=$0.20); T2 $22.81 = entry + 3x R; structure ceiling = 52w high $24.10"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $217.0M; pass"
invalidation: "loses EMA20 $22.22 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-30 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
