---
ticker: SNA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $363.38 holding the uptrend (no breakdown on volume)"
entry_price: 363.38
stop_price: 350.93
stop_logic: "chandelier trail: HH22 $372.26 - 3x ATR $7.11 = $350.93 — exit when decline exceeds ~3 average daily ranges"
target_price: 382.04
target_logic: "T1 $382.04 = entry $363.38 + 1.5x R (R=$12.45); T2 $400.71 = entry + 3x R; structure ceiling = 52w high $420.32"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $139.4M; pass"
invalidation: "loses EMA20 $363.38 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-28 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
