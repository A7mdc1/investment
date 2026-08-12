---
ticker: WDC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $497.06 holding the uptrend (no breakdown on volume)"
entry_price: 497.06
stop_price: 440.69
stop_logic: "chandelier trail: HH22 $589.65 - 3x ATR $49.65 = $440.69 — exit when decline exceeds ~3 average daily ranges"
target_price: 581.63
target_logic: "T1 $581.63 = entry $497.06 + 1.5x R (R=$56.38); T2 $666.19 = entry + 3x R; structure ceiling = 52w high $799.60"
holding_window_days: 21
catalyst: "2026-11-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $4065.7M; pass"
invalidation: "loses EMA20 $497.06 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
