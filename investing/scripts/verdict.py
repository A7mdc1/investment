"""verdict.py — resolve each holding to ONE verb from rules.md (your policy).

Precedence: SELL > TRIM > REVIEW > HOLD. Thresholds come from the YAML block at
the top of rules.md, so you tune policy in one place. Technical rules (chandelier
trail, EMA break, momentum stop) use live history via technicals.py and skip
gracefully if no data. The engine never trades and gives no advice — it reports
which of YOUR rules match current data.
"""
from __future__ import annotations
import datetime as dt
import json
import os
import sys
import yaml
from common import load_holdings
import technicals

RULES = os.path.join(os.path.dirname(__file__), "..", "rules.md")
RANK = {"SELL": 3, "TRIM": 2, "REVIEW": 1, "HOLD": 0}


def load_cfg() -> dict:
    txt = open(RULES, encoding="utf-8").read()
    if txt.startswith("---"):
        return yaml.safe_load(txt.split("---", 2)[1]) or {}
    return {}


def price_of(t, fallback):
    try:
        import yfinance as yf
        p = yf.Ticker(t).fast_info.get("lastPrice")
        if p:
            return float(p)
    except Exception as e:
        print(f"[warn] price {t}: {e}", file=sys.stderr)
    return fallback


def compute(cfg=None, hs=None) -> dict:
    """Resolve every holding's verb + drivers. Returns the same dict main() prints."""
    if cfg is None:
        cfg = load_cfg()
    if hs is None:
        hs = load_holdings()
    small = len(hs) < int(cfg.get("min_names_for_concentration", 4))

    vals = []
    total = 0.0
    for h in hs:
        m = h["meta"]
        px = price_of(m["ticker"], m.get("last_price"))
        vv = (px * (m.get("shares", 0) or 0)) if px else 0
        total += vv
        vals.append((m, px, vv))

    out, portfolio_notes = [], []
    for m, px, vv in vals:
        weight = (vv / total) if total else 0
        cb = m.get("cost_basis")
        ttype = m.get("trade_type", "core")
        status = (m.get("shariah") or {}).get("status", "unknown")
        tech = technicals.fetch(m["ticker"], cfg)
        fired = []

        # Stage 1: compliance gate
        if status == "non-compliant":
            fired.append(("SELL", "COMPLIANCE_GATE", "off-mandate; exit (verify Zoya/Musaffa)"))
        if status in ("unknown", "doubtful"):
            fired.append(("REVIEW", "COMPLIANCE_SCREEN", f"status '{status}' — screen before add"))

        # Stage 4: hard / technical sell triggers
        stop = m.get("initial_stop")
        if px and stop and px < stop:
            fired.append(("SELL", "HARD_STOP", f"price {px:g} < initial stop {stop:g}"))
        if m.get("thesis_broken"):
            fired.append(("SELL", "THESIS_BREAK", "thesis invalidated"))
        if tech and px:
            if ttype in ("swing", "momentum", "catalyst") and px < tech["chandelier_stop"]:
                fired.append(("SELL", "TRAIL_STOP",
                              f"price {px:g} < chandelier {tech['chandelier_stop']:g}"))
            if ttype == "momentum" and tech["bom_drop_pct"] is not None \
                    and tech["bom_drop_pct"] <= -float(cfg.get("momentum_stop_bom_pct", 15)):
                fired.append(("SELL", "MOMENTUM_STOP",
                              f"down {tech['bom_drop_pct']:.1f}% from month-open"))
            if ttype in ("swing", "momentum") and px < tech["ema_slow"]:
                fired.append(("SELL", "EMA_BREAK", f"close < EMA{cfg.get('ema_slow',50)}"))
            elif ttype in ("swing", "momentum") and px < tech["ema_fast"]:
                fired.append(("REVIEW", "EMA_FADE", f"close < EMA{cfg.get('ema_fast',20)} (early)"))
            if tech["atr_pct"] and tech["atr_pct"] >= float(cfg.get("vol_throttle_atr_pct", 6)):
                portfolio_notes.append(f"{m['ticker']} ATR {tech['atr_pct']}% — size down per vol throttle")

        # Stage 3: trim / hold
        r_mult = None
        if px and cb and stop and (cb - stop) != 0:
            r_mult = (px - cb) / abs(cb - stop)
            if r_mult >= float(cfg.get("take_profit_r", 1.5)) and not m.get("trimmed"):
                fired.append(("TRIM", "TAKE_PARTIAL",
                              f"+{r_mult:.1f}R — trim, move stop to breakeven"))
        if not small and weight * 100 > float(cfg.get("max_position_pct", 22)):
            fired.append(("TRIM", "CONCENTRATION",
                          f"{weight:.0%} > {cfg.get('max_position_pct',22)}% cap"))
        pe = m.get("pe")
        if pe and pe >= float(cfg.get("pe_rich", 50)):
            fired.append(("HOLD", "VALUATION_RICH", f"P/E ~{pe:g} — hold, do not add"))

        dd = ((px - cb) / cb) if (px and cb) else None
        if dd is not None and dd <= -float(cfg.get("drawdown_review_pct", 20)) / 100:
            fired.append(("REVIEW", "DRAWDOWN_REVIEW", f"down {dd:.0%} vs cost"))

        verb = max((f[0] for f in fired), key=lambda x: RANK[x], default="HOLD")
        out.append({
            "ticker": m["ticker"], "name": m.get("name"), "trade_type": ttype,
            "verdict": verb, "price": px, "weight_pct": round(weight * 100, 1),
            "return_pct": round(dd * 100, 1) if dd is not None else None,
            "r_multiple": round(r_mult, 2) if r_mult is not None else None,
            "trailing_stop": tech["chandelier_stop"] if tech else None,
            "ema_fast": tech["ema_fast"] if tech else None,
            "mom_6_1_pct": round(tech["mom_6_1"] * 100, 1) if (tech and tech["mom_6_1"] is not None) else None,
            "drivers": [{"verb": vb, "rule": r, "why": w} for (vb, r, w) in fired]
                       or [{"verb": "HOLD", "rule": "DEFAULT", "why": "no rule fired"}],
        })

    note = (f"Only {len(hs)} holding(s): concentration muted until "
            f">= {cfg.get('min_names_for_concentration',4)} names.") if small else None
    return {"note": note, "portfolio_notes": sorted(set(portfolio_notes)), "verdicts": out}


def main():
    print(json.dumps(compute(), indent=2))


if __name__ == "__main__":
    main()
