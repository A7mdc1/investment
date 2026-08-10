---
ticker: UTHR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $529.41 holding the uptrend (no breakdown on volume)"
entry_price: 529.41
stop_price: 512.69
stop_logic: "chandelier trail: HH22 $553.47 - 3x ATR $13.59 = $512.69 — exit when decline exceeds ~3 average daily ranges"
target_price: 554.50
target_logic: "T1 $554.50 = entry $529.41 + 1.5x R (R=$16.72); T2 $579.58 = entry + 3x R; structure ceiling = 52w high $609.48"
holding_window_days: 21
catalyst: "2026-10-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $262.4M; pass"
invalidation: "loses EMA20 $529.41 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-10 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
