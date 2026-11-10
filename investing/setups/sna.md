---
ticker: SNA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $365.43 holding the uptrend (no breakdown on volume)"
entry_price: 365.43
stop_price: 352.84
stop_logic: "chandelier trail: HH22 $377.49 - 3x ATR $8.22 = $352.84 — exit when decline exceeds ~3 average daily ranges"
target_price: 384.31
target_logic: "T1 $384.31 = entry $365.43 + 1.5x R (R=$12.59); T2 $403.20 = entry + 3x R; structure ceiling = 52w high $420.44"
holding_window_days: 21
catalyst: "2027-02-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $170.3M; pass"
invalidation: "loses EMA20 $365.43 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
