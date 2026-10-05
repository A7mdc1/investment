---
ticker: LLY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $1154.26 ahead of the 2026-10-29 print"
entry_price: 1154.26
stop_price: 1127.22
stop_logic: "chandelier trail: HH22 $1215.00 - 3x ATR $29.26 = $1127.22 — exit when decline exceeds ~3 average daily ranges"
target_price: 1194.82
target_logic: "T1 $1194.82 = entry $1154.26 + 1.5x R (R=$27.04); T2 $1235.37 = entry + 3x R; structure ceiling = 52w high $1292.56"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2518.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($29.26)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-05 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
