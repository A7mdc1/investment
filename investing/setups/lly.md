---
ticker: LLY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $1174.61 ahead of the 2026-10-29 print"
entry_price: 1174.61
stop_price: 1165.29
stop_logic: "chandelier trail: HH22 $1292.65 - 3x ATR $42.45 = $1165.29 — exit when decline exceeds ~3 average daily ranges"
target_price: 1188.59
target_logic: "T1 $1188.59 = entry $1174.61 + 1.5x R (R=$9.32); T2 $1202.58 = entry + 3x R; structure ceiling = 52w high $1292.20"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $3416.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($42.45)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-30 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
