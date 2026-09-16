---
ticker: DDS
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $652.02 ahead of the 2026-11-12 print"
entry_price: 652.02
stop_price: 597.99
stop_logic: "chandelier trail: HH22 $665.25 - 3x ATR $22.42 = $597.99 — exit when decline exceeds ~3 average daily ranges"
target_price: 733.07
target_logic: "T1 $733.07 = entry $652.02 + 1.5x R (R=$54.03); T2 $814.12 = entry + 3x R; structure ceiling = 52w high $710.26"
holding_window_days: 21
catalyst: "2026-11-12 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $101.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($22.42)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-16 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
