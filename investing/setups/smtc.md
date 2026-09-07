---
ticker: SMTC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $134.12 holding the uptrend (no breakdown on volume)"
entry_price: 134.12
stop_price: 122.39
stop_logic: "chandelier trail: HH22 $155.77 - 3x ATR $11.13 = $122.39 — exit when decline exceeds ~3 average daily ranges"
target_price: 151.72
target_logic: "T1 $151.72 = entry $134.12 + 1.5x R (R=$11.73); T2 $169.32 = entry + 3x R; structure ceiling = 52w high $177.33"
holding_window_days: 21
catalyst: "2026-11-23 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $427.6M; pass"
invalidation: "loses EMA20 $134.12 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
