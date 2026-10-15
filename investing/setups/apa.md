---
ticker: APA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $47.31 ahead of the 2026-11-04 print"
entry_price: 47.31
stop_price: 44.05
stop_logic: "chandelier trail: HH22 $48.60 - 3x ATR $1.52 = $44.05 — exit when decline exceeds ~3 average daily ranges"
target_price: 52.20
target_logic: "T1 $52.20 = entry $47.31 + 1.5x R (R=$3.26); T2 $57.08 = entry + 3x R; structure ceiling = 52w high $48.62"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $245.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.52)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-15 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
