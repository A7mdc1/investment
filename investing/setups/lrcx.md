---
ticker: LRCX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $315.32 holding the uptrend (no breakdown on volume)"
entry_price: 315.32
stop_price: 288.77
stop_logic: "chandelier trail: HH22 $357.25 - 3x ATR $22.83 = $288.77 — exit when decline exceeds ~3 average daily ranges"
target_price: 355.15
target_logic: "T1 $355.15 = entry $315.32 + 1.5x R (R=$26.56); T2 $394.99 = entry + 3x R; structure ceiling = 52w high $438.65"
holding_window_days: 21
catalyst: "2026-10-21 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $3218.1M; pass"
invalidation: "loses EMA20 $315.32 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
