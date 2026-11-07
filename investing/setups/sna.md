---
ticker: SNA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $363.62 holding the uptrend (no breakdown on volume)"
entry_price: 363.62
stop_price: 350.70
stop_logic: "chandelier trail: HH22 $374.86 - 3x ATR $8.05 = $350.70 — exit when decline exceeds ~3 average daily ranges"
target_price: 383.01
target_logic: "T1 $383.01 = entry $363.62 + 1.5x R (R=$12.93); T2 $402.40 = entry + 3x R; structure ceiling = 52w high $420.64"
holding_window_days: 21
catalyst: "2027-02-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $171.2M; pass"
invalidation: "loses EMA20 $363.62 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
