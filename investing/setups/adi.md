---
ticker: ADI
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $388.83 ahead of the 2026-08-19 print"
entry_price: 388.83
stop_price: 386.48
stop_logic: "chandelier trail: HH22 $445.91 - 3x ATR $19.81 = $386.48 — exit when decline exceeds ~3 average daily ranges"
target_price: 392.35
target_logic: "T1 $392.35 = entry $388.83 + 1.5x R (R=$2.35); T2 $395.88 = entry + 3x R; structure ceiling = 52w high $445.91"
holding_window_days: 21
catalyst: "2026-08-19 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2382.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($19.81)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-07 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
