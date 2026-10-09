---
ticker: SMTC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $187.59 ahead of the 2026-11-23 print"
entry_price: 187.59
stop_price: 167.17
stop_logic: "chandelier trail: HH22 $201.99 - 3x ATR $11.61 = $167.17 — exit when decline exceeds ~3 average daily ranges"
target_price: 218.22
target_logic: "T1 $218.22 = entry $187.59 + 1.5x R (R=$20.42); T2 $248.86 = entry + 3x R; structure ceiling = 52w high $201.93"
holding_window_days: 21
catalyst: "2026-11-23 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $590.3M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($11.61)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-09 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
