---
ticker: ADM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $71.48 holding the uptrend (no breakdown on volume)"
entry_price: 71.48
stop_price: 74.59
stop_logic: "chandelier trail: HH22 $80.57 - 3x ATR $1.99 = $74.59 — exit when decline exceeds ~3 average daily ranges"
target_price: null
target_logic: null           # scaffold: target unavailable (needs entry>stop for R)
holding_window_days: 21
catalyst: "2027-02-02 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $275.6M; pass"
invalidation: "loses EMA20 $71.48 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-21 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
