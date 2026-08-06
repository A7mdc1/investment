---
ticker: UTHR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $528.27 holding the uptrend (no breakdown on volume)"
entry_price: 528.27
stop_price: 523.55
stop_logic: "chandelier trail: HH22 $563.25 - 3x ATR $13.23 = $523.55 — exit when decline exceeds ~3 average daily ranges"
target_price: 535.34
target_logic: "T1 $535.34 = entry $528.27 + 1.5x R (R=$4.72); T2 $542.41 = entry + 3x R; structure ceiling = 52w high $609.15"
holding_window_days: 21
catalyst: "2026-10-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $231.0M; pass"
invalidation: "loses EMA20 $528.27 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
