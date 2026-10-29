---
ticker: AEM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $183.24 holding the uptrend (no breakdown on volume)"
entry_price: 183.24
stop_price: 173.51
stop_logic: "chandelier trail: HH22 $192.39 - 3x ATR $6.29 = $173.51 — exit when decline exceeds ~3 average daily ranges"
target_price: 197.84
target_logic: "T1 $197.84 = entry $183.24 + 1.5x R (R=$9.73); T2 $212.44 = entry + 3x R; structure ceiling = 52w high $254.04"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $290.5M; pass"
invalidation: "loses EMA20 $183.24 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-29 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
