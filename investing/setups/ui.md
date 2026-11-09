---
ticker: UI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $587.52 holding the uptrend (no breakdown on volume)"
entry_price: 587.52
stop_price: 568.89
stop_logic: "chandelier trail: HH22 $663.05 - 3x ATR $31.39 = $568.89 — exit when decline exceeds ~3 average daily ranges"
target_price: 615.46
target_logic: "T1 $615.46 = entry $587.52 + 1.5x R (R=$18.63); T2 $643.40 = entry + 3x R; structure ceiling = 52w high $1096.83"
holding_window_days: 21
catalyst: "2027-02-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $51.5M; pass"
invalidation: "loses EMA20 $587.52 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-09 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
