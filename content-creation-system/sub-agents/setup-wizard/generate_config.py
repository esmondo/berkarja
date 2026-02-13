"""
Generate config files from Setup Wizard interview responses.
Output structure aligned with config-templates/*.template.yaml
"""

import yaml
from datetime import datetime
from pathlib import Path
from typing import Any


def _normalize_platform(s: str) -> str:
    """Map user input to canonical platform key."""
    m = {
        "tiktok": "tiktok",
        "ig": "instagram",
        "instagram": "instagram",
        "yt": "youtube",
        "youtube": "youtube",
        "linkedin": "linkedin",
        "twitter": "twitter",
        "x": "twitter",
    }
    return m.get(s.lower().strip(), s.lower().replace(" ", "_"))


def _parse_velocity(freq: str) -> int:
    """Map posting frequency to weekly_target."""
    freq = (freq or "").lower()
    if "daily" in freq or "every day" in freq:
        return 7
    if "3x" in freq or "3/" in freq or "thrice" in freq:
        return 3
    if "weekly" in freq or "once" in freq:
        return 1
    if "twice" in freq or "2x" in freq:
        return 2
    return 3  # default


def _parse_effort(s: str) -> str:
    """Map effort threshold to low/medium/high."""
    s = (s or "").lower()
    if "high" in s or "full" in s or "complex" in s:
        return "high"
    if "low" in s or "quick" in s or "minimal" in s:
        return "low"
    return "medium"


def _parse_novelty(s: str) -> str:
    """Map novelty preference."""
    s = (s or "").lower()
    if "innovate" in s or "new" in s or "experiment" in s:
        return "high"
    if "proven" in s or "stick" in s or "safe" in s:
        return "low"
    return "medium"


def _parse_trend_sensitivity(s: str) -> str:
    """Map trend sensitivity."""
    s = (s or "").lower()
    if "chase" in s or "trend" in s or "viral" in s:
        return "high"
    if "evergreen" in s or "timeless" in s or "ignore" in s:
        return "low"
    return "medium"


def _trend_to_float(s: str) -> float:
    """Map trend sensitivity string to 0-1 float."""
    s = (s or "").lower()
    if "high" in s:
        return 0.8
    if "low" in s:
        return 0.3
    return 0.5


def _novelty_to_float(s: str) -> float:
    """Map novelty preference to minimum novelty score 0-1."""
    s = (s or "").lower()
    if "high" in s or "innovate" in s:
        return 0.6
    if "low" in s or "proven" in s:
        return 0.3
    return 0.5


def _infer_humor(brand_voice_desc: str) -> str:
    """Infer humor_level from brand voice description."""
    s = (brand_voice_desc or "").lower()
    if "humor" in s or "funny" in s or "wit" in s:
        return "high"
    if "serious" in s or "formal" in s or "professional" in s:
        return "low"
    return "medium"


def _infer_jargon(brand_voice_desc: str) -> str:
    """Infer jargon_tolerance from brand voice description."""
    s = (brand_voice_desc or "").lower()
    if "technical" in s or "jargon" in s or "expert" in s:
        return "technical"
    if "accessible" in s or "simple" in s or "minimal" in s:
        return "minimal"
    return "moderate"


def generate_config(responses: dict[str, Any]) -> dict[str, str]:
    """
    Convert interview responses into YAML config content strings.
    Returns dict mapping filename -> YAML string.
    """
    name = (responses.get("name") or "").strip() or "Creator"
    about = (responses.get("about") or "").strip()
    brand_voice_desc = (responses.get("brand_voice") or "").strip()
    pillars_raw = responses.get("pillars") or []
    forbidden = responses.get("forbidden") or []
    platforms_raw = responses.get("platforms") or []
    audience = (responses.get("audience") or "").strip()
    velocity_raw = responses.get("velocity") or ""
    equipment = (responses.get("equipment") or "").strip()
    location = (responses.get("location") or "").strip()
    time_constraints = (responses.get("time_constraints") or "").strip()
    effort_raw = responses.get("effort") or ""
    novelty_raw = responses.get("novelty") or ""
    trend_raw = responses.get("trend_sensitivity") or ""

    # Parse pillars: support string list or comma-separated
    if isinstance(pillars_raw, str):
        pillars_raw = [p.strip() for p in pillars_raw.split(",") if p.strip()]
    pillars = [p for p in pillars_raw if p][:5]

    # Parse platforms
    if isinstance(platforms_raw, str):
        platforms_raw = [p.strip() for p in platforms_raw.split(",") if p.strip()]
    platforms = [_normalize_platform(p) for p in platforms_raw if p]
    if not platforms:
        platforms = ["tiktok", "instagram", "youtube"]

    weekly_target = _parse_velocity(velocity_raw)
    effort = _parse_effort(effort_raw)
    novelty = _parse_novelty(novelty_raw)
    trend_sensitivity = _parse_trend_sensitivity(trend_raw)

    # Infer voice params from brand_voice text
    tone_val = responses.get("tone") or brand_voice_desc or "technical + accessible"
    style_val = responses.get("style") or "conversational, scannable"
    humor = responses.get("humor_level") or _infer_humor(brand_voice_desc)
    jargon = responses.get("jargon_tolerance") or _infer_jargon(brand_voice_desc)
    good_ex = responses.get("good_example") or 'Explaining complex topics with clear analogies'
    bad_ex = responses.get("bad_example") or "Dense, jargon-heavy academic style"

    if isinstance(forbidden, str) and forbidden:
        forbidden_list = [t.strip() for t in forbidden.split(",") if t.strip()]
    elif isinstance(forbidden, list):
        forbidden_list = forbidden
    else:
        forbidden_list = []

    # --- brand_voice.yaml (aligned with config-templates/brand_voice.template.yaml) ---
    brand_voice = {
        "user": {
            "name": name,
            "bio": about or "",
        },
        "voice": {
            "tone": tone_val,
            "style": style_val,
            "humor_level": humor,
            "jargon_tolerance": jargon,
        },
        "forbidden": {"topics": forbidden_list},
        "examples": {"good": good_ex, "bad": bad_ex},
    }

    # --- content_pillars.yaml (aligned with config-templates/content_pillars.template.yaml) ---
    if not pillars:
        pillars = ["education", "inspiration", "community"]

    weights = responses.get("pillar_weights")
    if isinstance(weights, (list, tuple)) and len(weights) >= len(pillars):
        weight_list = [float(w) for w in weights[: len(pillars)]]
    else:
        weight_per_pillar = 1.0 / len(pillars)
        weight_list = [round(weight_per_pillar, 2)] * len(pillars)

    def pillar_entry(i: int, p: Any, w: float) -> dict:
        if isinstance(p, dict):
            return {
                "name": p.get("name", ""),
                "weight": w,
                "subtopics": p.get("subtopics", []),
            }
        pillar_name = str(p).replace("_", " ").title()
        return {
            "name": pillar_name,
            "weight": w,
            "subtopics": [],
        }

    pain_raw = responses.get("pain_points") or []
    if isinstance(pain_raw, str):
        pain_raw = [x.strip() for x in pain_raw.split(",") if x.strip()]

    content_pillars = {
        "pillars": [pillar_entry(i, p, weight_list[i]) for i, p in enumerate(pillars[:5])],
        "audience": {
            "primary": audience or "General audience",
            "pain_points": pain_raw,
        },
    }

    # --- platform_specs.yaml (scheduling) ---
    default_hours = [9, 12, 18, 21]
    default_days = [2, 3, 4, 5]  # Tue–Fri
    velocity_str = f"{weekly_target}x/week" if weekly_target > 1 else "weekly"
    platform_specs = {
        "platforms": {},
        "audience": audience or "General audience",
        "production": {
            "equipment": equipment or "Not specified",
            "location": location or "Not specified",
            "time_constraints": time_constraints or "Flexible",
        },
        "validation": {
            "effort_threshold": effort,
            "novelty_preference": novelty,
            "trend_sensitivity": trend_sensitivity,
        },
    }
    for p in platforms:
        platform_specs["platforms"][p] = {
            "best_hours": default_hours,
            "best_days": default_days,
            "timezone": "UTC",
        }

    # --- config.yaml (aligned with config-templates/config.template.yaml) ---
    freq_map = {p: velocity_str for p in platforms}
    enabled_map = {p: True for p in platforms}
    for pk in ["tiktok", "instagram", "youtube"]:
        if pk not in enabled_map:
            enabled_map[pk] = pk in platforms
        if pk not in freq_map:
            freq_map[pk] = velocity_str

    equipment_list = [x.strip() for x in (equipment or "").split(",") if x.strip()] or ["Not specified"]
    locations_list = [x.strip() for x in (location or "").split(",") if x.strip()] or ["Not specified"]

    config_yaml = {
        "system": {
            "version": "1.0.0",
            "initialized": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        },
        "platforms": {
            "active": platforms,
            "tiktok": {
                "enabled": "tiktok" in platforms,
                "posting_frequency": freq_map.get("tiktok", velocity_str),
            },
            "instagram": {
                "enabled": "instagram" in platforms,
                "posting_frequency": freq_map.get("instagram", velocity_str),
            },
            "youtube": {
                "enabled": "youtube" in platforms,
                "posting_frequency": freq_map.get("youtube", velocity_str),
            },
        },
        "production": {
            "equipment": equipment_list,
            "locations": locations_list,
            "effort_threshold": effort,
        },
        "validation": {
            "novelty_min": _novelty_to_float(novelty_raw),
            "trend_sensitivity": _trend_to_float(trend_raw),
        },
        "memory": {
            "vector_db": "pinecone",
            "refresh_cycle": "weekly",
        },
        "api_keys": {
            "ensemble_data": "${ENSEMBLE_KEY}",
            "analytics": "${ANALYTICS_KEY}",
        },
        # Legacy paths for sub-agents that reference config
        "paths": {
            "knowledge_base": "knowledge-base/",
            "scripts": "scripts/",
            "sub_agents": "sub-agents/",
            "config": "config/",
        },
        "user": {
            "name": name,
            "brand_pillars": [str(p).replace(" ", "_").lower() for p in pillars] if pillars else [],
            "platforms": platforms,
        },
        "content_velocity": {
            "weekly_target": weekly_target,
            "effort_threshold": effort,
        },
    }

    def to_yaml(obj: dict) -> str:
        return yaml.dump(obj, default_flow_style=False, allow_unicode=True, sort_keys=False)

    return {
        "brand_voice.yaml": to_yaml(brand_voice),
        "content_pillars.yaml": to_yaml(content_pillars),
        "platform_specs.yaml": to_yaml(platform_specs),
        "config.yaml": to_yaml(config_yaml),
    }


def write_to_disk(configs: dict[str, str], config_dir: Path | str) -> list[Path]:
    """Write config dict to config_dir. Creates dir if needed. Returns list of written paths."""
    config_dir = Path(config_dir)
    config_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for filename, content in configs.items():
        path = config_dir / filename
        path.write_text(content, encoding="utf-8")
        written.append(path)
    return written
