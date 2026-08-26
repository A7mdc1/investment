---
ticker: CRH
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $97.25 holding the uptrend (no breakdown on volume)"
entry_price: 97.25
stop_price: 95.50
stop_logic: "chandelier trail: HH22 $103.86 - 3x ATR $2.79 = $95.50 — exit when decline exceeds ~3 average daily ranges"
target_price: 99.88
target_logic: "T1 $99.88 = entry $97.25 + 1.5x R (R=$1.75); T2 $102.50 = entry + 3x R; structure ceiling = 52w high $130.03"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $433.4M; pass"
invalidation: "loses EMA20 $97.25 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-26 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
