---
ticker: AR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $34.68 ahead of the 2026-07-29 print"
entry_price: 34.68
stop_price: 34.12
stop_logic: "chandelier trail: HH22 $37.20 - 3x ATR $1.03 = $34.12 — exit when decline exceeds ~3 average daily ranges"
target_price: 35.52
target_logic: "T1 $35.52 = entry $34.68 + 1.5x R (R=$0.56); T2 $36.36 = entry + 3x R; structure ceiling = 52w high $45.75"
holding_window_days: 21
catalyst: "2026-07-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $173.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.03)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
