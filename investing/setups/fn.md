---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $326.66 holding the uptrend (no breakdown on volume)"
entry_price: 326.66
stop_price: 278.46
stop_logic: "chandelier trail: HH22 $379.43 - 3x ATR $33.66 = $278.46 — exit when decline exceeds ~3 average daily ranges"
target_price: 398.95
target_logic: "T1 $398.95 = entry $326.66 + 1.5x R (R=$48.20); T2 $471.25 = entry + 3x R; structure ceiling = 52w high $748.58"
holding_window_days: 21
catalyst: "2027-02-01 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $409.3M; pass"
invalidation: "loses EMA20 $326.66 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-26 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
