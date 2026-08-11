---
ticker: KEYS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $342.10 ahead of the 2026-08-18 print"
entry_price: 342.10
stop_price: 305.93
stop_logic: "chandelier trail: HH22 $345.36 - 3x ATR $13.14 = $305.93 — exit when decline exceeds ~3 average daily ranges"
target_price: 396.36
target_logic: "T1 $396.36 = entry $342.10 + 1.5x R (R=$36.17); T2 $450.62 = entry + 3x R; structure ceiling = 52w high $375.11"
holding_window_days: 21
catalyst: "2026-08-18 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $362.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($13.14)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-11 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
