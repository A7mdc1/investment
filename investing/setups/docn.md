---
ticker: DOCN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $126.72 holding the uptrend (no breakdown on volume)"
entry_price: 126.72
stop_price: 108.03
stop_logic: "chandelier trail: HH22 $144.52 - 3x ATR $12.16 = $108.03 — exit when decline exceeds ~3 average daily ranges"
target_price: 154.74
target_logic: "T1 $154.74 = entry $126.72 + 1.5x R (R=$18.68); T2 $182.77 = entry + 3x R; structure ceiling = 52w high $187.62"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $431.1M; pass"
invalidation: "loses EMA20 $126.72 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-12 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
