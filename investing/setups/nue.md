---
ticker: NUE
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $252.36 ahead of the 2026-10-26 print"
entry_price: 252.36
stop_price: 245.97
stop_logic: "chandelier trail: HH22 $267.44 - 3x ATR $7.16 = $245.97 — exit when decline exceeds ~3 average daily ranges"
target_price: 261.95
target_logic: "T1 $261.95 = entry $252.36 + 1.5x R (R=$6.39); T2 $271.54 = entry + 3x R; structure ceiling = 52w high $279.47"
holding_window_days: 21
catalyst: "2026-10-26 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $310.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($7.16)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
