---
ticker: GWRE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $137.21 ahead of the 2026-09-03 print"
entry_price: 137.21
stop_price: 130.22
stop_logic: "chandelier trail: HH22 $152.19 - 3x ATR $7.32 = $130.22 — exit when decline exceeds ~3 average daily ranges"
target_price: 147.68
target_logic: "T1 $147.68 = entry $137.21 + 1.5x R (R=$6.98); T2 $158.16 = entry + 3x R; structure ceiling = 52w high $272.77"
holding_window_days: 21
catalyst: "2026-09-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $190.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($7.32)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-24 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
