---
ticker: TXN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $291.49 holding the uptrend (no breakdown on volume)"
entry_price: 291.49
stop_price: 281.01
stop_logic: "chandelier trail: HH22 $317.20 - 3x ATR $12.06 = $281.01 — exit when decline exceeds ~3 average daily ranges"
target_price: 307.19
target_logic: "T1 $307.19 = entry $291.49 + 1.5x R (R=$10.47); T2 $322.90 = entry + 3x R; structure ceiling = 52w high $330.78"
holding_window_days: 21
catalyst: "2027-01-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2616.1M; pass"
invalidation: "loses EMA20 $291.49 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-09 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
