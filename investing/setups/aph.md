---
ticker: APH
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $155.62 holding the uptrend (no breakdown on volume)"
entry_price: 155.62
stop_price: 151.98
stop_logic: "chandelier trail: HH22 $174.14 - 3x ATR $7.39 = $151.98 — exit when decline exceeds ~3 average daily ranges"
target_price: 161.08
target_logic: "T1 $161.08 = entry $155.62 + 1.5x R (R=$3.64); T2 $166.54 = entry + 3x R; structure ceiling = 52w high $178.56"
holding_window_days: 21
catalyst: "2026-10-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1082.0M; pass"
invalidation: "loses EMA20 $155.62 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-02 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
