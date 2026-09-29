---
ticker: XOM
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $161.46 ahead of the 2026-10-30 print"
entry_price: 161.46
stop_price: 158.46
stop_logic: "chandelier trail: HH22 $169.64 - 3x ATR $3.73 = $158.46 — exit when decline exceeds ~3 average daily ranges"
target_price: 165.95
target_logic: "T1 $165.95 = entry $161.46 + 1.5x R (R=$2.99); T2 $170.44 = entry + 3x R; structure ceiling = 52w high $174.17"
holding_window_days: 21
catalyst: "2026-10-30 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $2255.7M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($3.73)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-09-29 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
