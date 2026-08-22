---
ticker: XOM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $158.10 holding the uptrend (no breakdown on volume)"
entry_price: 158.10
stop_price: 157.04
stop_logic: "chandelier trail: HH22 $168.64 - 3x ATR $3.87 = $157.04 — exit when decline exceeds ~3 average daily ranges"
target_price: 159.70
target_logic: "T1 $159.70 = entry $158.10 + 1.5x R (R=$1.07); T2 $161.30 = entry + 3x R; structure ceiling = 52w high $174.17"
holding_window_days: 21
catalyst: "2026-10-30 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2250.8M; pass"
invalidation: "loses EMA20 $158.10 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-22 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
