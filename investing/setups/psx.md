---
ticker: PSX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $177.19 ahead of the 2026-08-05 print"
entry_price: 177.19
stop_price: 172.06
stop_logic: "chandelier trail: HH22 $188.00 - 3x ATR $5.31 = $172.06 — exit when decline exceeds ~3 average daily ranges"
target_price: 184.89
target_logic: "T1 $184.89 = entry $177.19 + 1.5x R (R=$5.13); T2 $192.59 = entry + 3x R; structure ceiling = 52w high $189.31"
holding_window_days: 21
catalyst: "2026-08-05 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $474.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($5.31)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
