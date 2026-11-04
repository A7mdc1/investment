---
ticker: TXN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $294.36 holding the uptrend (no breakdown on volume)"
entry_price: 294.36
stop_price: 286.34
stop_logic: "chandelier trail: HH22 $317.16 - 3x ATR $10.27 = $286.34 — exit when decline exceeds ~3 average daily ranges"
target_price: 306.39
target_logic: "T1 $306.39 = entry $294.36 + 1.5x R (R=$8.02); T2 $318.43 = entry + 3x R; structure ceiling = 52w high $330.58"
holding_window_days: 21
catalyst: "2027-01-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2285.1M; pass"
invalidation: "loses EMA20 $294.36 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-04 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
