---
ticker: KEYS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $291.06 holding the uptrend (no breakdown on volume)"
entry_price: 291.06
stop_price: 287.20
stop_logic: "chandelier trail: HH22 $340.43 - 3x ATR $17.74 = $287.20 — exit when decline exceeds ~3 average daily ranges"
target_price: 296.85
target_logic: "T1 $296.85 = entry $291.06 + 1.5x R (R=$3.86); T2 $302.64 = entry + 3x R; structure ceiling = 52w high $389.75"
holding_window_days: 21
catalyst: "2027-02-23 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $497.6M; pass"
invalidation: "loses EMA20 $291.06 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-25 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
