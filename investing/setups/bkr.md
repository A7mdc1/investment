---
ticker: BKR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $62.41 ahead of the 2026-10-22 print"
entry_price: 62.41
stop_price: 60.86
stop_logic: "chandelier trail: HH22 $65.44 - 3x ATR $1.53 = $60.86 — exit when decline exceeds ~3 average daily ranges"
target_price: 64.73
target_logic: "T1 $64.73 = entry $62.41 + 1.5x R (R=$1.55); T2 $67.06 = entry + 3x R; structure ceiling = 52w high $69.89"
holding_window_days: 21
catalyst: "2026-10-22 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $388.5M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.53)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-30 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
