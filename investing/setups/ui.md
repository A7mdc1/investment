---
ticker: UI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $632.22 holding the uptrend (no breakdown on volume)"
entry_price: 632.22
stop_price: 578.43
stop_logic: "chandelier trail: HH22 $698.46 - 3x ATR $40.01 = $578.43 — exit when decline exceeds ~3 average daily ranges"
target_price: 712.91
target_logic: "T1 $712.91 = entry $632.22 + 1.5x R (R=$53.79); T2 $793.60 = entry + 3x R; structure ceiling = 52w high $1094.61"
holding_window_days: 21
catalyst: "2027-02-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $61.1M; pass"
invalidation: "loses EMA20 $632.22 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-26 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
