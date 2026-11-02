---
ticker: NXT
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $81.88 holding the uptrend (no breakdown on volume)"
entry_price: 81.88
stop_price: 78.17
stop_logic: "chandelier trail: HH22 $92.98 - 3x ATR $4.94 = $78.17 — exit when decline exceeds ~3 average daily ranges"
target_price: 87.44
target_logic: "T1 $87.44 = entry $81.88 + 1.5x R (R=$3.71); T2 $93.01 = entry + 3x R; structure ceiling = 52w high $163.02"
holding_window_days: 21
catalyst: "2027-01-27 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $191.5M; pass"
invalidation: "loses EMA20 $81.88 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-02 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
