---
ticker: DIOD
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $84.88 holding the uptrend (no breakdown on volume)"
entry_price: 84.88
stop_price: 76.41
stop_logic: "chandelier trail: HH22 $94.64 - 3x ATR $6.08 = $76.41 — exit when decline exceeds ~3 average daily ranges"
target_price: 97.59
target_logic: "T1 $97.59 = entry $84.88 + 1.5x R (R=$8.47); T2 $110.31 = entry + 3x R; structure ceiling = 52w high $125.90"
holding_window_days: 21
catalyst: "2027-02-09 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $43.1M; pass"
invalidation: "loses EMA20 $84.88 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
