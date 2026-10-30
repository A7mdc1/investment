---
ticker: BBY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $94.95 ahead of the 2026-11-24 print"
entry_price: 94.95
stop_price: 91.16
stop_logic: "chandelier trail: HH22 $100.58 - 3x ATR $3.14 = $91.16 — exit when decline exceeds ~3 average daily ranges"
target_price: 100.64
target_logic: "T1 $100.64 = entry $94.95 + 1.5x R (R=$3.79); T2 $106.32 = entry + 3x R; structure ceiling = 52w high $100.58"
holding_window_days: 21
catalyst: "2026-11-24 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $257.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($3.14)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-30 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
