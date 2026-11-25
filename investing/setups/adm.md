---
ticker: ADM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $70.14 holding the uptrend (no breakdown on volume)"
entry_price: 70.14
stop_price: 73.00
stop_logic: "chandelier trail: HH22 $79.30 - 3x ATR $2.10 = $73.00 — exit when decline exceeds ~3 average daily ranges"
target_price: null
target_logic: null           # scaffold: target unavailable (needs entry>stop for R)
holding_window_days: 21
catalyst: "2027-02-02 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $287.0M; pass"
invalidation: "loses EMA20 $70.14 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-25 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
