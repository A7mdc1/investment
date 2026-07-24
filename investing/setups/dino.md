---
ticker: DINO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $89.30 ahead of the 2026-07-28 print"
entry_price: 89.30
stop_price: 85.11
stop_logic: "chandelier trail: HH22 $93.66 - 3x ATR $2.85 = $85.11 — exit when decline exceeds ~3 average daily ranges"
target_price: 95.58
target_logic: "T1 $95.58 = entry $89.30 + 1.5x R (R=$4.19); T2 $101.86 = entry + 3x R; structure ceiling = 52w high $93.70"
holding_window_days: 21
catalyst: "2026-07-28 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $211.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($2.85)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-07-24 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
