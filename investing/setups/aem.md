---
ticker: AEM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $147.09 holding the uptrend (no breakdown on volume)"
entry_price: 147.09
stop_price: 144.35
stop_logic: "chandelier trail: HH22 $160.55 - 3x ATR $5.40 = $144.35 — exit when decline exceeds ~3 average daily ranges"
target_price: 151.19
target_logic: "T1 $151.19 = entry $147.09 + 1.5x R (R=$2.74); T2 $155.30 = entry + 3x R; structure ceiling = 52w high $254.82"
holding_window_days: 21
catalyst: "2026-10-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $367.3M; pass"
invalidation: "loses EMA20 $147.09 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-30 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
