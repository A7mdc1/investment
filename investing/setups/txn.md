---
ticker: TXN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $281.85 ahead of the 2027-01-26 print"
entry_price: 281.85
stop_price: 265.45
stop_logic: "chandelier trail: HH22 $317.20 - 3x ATR $17.25 = $265.45 — exit when decline exceeds ~3 average daily ranges"
target_price: 306.45
target_logic: "T1 $306.45 = entry $281.85 + 1.5x R (R=$16.40); T2 $331.04 = entry + 3x R; structure ceiling = 52w high $330.81"
holding_window_days: 21
catalyst: "2027-01-26 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2791.9M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($17.25)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-28 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
