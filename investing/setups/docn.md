---
ticker: DOCN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $127.65 holding the uptrend (no breakdown on volume)"
entry_price: 127.65
stop_price: 108.71
stop_logic: "chandelier trail: HH22 $144.52 - 3x ATR $11.94 = $108.71 — exit when decline exceeds ~3 average daily ranges"
target_price: 156.05
target_logic: "T1 $156.05 = entry $127.65 + 1.5x R (R=$18.93); T2 $184.44 = entry + 3x R; structure ceiling = 52w high $187.58"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $426.2M; pass"
invalidation: "loses EMA20 $127.65 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
