---
ticker: TXN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $287.05 holding the uptrend (no breakdown on volume)"
entry_price: 287.05
stop_price: 266.03
stop_logic: "chandelier trail: HH22 $317.20 - 3x ATR $17.06 = $266.03 — exit when decline exceeds ~3 average daily ranges"
target_price: 318.58
target_logic: "T1 $318.58 = entry $287.05 + 1.5x R (R=$21.02); T2 $350.11 = entry + 3x R; structure ceiling = 52w high $330.71"
holding_window_days: 21
catalyst: "2027-01-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2780.3M; pass"
invalidation: "loses EMA20 $287.05 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-26 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
