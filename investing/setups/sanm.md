---
ticker: SANM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $161.25 holding the uptrend (no breakdown on volume)"
entry_price: 161.25
stop_price: 140.26
stop_logic: "chandelier trail: HH22 $177.19 - 3x ATR $12.31 = $140.26 — exit when decline exceeds ~3 average daily ranges"
target_price: 192.73
target_logic: "T1 $192.73 = entry $161.25 + 1.5x R (R=$20.99); T2 $224.21 = entry + 3x R; structure ceiling = 52w high $288.45"
holding_window_days: 21
catalyst: "2027-02-01 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $175.5M; pass"
invalidation: "loses EMA20 $161.25 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-18 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
