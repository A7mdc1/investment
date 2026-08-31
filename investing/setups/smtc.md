---
ticker: SMTC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $132.07 holding the uptrend (no breakdown on volume)"
entry_price: 132.07
stop_price: 122.22
stop_logic: "chandelier trail: HH22 $155.77 - 3x ATR $11.18 = $122.22 — exit when decline exceeds ~3 average daily ranges"
target_price: 146.84
target_logic: "T1 $146.84 = entry $132.07 + 1.5x R (R=$9.85); T2 $161.61 = entry + 3x R; structure ceiling = 52w high $177.43"
holding_window_days: 21
catalyst: "2026-11-23 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $416.1M; pass"
invalidation: "loses EMA20 $132.07 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-31 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
