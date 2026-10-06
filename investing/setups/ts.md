---
ticker: TS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $57.02 ahead of the 2026-11-04 print"
entry_price: 57.02
stop_price: 54.64
stop_logic: "chandelier trail: HH22 $58.74 - 3x ATR $1.37 = $54.64 — exit when decline exceeds ~3 average daily ranges"
target_price: 60.59
target_logic: "T1 $60.59 = entry $57.02 + 1.5x R (R=$2.38); T2 $64.16 = entry + 3x R; structure ceiling = 52w high $64.58"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $65.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.37)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
