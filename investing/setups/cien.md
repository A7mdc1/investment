---
ticker: CIEN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $418.39 ahead of the 2026-09-09 print"
entry_price: 418.39
stop_price: 396.66
stop_logic: "chandelier trail: HH22 $485.69 - 3x ATR $29.68 = $396.66 — exit when decline exceeds ~3 average daily ranges"
target_price: 450.99
target_logic: "T1 $450.99 = entry $418.39 + 1.5x R (R=$21.73); T2 $483.59 = entry + 3x R; structure ceiling = 52w high $637.79"
holding_window_days: 21
catalyst: "2026-09-09 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $769.8M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($29.68)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-04 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
