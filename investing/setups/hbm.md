---
ticker: HBM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $25.18 holding the uptrend (no breakdown on volume)"
entry_price: 25.18
stop_price: 24.78
stop_logic: "chandelier trail: HH22 $28.62 - 3x ATR $1.28 = $24.78 — exit when decline exceeds ~3 average daily ranges"
target_price: 25.78
target_logic: "T1 $25.78 = entry $25.18 + 1.5x R (R=$0.40); T2 $26.37 = entry + 3x R; structure ceiling = 52w high $32.16"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $132.8M; pass"
invalidation: "loses EMA20 $25.18 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
