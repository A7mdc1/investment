---
ticker: FSLR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $171.86 ahead of the 2026-10-29 print"
entry_price: 171.86
stop_price: 169.11
stop_logic: "chandelier trail: HH22 $190.00 - 3x ATR $6.96 = $169.11 — exit when decline exceeds ~3 average daily ranges"
target_price: 175.98
target_logic: "T1 $175.98 = entry $171.86 + 1.5x R (R=$2.75); T2 $180.10 = entry + 3x R; structure ceiling = 52w high $321.23"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $345.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($6.96)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-23 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
