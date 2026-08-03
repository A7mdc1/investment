---
ticker: AEM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $147.04 holding the uptrend (no breakdown on volume)"
entry_price: 147.04
stop_price: 141.78
stop_logic: "chandelier trail: HH22 $158.07 - 3x ATR $5.43 = $141.78 — exit when decline exceeds ~3 average daily ranges"
target_price: 154.92
target_logic: "T1 $154.92 = entry $147.04 + 1.5x R (R=$5.25); T2 $162.80 = entry + 3x R; structure ceiling = 52w high $254.53"
holding_window_days: 21
catalyst: "2026-10-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $340.3M; pass"
invalidation: "loses EMA20 $147.04 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-03 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
