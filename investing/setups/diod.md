---
ticker: DIOD
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $85.74 holding the uptrend (no breakdown on volume)"
entry_price: 85.74
stop_price: 76.51
stop_logic: "chandelier trail: HH22 $94.64 - 3x ATR $6.04 = $76.51 — exit when decline exceeds ~3 average daily ranges"
target_price: 99.58
target_logic: "T1 $99.58 = entry $85.74 + 1.5x R (R=$9.23); T2 $113.43 = entry + 3x R; structure ceiling = 52w high $125.90"
holding_window_days: 21
catalyst: "2027-02-09 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $47.0M; pass"
invalidation: "loses EMA20 $85.74 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
