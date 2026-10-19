---
ticker: AEM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $187.32 ahead of the 2026-10-28 print"
entry_price: 187.32
stop_price: 185.99
stop_logic: "chandelier trail: HH22 $204.62 - 3x ATR $6.21 = $185.99 — exit when decline exceeds ~3 average daily ranges"
target_price: 189.31
target_logic: "T1 $189.31 = entry $187.32 + 1.5x R (R=$1.33); T2 $191.30 = entry + 3x R; structure ceiling = 52w high $254.17"
holding_window_days: 21
catalyst: "2026-10-28 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $322.0M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($6.21)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-19 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
