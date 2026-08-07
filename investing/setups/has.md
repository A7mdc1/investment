---
ticker: HAS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $89.37 holding the uptrend (no breakdown on volume)"
entry_price: 89.37
stop_price: 88.64
stop_logic: "chandelier trail: HH22 $97.00 - 3x ATR $2.79 = $88.64 — exit when decline exceeds ~3 average daily ranges"
target_price: 90.46
target_logic: "T1 $90.46 = entry $89.37 + 1.5x R (R=$0.73); T2 $91.55 = entry + 3x R; structure ceiling = 52w high $105.39"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $211.7M; pass"
invalidation: "loses EMA20 $89.37 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
