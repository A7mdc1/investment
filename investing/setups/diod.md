---
ticker: DIOD
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $85.60 holding the uptrend (no breakdown on volume)"
entry_price: 85.60
stop_price: 76.60
stop_logic: "chandelier trail: HH22 $94.64 - 3x ATR $6.01 = $76.60 — exit when decline exceeds ~3 average daily ranges"
target_price: 99.10
target_logic: "T1 $99.10 = entry $85.60 + 1.5x R (R=$9.00); T2 $112.61 = entry + 3x R; structure ceiling = 52w high $125.94"
holding_window_days: 21
catalyst: "2027-02-09 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $46.2M; pass"
invalidation: "loses EMA20 $85.60 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
