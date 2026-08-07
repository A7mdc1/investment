---
ticker: PDFS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $50.12 holding the uptrend (no breakdown on volume)"
entry_price: 50.12
stop_price: 45.36
stop_logic: "chandelier trail: HH22 $57.20 - 3x ATR $3.95 = $45.36 — exit when decline exceeds ~3 average daily ranges"
target_price: 57.26
target_logic: "T1 $57.26 = entry $50.12 + 1.5x R (R=$4.76); T2 $64.40 = entry + 3x R; structure ceiling = 52w high $71.73"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $23.7M; pass"
invalidation: "loses EMA20 $50.12 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
