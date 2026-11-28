---
ticker: UI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $634.71 holding the uptrend (no breakdown on volume)"
entry_price: 634.71
stop_price: 578.78
stop_logic: "chandelier trail: HH22 $698.46 - 3x ATR $39.89 = $578.78 — exit when decline exceeds ~3 average daily ranges"
target_price: 718.61
target_logic: "T1 $718.61 = entry $634.71 + 1.5x R (R=$55.93); T2 $802.52 = entry + 3x R; structure ceiling = 52w high $1095.42"
holding_window_days: 21
catalyst: "2027-02-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $60.4M; pass"
invalidation: "loses EMA20 $634.71 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-28 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
