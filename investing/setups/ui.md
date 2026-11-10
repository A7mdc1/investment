---
ticker: UI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $598.71 holding the uptrend (no breakdown on volume)"
entry_price: 598.71
stop_price: 593.11
stop_logic: "chandelier trail: HH22 $690.00 - 3x ATR $32.30 = $593.11 — exit when decline exceeds ~3 average daily ranges"
target_price: 607.11
target_logic: "T1 $607.11 = entry $598.71 + 1.5x R (R=$5.60); T2 $615.51 = entry + 3x R; structure ceiling = 52w high $1096.34"
holding_window_days: 21
catalyst: "2027-02-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $54.1M; pass"
invalidation: "loses EMA20 $598.71 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
