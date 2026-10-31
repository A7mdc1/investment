---
ticker: APA
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $52.82 ahead of the 2026-11-04 print"
entry_price: 52.82
stop_price: 48.20
stop_logic: "chandelier trail: HH22 $52.96 - 3x ATR $1.59 = $48.20 — exit when decline exceeds ~3 average daily ranges"
target_price: 59.75
target_logic: "T1 $59.75 = entry $52.82 + 1.5x R (R=$4.62); T2 $66.69 = entry + 3x R; structure ceiling = 52w high $52.98"
holding_window_days: 21
catalyst: "2026-11-04 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $245.1M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($1.59)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-31 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
