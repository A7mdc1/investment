---
ticker: SNA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $363.71 holding the uptrend (no breakdown on volume)"
entry_price: 363.71
stop_price: 350.71
stop_logic: "chandelier trail: HH22 $374.86 - 3x ATR $8.05 = $350.71 — exit when decline exceeds ~3 average daily ranges"
target_price: 383.21
target_logic: "T1 $383.21 = entry $363.71 + 1.5x R (R=$13.00); T2 $402.71 = entry + 3x R; structure ceiling = 52w high $420.27"
holding_window_days: 21
catalyst: "2027-02-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $166.7M; pass"
invalidation: "loses EMA20 $363.71 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
