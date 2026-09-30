---
ticker: BBY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $87.85 ahead of the 2026-11-24 print"
entry_price: 87.85
stop_price: 87.27
stop_logic: "chandelier trail: HH22 $96.53 - 3x ATR $3.09 = $87.27 — exit when decline exceeds ~3 average daily ranges"
target_price: 88.72
target_logic: "T1 $88.72 = entry $87.85 + 1.5x R (R=$0.58); T2 $89.60 = entry + 3x R; structure ceiling = 52w high $96.54"
holding_window_days: 21
catalyst: "2026-11-24 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $318.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($3.09)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-30 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
