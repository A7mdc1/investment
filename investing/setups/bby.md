---
ticker: BBY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $88.39 ahead of the 2026-11-24 print"
entry_price: 88.39
stop_price: 88.13
stop_logic: "chandelier trail: HH22 $96.53 - 3x ATR $2.80 = $88.13 — exit when decline exceeds ~3 average daily ranges"
target_price: 88.77
target_logic: "T1 $88.77 = entry $88.39 + 1.5x R (R=$0.26); T2 $89.16 = entry + 3x R; structure ceiling = 52w high $96.50"
holding_window_days: 21
catalyst: "2026-11-24 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $280.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.80)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
