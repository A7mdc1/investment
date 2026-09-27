---
ticker: XOM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $160.59 ahead of the 2026-10-30 print"
entry_price: 160.59
stop_price: 158.57
stop_logic: "chandelier trail: HH22 $169.64 - 3x ATR $3.69 = $158.57 — exit when decline exceeds ~3 average daily ranges"
target_price: 163.62
target_logic: "T1 $163.62 = entry $160.59 + 1.5x R (R=$2.02); T2 $166.66 = entry + 3x R; structure ceiling = 52w high $174.18"
holding_window_days: 21
catalyst: "2026-10-30 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2359.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($3.69)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
