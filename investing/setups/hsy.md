---
ticker: HSY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $171.40 holding the uptrend (no breakdown on volume)"
entry_price: 171.40
stop_price: 162.18
stop_logic: "chandelier trail: HH22 $178.42 - 3x ATR $5.41 = $162.18 — exit when decline exceeds ~3 average daily ranges"
target_price: 185.24
target_logic: "T1 $185.24 = entry $171.40 + 1.5x R (R=$9.23); T2 $199.08 = entry + 3x R; structure ceiling = 52w high $233.92"
holding_window_days: 21
catalyst: "2027-02-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $347.1M; pass"
invalidation: "loses EMA20 $171.40 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
