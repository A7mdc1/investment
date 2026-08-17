---
ticker: KGC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $25.76 holding the uptrend (no breakdown on volume)"
entry_price: 25.76
stop_price: 25.07
stop_logic: "chandelier trail: HH22 $28.04 - 3x ATR $0.99 = $25.07 — exit when decline exceeds ~3 average daily ranges"
target_price: 26.81
target_logic: "T1 $26.81 = entry $25.76 + 1.5x R (R=$0.70); T2 $27.86 = entry + 3x R; structure ceiling = 52w high $39.02"
holding_window_days: 21
catalyst: "2026-11-10 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $191.9M; pass"
invalidation: "loses EMA20 $25.76 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
