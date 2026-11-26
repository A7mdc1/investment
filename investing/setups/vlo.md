---
ticker: VLO
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $356.88 holding the uptrend (no breakdown on volume)"
entry_price: 356.88
stop_price: 370.91
stop_logic: "chandelier trail: HH22 $421.72 - 3x ATR $16.94 = $370.91 — exit when decline exceeds ~3 average daily ranges"
target_price: null
target_logic: null           # scaffold: target unavailable (needs entry>stop for R)
holding_window_days: 21
catalyst: "2027-01-28 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $1106.7M; pass"
invalidation: "loses EMA20 $356.88 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-26 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
