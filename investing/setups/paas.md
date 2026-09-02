---
ticker: PAAS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $50.37 holding the uptrend (no breakdown on volume)"
entry_price: 50.37
stop_price: 48.00
stop_logic: "chandelier trail: HH22 $54.99 - 3x ATR $2.33 = $48.00 — exit when decline exceeds ~3 average daily ranges"
target_price: 53.91
target_logic: "T1 $53.91 = entry $50.37 + 1.5x R (R=$2.36); T2 $57.46 = entry + 3x R; structure ceiling = 52w high $69.37"
holding_window_days: 21
catalyst: "2026-11-16 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $268.1M; pass"
invalidation: "loses EMA20 $50.37 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-02 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
