---
ticker: JBL
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $289.55 ahead of the 2026-12-16 print"
entry_price: 289.55
stop_price: 286.49
stop_logic: "chandelier trail: HH22 $328.00 - 3x ATR $13.84 = $286.49 — exit when decline exceeds ~3 average daily ranges"
target_price: 294.12
target_logic: "T1 $294.12 = entry $289.55 + 1.5x R (R=$3.05); T2 $298.70 = entry + 3x R; structure ceiling = 52w high $428.96"
holding_window_days: 21
catalyst: "2026-12-16 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $359.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($13.84)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-29 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
