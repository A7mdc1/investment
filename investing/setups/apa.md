---
ticker: APA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $44.87 ahead of the 2026-11-04 print"
entry_price: 44.87
stop_price: 42.61
stop_logic: "chandelier trail: HH22 $47.44 - 3x ATR $1.61 = $42.61 — exit when decline exceeds ~3 average daily ranges"
target_price: 48.26
target_logic: "T1 $48.26 = entry $44.87 + 1.5x R (R=$2.26); T2 $51.64 = entry + 3x R; structure ceiling = 52w high $47.43"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $243.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.61)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-20 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
