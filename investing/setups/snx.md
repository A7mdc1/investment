---
ticker: SNX
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $260.06 ahead of the 2026-09-24 print"
entry_price: 260.06
stop_price: 242.31
stop_logic: "chandelier trail: HH22 $269.01 - 3x ATR $8.90 = $242.31 — exit when decline exceeds ~3 average daily ranges"
target_price: 286.69
target_logic: "T1 $286.69 = entry $260.06 + 1.5x R (R=$17.75); T2 $313.32 = entry + 3x R; structure ceiling = 52w high $295.86"
holding_window_days: 21
catalyst: "2026-09-24 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $171.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($8.90)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-08-06 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
