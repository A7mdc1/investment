---
ticker: PBF
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $85.59 ahead of the 2026-10-29 print"
entry_price: 85.59
stop_price: 74.96
stop_logic: "chandelier trail: HH22 $89.48 - 3x ATR $4.84 = $74.96 — exit when decline exceeds ~3 average daily ranges"
target_price: 101.55
target_logic: "T1 $101.55 = entry $85.59 + 1.5x R (R=$10.64); T2 $117.50 = entry + 3x R; structure ceiling = 52w high $89.44"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $305.4M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($4.84)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-09 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
