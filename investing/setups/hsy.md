---
ticker: HSY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $173.37 holding the uptrend (no breakdown on volume)"
entry_price: 173.37
stop_price: 166.97
stop_logic: "chandelier trail: HH22 $183.59 - 3x ATR $5.54 = $166.97 — exit when decline exceeds ~3 average daily ranges"
target_price: 182.97
target_logic: "T1 $182.97 = entry $173.37 + 1.5x R (R=$6.40); T2 $192.57 = entry + 3x R; structure ceiling = 52w high $233.89"
holding_window_days: 21
catalyst: "2027-02-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $366.6M; pass"
invalidation: "loses EMA20 $173.37 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-25 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
