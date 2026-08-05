---
ticker: WDC
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $548.52 ahead of the 2026-08-05 print"
entry_price: 548.52
stop_price: 454.94
stop_logic: "chandelier trail: HH22 $601.50 - 3x ATR $48.85 = $454.94 — exit when decline exceeds ~3 average daily ranges"
target_price: 688.89
target_logic: "T1 $688.89 = entry $548.52 + 1.5x R (R=$93.58); T2 $829.25 = entry + 3x R; structure ceiling = 52w high $799.59"
holding_window_days: 21
catalyst: "2026-08-05 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $3741.2M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($48.85)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-05 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
