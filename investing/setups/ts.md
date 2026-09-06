---
ticker: TS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $56.45 ahead of the 2026-11-04 print"
entry_price: 56.45
stop_price: 52.97
stop_logic: "chandelier trail: HH22 $56.86 - 3x ATR $1.30 = $52.97 — exit when decline exceeds ~3 average daily ranges"
target_price: 61.68
target_logic: "T1 $61.68 = entry $56.45 + 1.5x R (R=$3.48); T2 $66.90 = entry + 3x R; structure ceiling = 52w high $64.59"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $80.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.30)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
