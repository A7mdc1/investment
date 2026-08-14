---
ticker: LRCX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $315.94 holding the uptrend (no breakdown on volume)"
entry_price: 315.94
stop_price: 279.52
stop_logic: "chandelier trail: HH22 $345.12 - 3x ATR $21.87 = $279.52 — exit when decline exceeds ~3 average daily ranges"
target_price: 370.57
target_logic: "T1 $370.57 = entry $315.94 + 1.5x R (R=$36.42); T2 $425.20 = entry + 3x R; structure ceiling = 52w high $438.60"
holding_window_days: 21
catalyst: "2026-10-21 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $3162.8M; pass"
invalidation: "loses EMA20 $315.94 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
