---
ticker: PR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $20.27 holding the uptrend (no breakdown on volume)"
entry_price: 20.27
stop_price: 19.98
stop_logic: "chandelier trail: HH22 $21.95 - 3x ATR $0.66 = $19.98 — exit when decline exceeds ~3 average daily ranges"
target_price: 20.71
target_logic: "T1 $20.71 = entry $20.27 + 1.5x R (R=$0.29); T2 $21.14 = entry + 3x R; structure ceiling = 52w high $22.49"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $181.9M; pass"
invalidation: "loses EMA20 $20.27 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-09 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
