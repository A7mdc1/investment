---
ticker: FN
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: earnings_run
entry_trigger: "enter near $458.27 ahead of the 2026-11-02 print"
entry_price: 458.27
stop_price: 410.84
stop_logic: "chandelier trail: HH22 $467.37 - 3x ATR $18.84 = $410.84 — exit when decline exceeds ~3 average daily ranges"
target_price: 529.41
target_logic: "T1 $529.41 = entry $458.27 + 1.5x R (R=$47.43); T2 $600.55 = entry + 3x R; structure ceiling = 52w high $748.81"
holding_window_days: 21
catalyst: "2026-11-02 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $297.6M; pass"
invalidation: "no positive drift 5 sessions pre-print / gives back >1 ATR ($18.84)"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-10-02 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
