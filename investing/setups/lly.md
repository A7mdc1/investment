---
ticker: LLY
status: draft            # machine-filled by scaffold.py, UNREVIEWED — review & set planned to approve
setup_type: pullback
entry_trigger: "pullback to EMA20 $1375.19 holding the uptrend (no breakdown on volume)"
entry_price: 1375.19
stop_price: 1334.49
stop_logic: "chandelier trail: HH22 $1475.25 - 3x ATR $46.92 = $1334.49 — exit when decline exceeds ~3 average daily ranges"
target_price: 1436.23
target_logic: "T1 $1436.23 = entry $1375.19 + 1.5x R (R=$40.70); T2 $1497.28 = entry + 3x R; structure ceiling = 52w high $1474.89"
holding_window_days: 21
catalyst: "2027-02-03 earnings"
earnings_plan: no_earnings_in_window
liquidity_check: "avg $vol $4404.6M; pass"
invalidation: "loses EMA20 $1375.19 on rising volume"
shariah:
  status: unverified     # ALWAYS unverified from the scaffold — only a human Zoya/Musaffa screen sets compliant
  source: null
  screened: null         # pre-check: business OK, ratios OK — verify in Zoya/Musaffa
---

## Notes
Scaffolded 2026-11-27 from Yahoo data — every level is a formula output. Edit anything
you disagree with, then set status: planned to approve. Shariah is UNVERIFIED until
you screen it in Zoya/Musaffa and record the result above.
