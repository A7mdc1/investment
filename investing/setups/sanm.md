---
ticker: SANM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $158.36 holding the uptrend (no breakdown on volume)"
entry_price: 158.36
stop_price: 137.96
stop_logic: "chandelier trail: HH22 $177.19 - 3x ATR $13.08 = $137.96 — exit when decline exceeds ~3 average daily ranges"
target_price: 188.95
target_logic: "T1 $188.95 = entry $158.36 + 1.5x R (R=$20.40); T2 $219.55 = entry + 3x R; structure ceiling = 52w high $288.81"
holding_window_days: 21
catalyst: "2027-02-01 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $172.7M; pass"
invalidation: "loses EMA20 $158.36 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
