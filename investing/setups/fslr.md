---
ticker: FSLR
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $174.43 ahead of the 2026-10-29 print"
entry_price: 174.43
stop_price: 168.68
stop_logic: "chandelier trail: HH22 $187.85 - 3x ATR $6.39 = $168.68 — exit when decline exceeds ~3 average daily ranges"
target_price: 183.04
target_logic: "T1 $183.04 = entry $174.43 + 1.5x R (R=$5.74); T2 $191.65 = entry + 3x R; structure ceiling = 52w high $321.22"
holding_window_days: 21
catalyst: "2026-10-29 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $343.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($6.39)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-28 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
