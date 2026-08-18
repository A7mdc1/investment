---
ticker: IAG
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $16.86 holding the uptrend (no breakdown on volume)"
entry_price: 16.86
stop_price: 16.77
stop_logic: "chandelier trail: HH22 $19.19 - 3x ATR $0.81 = $16.77 — exit when decline exceeds ~3 average daily ranges"
target_price: 16.99
target_logic: "T1 $16.99 = entry $16.86 + 1.5x R (R=$0.09); T2 $17.12 = entry + 3x R; structure ceiling = 52w high $24.87"
holding_window_days: 21
catalyst: "2026-11-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $95.4M; pass"
invalidation: "loses EMA20 $16.86 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-18 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
