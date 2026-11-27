---
ticker: HSY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $174.12 holding the uptrend (no breakdown on volume)"
entry_price: 174.12
stop_price: 167.63
stop_logic: "chandelier trail: HH22 $183.98 - 3x ATR $5.45 = $167.63 — exit when decline exceeds ~3 average daily ranges"
target_price: 183.86
target_logic: "T1 $183.86 = entry $174.12 + 1.5x R (R=$6.49); T2 $193.60 = entry + 3x R; structure ceiling = 52w high $233.88"
holding_window_days: 21
catalyst: "2027-02-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $365.6M; pass"
invalidation: "loses EMA20 $174.12 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
