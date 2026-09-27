---
ticker: SMTC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $182.30 ahead of the 2026-11-23 print"
entry_price: 182.30
stop_price: 156.18
stop_logic: "chandelier trail: HH22 $190.64 - 3x ATR $11.49 = $156.18 — exit when decline exceeds ~3 average daily ranges"
target_price: 221.48
target_logic: "T1 $221.48 = entry $182.30 + 1.5x R (R=$26.12); T2 $260.66 = entry + 3x R; structure ceiling = 52w high $190.69"
holding_window_days: 21
catalyst: "2026-11-23 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $531.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($11.49)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
