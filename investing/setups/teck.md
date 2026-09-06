---
ticker: TECK
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $69.10 ahead of the 2026-10-22 print"
entry_price: 69.10
stop_price: 66.06
stop_logic: "chandelier trail: HH22 $71.93 - 3x ATR $1.96 = $66.06 — exit when decline exceeds ~3 average daily ranges"
target_price: 73.65
target_logic: "T1 $73.65 = entry $69.10 + 1.5x R (R=$3.03); T2 $78.20 = entry + 3x R; structure ceiling = 52w high $71.90"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $186.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.96)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
