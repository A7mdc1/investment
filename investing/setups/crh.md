---
ticker: CRH
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $91.98 holding the uptrend (no breakdown on volume)"
entry_price: 91.98
stop_price: 90.77
stop_logic: "chandelier trail: HH22 $100.17 - 3x ATR $3.13 = $90.77 — exit when decline exceeds ~3 average daily ranges"
target_price: 93.78
target_logic: "T1 $93.78 = entry $91.98 + 1.5x R (R=$1.20); T2 $95.59 = entry + 3x R; structure ceiling = 52w high $130.10"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $492.9M; pass"
invalidation: "loses EMA20 $91.98 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
