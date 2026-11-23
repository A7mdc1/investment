---
ticker: KLAC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $149.54 holding the uptrend (no breakdown on volume)"
entry_price: 149.54
stop_price: 139.78
stop_logic: "chandelier trail: HH22 $171.05 - 3x ATR $10.42 = $139.78 — exit when decline exceeds ~3 average daily ranges"
target_price: 164.18
target_logic: "T1 $164.18 = entry $149.54 + 1.5x R (R=$9.76); T2 $178.82 = entry + 3x R; structure ceiling = 52w high $306.35"
holding_window_days: 21
catalyst: "2027-01-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2167.7M; pass"
invalidation: "loses EMA20 $149.54 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
