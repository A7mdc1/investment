---
ticker: SNA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $366.29 holding the uptrend (no breakdown on volume)"
entry_price: 366.29
stop_price: 352.56
stop_logic: "chandelier trail: HH22 $377.49 - 3x ATR $8.31 = $352.56 — exit when decline exceeds ~3 average daily ranges"
target_price: 386.88
target_logic: "T1 $386.88 = entry $366.29 + 1.5x R (R=$13.73); T2 $407.47 = entry + 3x R; structure ceiling = 52w high $420.31"
holding_window_days: 21
catalyst: "2027-02-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $171.1M; pass"
invalidation: "loses EMA20 $366.29 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
