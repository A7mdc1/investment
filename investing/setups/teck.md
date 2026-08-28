---
ticker: TECK
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $69.06 ahead of the 2026-10-22 print"
entry_price: 69.06
stop_price: 65.27
stop_logic: "chandelier trail: HH22 $71.93 - 3x ATR $2.22 = $65.27 — exit when decline exceeds ~3 average daily ranges"
target_price: 74.75
target_logic: "T1 $74.75 = entry $69.06 + 1.5x R (R=$3.79); T2 $80.44 = entry + 3x R; structure ceiling = 52w high $71.94"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $189.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.22)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-28 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
