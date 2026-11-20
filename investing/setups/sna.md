---
ticker: SNA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $363.77 holding the uptrend (no breakdown on volume)"
entry_price: 363.77
stop_price: 350.29
stop_logic: "chandelier trail: HH22 $378.04 - 3x ATR $9.25 = $350.29 — exit when decline exceeds ~3 average daily ranges"
target_price: 383.99
target_logic: "T1 $383.99 = entry $363.77 + 1.5x R (R=$13.48); T2 $404.20 = entry + 3x R; structure ceiling = 52w high $420.53"
holding_window_days: 21
catalyst: "2027-02-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $161.1M; pass"
invalidation: "loses EMA20 $363.77 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-20 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
