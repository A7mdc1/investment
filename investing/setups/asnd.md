---
ticker: ASND
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $240.91 holding the uptrend (no breakdown on volume)"
entry_price: 240.91
stop_price: 238.20
stop_logic: "chandelier trail: HH22 $255.61 - 3x ATR $5.80 = $238.20 — exit when decline exceeds ~3 average daily ranges"
target_price: 244.97
target_logic: "T1 $244.97 = entry $240.91 + 1.5x R (R=$2.71); T2 $249.03 = entry + 3x R; structure ceiling = 52w high $282.03"
holding_window_days: 21
catalyst: null
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $155.1M; pass"
invalidation: "loses EMA20 $240.91 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-02 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
