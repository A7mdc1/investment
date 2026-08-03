---
ticker: NVDA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $207.11 ahead of the 2026-08-26 print"
entry_price: 207.11
stop_price: 191.36
stop_logic: "chandelier trail: HH22 $214.39 - 3x ATR $7.68 = $191.36 — exit when decline exceeds ~3 average daily ranges"
target_price: 230.74
target_logic: "T1 $230.74 = entry $207.11 + 1.5x R (R=$15.75); T2 $254.37 = entry + 3x R; structure ceiling = 52w high $236.16"
holding_window_days: 21
catalyst: "2026-08-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $25689.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($7.68)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-03 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
