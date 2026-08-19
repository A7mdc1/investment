---
ticker: NET
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $293.95 holding the uptrend (no breakdown on volume)"
entry_price: 293.95
stop_price: 282.83
stop_logic: "chandelier trail: HH22 $332.22 - 3x ATR $16.46 = $282.83 — exit when decline exceeds ~3 average daily ranges"
target_price: 310.64
target_logic: "T1 $310.64 = entry $293.95 + 1.5x R (R=$11.12); T2 $327.32 = entry + 3x R; structure ceiling = 52w high $332.24"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1166.9M; pass"
invalidation: "loses EMA20 $293.95 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
