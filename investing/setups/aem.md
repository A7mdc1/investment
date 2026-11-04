---
ticker: AEM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $179.62 holding the uptrend (no breakdown on volume)"
entry_price: 179.62
stop_price: 170.09
stop_logic: "chandelier trail: HH22 $192.39 - 3x ATR $7.43 = $170.09 — exit when decline exceeds ~3 average daily ranges"
target_price: 193.91
target_logic: "T1 $193.91 = entry $179.62 + 1.5x R (R=$9.53); T2 $208.21 = entry + 3x R; structure ceiling = 52w high $254.22"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $329.0M; pass"
invalidation: "loses EMA20 $179.62 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-04 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
