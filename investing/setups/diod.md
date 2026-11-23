---
ticker: DIOD
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $83.58 holding the uptrend (no breakdown on volume)"
entry_price: 83.58
stop_price: 75.42
stop_logic: "chandelier trail: HH22 $94.64 - 3x ATR $6.41 = $75.42 — exit when decline exceeds ~3 average daily ranges"
target_price: 95.81
target_logic: "T1 $95.81 = entry $83.58 + 1.5x R (R=$8.16); T2 $108.05 = entry + 3x R; structure ceiling = 52w high $125.95"
holding_window_days: 21
catalyst: "2027-02-09 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $44.4M; pass"
invalidation: "loses EMA20 $83.58 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
