---
ticker: AEM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $148.94 holding the uptrend (no breakdown on volume)"
entry_price: 148.94
stop_price: 147.89
stop_logic: "chandelier trail: HH22 $165.34 - 3x ATR $5.82 = $147.89 — exit when decline exceeds ~3 average daily ranges"
target_price: 150.53
target_logic: "T1 $150.53 = entry $148.94 + 1.5x R (R=$1.06); T2 $152.11 = entry + 3x R; structure ceiling = 52w high $254.53"
holding_window_days: 21
catalyst: "2026-10-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $341.7M; pass"
invalidation: "loses EMA20 $148.94 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-05 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
