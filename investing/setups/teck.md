---
ticker: TECK
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $67.35 ahead of the 2026-10-29 print"
entry_price: 67.35
stop_price: 65.32
stop_logic: "chandelier trail: HH22 $72.46 - 3x ATR $2.38 = $65.32 — exit when decline exceeds ~3 average daily ranges"
target_price: 70.39
target_logic: "T1 $70.39 = entry $67.35 + 1.5x R (R=$2.03); T2 $73.43 = entry + 3x R; structure ceiling = 52w high $72.50"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $187.5M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.38)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
