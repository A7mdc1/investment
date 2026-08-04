---
ticker: DELL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $474.68 ahead of the 2026-09-03 print"
entry_price: 474.68
stop_price: 370.43
stop_logic: "chandelier trail: HH22 $475.50 - 3x ATR $35.02 = $370.43 — exit when decline exceeds ~3 average daily ranges"
target_price: 631.06
target_logic: "T1 $631.06 = entry $474.68 + 1.5x R (R=$104.25); T2 $787.44 = entry + 3x R; structure ceiling = 52w high $475.63"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2704.5M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($35.02)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-04 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
