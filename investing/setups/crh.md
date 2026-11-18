---
ticker: CRH
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $91.64 holding the uptrend (no breakdown on volume)"
entry_price: 91.64
stop_price: 90.03
stop_logic: "chandelier trail: HH22 $99.75 - 3x ATR $3.24 = $90.03 — exit when decline exceeds ~3 average daily ranges"
target_price: 94.04
target_logic: "T1 $94.04 = entry $91.64 + 1.5x R (R=$1.60); T2 $96.45 = entry + 3x R; structure ceiling = 52w high $129.50"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $487.4M; pass"
invalidation: "loses EMA20 $91.64 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-18 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
