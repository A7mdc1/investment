---
ticker: VLO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $298.70 holding the uptrend (no breakdown on volume)"
entry_price: 298.70
stop_price: 284.95
stop_logic: "chandelier trail: HH22 $319.01 - 3x ATR $11.35 = $284.95 — exit when decline exceeds ~3 average daily ranges"
target_price: 319.33
target_logic: "T1 $319.33 = entry $298.70 + 1.5x R (R=$13.75); T2 $339.96 = entry + 3x R; structure ceiling = 52w high $319.05"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $881.4M; pass"
invalidation: "loses EMA20 $298.70 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-08 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
