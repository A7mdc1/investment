---
ticker: ANET
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $185.91 holding the uptrend (no breakdown on volume)"
entry_price: 185.91
stop_price: 176.35
stop_logic: "chandelier trail: HH22 $212.15 - 3x ATR $11.93 = $176.35 — exit when decline exceeds ~3 average daily ranges"
target_price: 200.25
target_logic: "T1 $200.25 = entry $185.91 + 1.5x R (R=$9.56); T2 $214.59 = entry + 3x R; structure ceiling = 52w high $217.52"
holding_window_days: 21
catalyst: "2027-02-09 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1549.4M; pass"
invalidation: "loses EMA20 $185.91 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
