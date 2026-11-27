---
ticker: DIOD
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $81.59 holding the uptrend (no breakdown on volume)"
entry_price: 81.59
stop_price: 73.85
stop_logic: "chandelier trail: HH22 $94.64 - 3x ATR $6.93 = $73.85 — exit when decline exceeds ~3 average daily ranges"
target_price: 93.21
target_logic: "T1 $93.21 = entry $81.59 + 1.5x R (R=$7.74); T2 $104.82 = entry + 3x R; structure ceiling = 52w high $126.02"
holding_window_days: 21
catalyst: "2027-02-09 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $44.6M; pass"
invalidation: "loses EMA20 $81.59 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
