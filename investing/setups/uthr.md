---
ticker: UTHR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $520.36 holding the uptrend (no breakdown on volume)"
entry_price: 520.36
stop_price: 500.71
stop_logic: "chandelier trail: HH22 $541.25 - 3x ATR $13.51 = $500.71 — exit when decline exceeds ~3 average daily ranges"
target_price: 549.83
target_logic: "T1 $549.83 = entry $520.36 + 1.5x R (R=$19.65); T2 $579.30 = entry + 3x R; structure ceiling = 52w high $609.23"
holding_window_days: 21
catalyst: "2026-10-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $267.7M; pass"
invalidation: "loses EMA20 $520.36 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-18 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
