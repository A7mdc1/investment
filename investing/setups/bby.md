---
ticker: BBY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $85.37 holding the uptrend (no breakdown on volume)"
entry_price: 85.37
stop_price: 81.48
stop_logic: "chandelier trail: HH22 $91.27 - 3x ATR $3.26 = $81.48 — exit when decline exceeds ~3 average daily ranges"
target_price: 91.20
target_logic: "T1 $91.20 = entry $85.37 + 1.5x R (R=$3.89); T2 $97.04 = entry + 3x R; structure ceiling = 52w high $91.22"
holding_window_days: 21
catalyst: "2026-11-24 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $319.4M; pass"
invalidation: "loses EMA20 $85.37 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-29 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
