---
ticker: DLO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $14.49 holding the uptrend (no breakdown on volume)"
entry_price: 14.49
stop_price: 13.94
stop_logic: "chandelier trail: HH22 $15.65 - 3x ATR $0.57 = $13.94 — exit when decline exceeds ~3 average daily ranges"
target_price: 15.31
target_logic: "T1 $15.31 = entry $14.49 + 1.5x R (R=$0.55); T2 $16.14 = entry + 3x R; structure ceiling = 52w high $16.51"
holding_window_days: 21
catalyst: "2026-11-11 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $28.3M; pass"
invalidation: "loses EMA20 $14.49 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
