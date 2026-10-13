---
ticker: AEM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $185.34 ahead of the 2026-10-28 print"
entry_price: 185.34
stop_price: 186.35
stop_logic: "chandelier trail: HH22 $204.62 - 3x ATR $6.09 = $186.35 — exit when decline exceeds ~3 average daily ranges"
target_price: null
target_logic: null           # scaffold: target unavailable (needs entry>stop for R)
holding_window_days: 21
catalyst: "2026-10-28 earnings"
earnings_plan: exit_before   # machine default — change to hold_through_sized_down ONLY deliberately; sizing then uses the 25% gap assumption
liquidity_check: "avg $vol $311.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($6.09)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-13 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
