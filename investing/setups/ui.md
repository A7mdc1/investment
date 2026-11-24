---
ticker: UI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $630.02 holding the uptrend (no breakdown on volume)"
entry_price: 630.02
stop_price: 583.17
stop_logic: "chandelier trail: HH22 $698.46 - 3x ATR $38.43 = $583.17 — exit when decline exceeds ~3 average daily ranges"
target_price: 700.29
target_logic: "T1 $700.29 = entry $630.02 + 1.5x R (R=$46.85); T2 $770.57 = entry + 3x R; structure ceiling = 52w high $1095.33"
holding_window_days: 21
catalyst: "2027-02-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $58.7M; pass"
invalidation: "loses EMA20 $630.02 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-24 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
