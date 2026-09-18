---
ticker: XOM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $162.64 ahead of the 2026-10-30 print"
entry_price: 162.64
stop_price: 158.96
stop_logic: "chandelier trail: HH22 $169.64 - 3x ATR $3.56 = $158.96 — exit when decline exceeds ~3 average daily ranges"
target_price: 168.16
target_logic: "T1 $168.16 = entry $162.64 + 1.5x R (R=$3.68); T2 $173.67 = entry + 3x R; structure ceiling = 52w high $174.13"
holding_window_days: 21
catalyst: "2026-10-30 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2152.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($3.56)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-18 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
