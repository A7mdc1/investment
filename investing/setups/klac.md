---
ticker: KLAC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $156.23 holding the uptrend (no breakdown on volume)"
entry_price: 156.23
stop_price: 144.61
stop_logic: "chandelier trail: HH22 $173.05 - 3x ATR $9.48 = $144.61 — exit when decline exceeds ~3 average daily ranges"
target_price: 173.66
target_logic: "T1 $173.66 = entry $156.23 + 1.5x R (R=$11.62); T2 $191.09 = entry + 3x R; structure ceiling = 52w high $306.86"
holding_window_days: 21
catalyst: "2027-01-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2158.7M; pass"
invalidation: "loses EMA20 $156.23 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
