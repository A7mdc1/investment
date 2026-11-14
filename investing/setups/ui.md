---
ticker: UI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $619.25 holding the uptrend (no breakdown on volume)"
entry_price: 619.25
stop_price: 603.63
stop_logic: "chandelier trail: HH22 $699.50 - 3x ATR $31.96 = $603.63 — exit when decline exceeds ~3 average daily ranges"
target_price: 642.69
target_logic: "T1 $642.69 = entry $619.25 + 1.5x R (R=$15.62); T2 $666.12 = entry + 3x R; structure ceiling = 52w high $1096.17"
holding_window_days: 21
catalyst: "2027-02-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $54.1M; pass"
invalidation: "loses EMA20 $619.25 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
