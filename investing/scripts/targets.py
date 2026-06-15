"""targets.py — compute a target price, a laddered SELL plan, and a target
DURATION (with time-stop date) for each holding, from the methods in rules.md.

These are METHOD-DERIVED levels from your own entry/stop/trade-type inputs —
arithmetic, not predictions. A target price is not a forecast that price will
get there; it's the level your chosen reward:risk method points to.

Needs per-holding front-matter: cost_basis (entry), initial_stop, trade_type,
opened (YYYY-MM-DD). Falls back gracefully if fields are missing.
"""
from __future__ import annotations
import datetime as dt
import json
import os
import yaml
from common import load_holdings
import technicals

RULES = os.path.join(os.path.dirname(__file__), "..", "rules.md")


def load_cfg() -> dict:
    txt = open(RULES, encoding="utf-8").read()
    return (yaml.safe_load(txt.split("---", 2)[1]) or {}) if txt.startswith("---") else {}


def target_price(entry, stop, tech, cfg):
    """Return (target, method_used). r_multiple is the default/fallback."""
    method = cfg.get("target_method", "r_multiple")
    rr = float(cfg.get("reward_risk", 3.0))
    risk = (entry - stop) if (entry and stop and entry > stop) else None
    r_target = (entry + rr * risk) if risk else None

    if method == "atr" and tech and tech.get("atr"):
        return round(entry + float(cfg.get("atr_target_mult", 4.0)) * tech["atr"], 2), "atr"
    if method == "structure" and tech:
        # use prior 52w-high area as a structure ceiling proxy; take the lower of
        # structure vs the R-multiple target so the objective stays realistic
        struct = None
        if tech.get("dist_52w_high_pct") is not None and tech.get("price"):
            struct = tech["price"] / (1 + tech["dist_52w_high_pct"] / 100)  # = 52w high
        cands = [x for x in (struct, r_target) if x]
        if cands:
            return round(min(cands), 2), "structure(min vs R)"
    if r_target:
        return round(r_target, 2), "r_multiple"
    return None, "needs entry+stop"


def main():
    cfg = load_cfg()
    today = dt.date.today()
    dur = {k: int(cfg.get(f"duration_days_{k}", d)) for k, d in
           [("swing", 21), ("momentum", 90), ("catalyst", 45), ("core", 365)]}
    out = []
    for h in load_holdings():
        m = h["meta"]
        entry = m.get("cost_basis")
        stop = m.get("initial_stop")
        ttype = m.get("trade_type", "core")
        tech = technicals.fetch(m["ticker"], cfg)
        px = (tech or {}).get("price") or m.get("last_price")
        risk = (entry - stop) if (entry and stop and entry > stop) else None

        tgt, method = target_price(entry, stop, tech, cfg)
        # laddered sell plan
        plan = None
        if risk:
            t1 = round(entry + float(cfg["t1_r"]) * risk, 2)
            t2 = round(entry + float(cfg["t2_r"]) * risk, 2)
            plan = {
                "T1": {"price": t1, "r": cfg["t1_r"],
                       "action": f"sell {float(cfg['t1_fraction'])*100:.0f}%, move stop to breakeven ({entry})"},
                "T2": {"price": t2, "r": cfg["t2_r"],
                       "action": "trail remainder (Chandelier) toward here"},
            }
        # progress to T1
        progress = None
        if risk and px:
            t1 = entry + float(cfg["t1_r"]) * risk
            progress = round((px - entry) / (t1 - entry), 2) if (t1 - entry) else None

        # duration + time-stop date
        target_days = dur.get(ttype, dur["core"])
        opened = m.get("opened")
        time_stop_date, time_stop_hit = None, None
        if opened:
            d0 = opened if isinstance(opened, dt.date) else dt.date.fromisoformat(str(opened))
            time_stop_date = (d0 + dt.timedelta(days=target_days)).isoformat()
            elapsed = (today - d0).days
            if elapsed >= target_days and (progress is None or progress < float(cfg["time_stop_progress"])):
                time_stop_hit = True

        out.append({
            "ticker": m["ticker"], "trade_type": ttype, "price": px,
            "entry": entry, "stop": stop, "risk_per_share": round(risk, 2) if risk else None,
            "target_price": tgt, "target_method": method,
            "reward_risk": cfg.get("reward_risk"),
            "sell_plan": plan, "progress_to_T1": progress,
            "target_duration_days": target_days, "time_stop_date": time_stop_date,
            "time_stop_hit": time_stop_hit,
            "needs": [k for k, v in {"initial_stop": stop, "opened": opened}.items() if not v] or None,
        })
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
