---
ticker: AMKR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $52.67 ahead of the 2026-10-26 print"
entry_price: 52.67
stop_price: 48.11
stop_logic: "chandelier trail: HH22 $55.13 - 3x ATR $2.34 = $48.11 — exit when decline exceeds ~3 average daily ranges"
target_price: 59.51
target_logic: "T1 $59.51 = entry $52.67 + 1.5x R (R=$4.56); T2 $66.35 = entry + 3x R; structure ceiling = 52w high $96.47"
holding_window_days: 21
catalyst: "2026-10-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $186.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.34)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-30 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
