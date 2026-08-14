---
ticker: AVGO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $393.36 ahead of the 2026-09-02 print"
entry_price: 393.36
stop_price: 383.87
stop_logic: "chandelier trail: HH22 $432.73 - 3x ATR $16.29 = $383.87 — exit when decline exceeds ~3 average daily ranges"
target_price: 407.59
target_logic: "T1 $407.59 = entry $393.36 + 1.5x R (R=$9.49); T2 $421.82 = entry + 3x R; structure ceiling = 52w high $494.17"
holding_window_days: 21
catalyst: "2026-09-02 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $6908.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($16.29)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-14 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
