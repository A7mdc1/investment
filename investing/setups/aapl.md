---
ticker: AAPL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $340.87 holding the uptrend (no breakdown on volume)"
entry_price: 340.87
stop_price: 331.12
stop_logic: "chandelier trail: HH22 $351.73 - 3x ATR $6.87 = $331.12 — exit when decline exceeds ~3 average daily ranges"
target_price: 355.49
target_logic: "T1 $355.49 = entry $340.87 + 1.5x R (R=$9.75); T2 $370.11 = entry + 3x R; structure ceiling = 52w high $351.75"
holding_window_days: 21
catalyst: "2027-01-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $14367.9M; pass"
invalidation: "loses EMA20 $340.87 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-03 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
