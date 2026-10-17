---
ticker: LLY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $1257.03 ahead of the 2026-10-29 print"
entry_price: 1257.03
stop_price: 1169.75
stop_logic: "chandelier trail: HH22 $1275.88 - 3x ATR $35.38 = $1169.75 — exit when decline exceeds ~3 average daily ranges"
target_price: 1387.95
target_logic: "T1 $1387.95 = entry $1257.03 + 1.5x R (R=$87.28); T2 $1518.87 = entry + 3x R; structure ceiling = 52w high $1293.24"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $2717.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($35.38)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-17 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
