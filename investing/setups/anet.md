---
ticker: ANET
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $181.22 holding the uptrend (no breakdown on volume)"
entry_price: 181.22
stop_price: 171.06
stop_logic: "chandelier trail: HH22 $212.16 - 3x ATR $13.70 = $171.06 — exit when decline exceeds ~3 average daily ranges"
target_price: 196.46
target_logic: "T1 $196.46 = entry $181.22 + 1.5x R (R=$10.16); T2 $211.70 = entry + 3x R; structure ceiling = 52w high $217.49"
holding_window_days: 21
catalyst: "2027-02-09 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1724.8M; pass"
invalidation: "loses EMA20 $181.22 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-26 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
