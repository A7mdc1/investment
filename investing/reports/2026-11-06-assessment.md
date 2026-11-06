# Portfolio Assessment — 2026-11-06

Not financial advice. Decision support only — every buy/sell/hold call is yours.
Shariah status below is a recorded broker-app screen or a mechanical pre-check,
neither a fatwa — verify in Zoya/Musaffa before acting.

## What ran
`discover.py` (live Yahoo, top 50 leads) → `scaffold.py --all-leads` (23 new DRAFT
cards; existing cards unchanged) → `prices / shariah / dcf / signals / verdict /
recommend` — all live, no data gaps. Per-holding web catalyst research was **not**
done in this unattended run (no catalyst facts are asserted below). `journal.py`
not run (no `transactions.csv`).

## Verdicts (your rules resolving, not advice)
| Ticker | Verdict | Rule | Price | Return | Weight | Trailing stop | 6m mom |
|---|---|---|---|---|---|---|---|
| BMNR | HOLD | DEFAULT | $18.80 | +21.8% vs $15.43 | 20.7% | $20.12 (**price is below it**) | +8.4% |
| NOW | HOLD | VALUATION_RICH (P/E ~119 ≥ 50 — hold, don't add) | $102.70 | −10.7% vs $114.97 | 79.3% | $136.54 (**price is below it**) | +53.3% |

Portfolio: $906.88 total; 2 holdings so concentration rules are muted. Vol throttle:
BMNR ATR 7.9%, NOW ATR 7.5% — size down.

PM-grade records (mechanical proxies, not a conviction call): both **LOW** conviction
(no reward:risk / stated edge). BMNR target = DCF $0.72 (−96%; DCF doesn't fit a
crypto-treasury business). NOW DCF $119.65 vs $102.70 (+16.5%; growth 18%, terminal
3%, discount 10%). NOW 52w-range position: 14th percentile.

## Action flags (priority order)
1. **Shariah — both screens stale (>100d).** BMNR screened 2026-07-07, NOW 2026-06-09. Re-screen both.
2. **BMNR ratio pre-check still FAILS** — industry "Capital Markets" fails the business screen, contradicting the recorded "compliant". Unresolved since the 2026-08-19 report; `recommend.py` reads only the recorded field. A Zoya/Musaffa re-screen decides it. Compliance is a gate, so do not add until resolved.
3. **Both holdings trade below their chandelier trailing stop** (BMNR $20.12, NOW $136.54) yet verdict.py returns HOLD — no SELL rule fired on it. NOW is ~25% under its trail with a 6m momentum of +53%; check whether the trail input is stale/mis-anchored vs. your intent.
4. NOW valuation rich (P/E ~119) — "hold, do not add" per your rule.

## Case to keep vs. trim (no pick made)
- **BMNR** — keep: +21.8% gain, positive 6m momentum, no rule fired. Trim/exit: below trail, Shariah conflict unresolved, DCF unusable, no stated thesis.
- **NOW** — keep: DCF +16.5% above price, strong 6m momentum, recorded compliant. Trim: −10.7% vs cost, below trail, P/E ~119, 79% of the account, thesis lacks variant view/invalidation/target.

## New ideas
`recommend.py` ideas array is empty: no planned/compliant card exists, so there are **no BUY-CANDIDATEs**. All 50 leads are LEAD/RESEARCH. Shariah UNVERIFIED for all.
Highest discovery reward:risk (formula estimates, not promises): KGC 15.3:1, EVR 9.7:1, TECK 9.5:1, PNFP 6.8:1, FSLR 6.4:1, AGI 5.4:1. Near-term dated catalysts: LIF/ASTS earnings 11-09, DLO 11-12, NVDA 11-17, KLIC/P 11-18, KEYS 11-19, FRO 11-20, DELL/ADI/BBY/NTNX 11-24.
Caution: several discovery rows show stop > entry (e.g. DELL, NET, MU, CIEN) — formula artifacts; treat those levels as unusable until reviewed.

## Draft setups
23 new DRAFT cards (RESEARCH — DRAFT awaiting your review; set `status: planned` to approve): ACGL, AEM, ANET, ASML, ASND, BBY, BF-B, EVR, FRO, FSLR, HSY, KEYS, NTAP, NTNX, PNFP, PSX, SMTC, SNA, SOLV, TECK, TRV, TXN, VLO. Every level is a formula output; example TXN: pullback to $291.22, stop $282.20, T1 $304.75 (1.5R), earnings 2027-01-26 outside window. Shariah is `unverified` on all.

## Follow-ups
1. Re-screen BMNR and NOW in Zoya/Musaffa (BMNR first).
2. Decide on BMNR/NOW vs. trailing stops; fill thesis/invalidation/target fields.
3. Review drafts for names you care about; fix stop>entry artifacts.
4. If you trade, run /apply-trade.

Not financial advice; verify compliance in Zoya/Musaffa.
