---
ticker: LLY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $1207.76 holding the uptrend (no breakdown on volume)"
entry_price: 1207.76
stop_price: 1164.80
stop_logic: "chandelier trail: HH22 $1292.65 - 3x ATR $42.62 = $1164.80 — exit when decline exceeds ~3 average daily ranges"
target_price: 1272.21
target_logic: "T1 $1272.21 = entry $1207.76 + 1.5x R (R=$42.96); T2 $1336.65 = entry + 3x R; structure ceiling = 52w high $1292.25"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $3337.1M; pass"
invalidation: "loses EMA20 $1207.76 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
