---
ticker: LLY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $1276.66 ahead of the 2026-10-29 print"
entry_price: 1276.66
stop_price: 1209.66
stop_logic: "chandelier trail: HH22 $1321.21 - 3x ATR $37.18 = $1209.66 — exit when decline exceeds ~3 average daily ranges"
target_price: 1377.16
target_logic: "T1 $1377.16 = entry $1276.66 + 1.5x R (R=$67.00); T2 $1477.67 = entry + 3x R; structure ceiling = 52w high $1321.59"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $2712.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($37.18)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
