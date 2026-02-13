#!/usr/bin/env python3
"""
Voice consistency checker. Validates content against brand voice and pillars.
"""
import sys
import yaml


def load_brand_voice(path: str = "brand_voice.yaml") -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def load_pillars(path: str = "content_pillars.yaml") -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def check_consistency(content: str) -> dict:
    """Check content alignment with brand voice and pillars."""
    voice = load_brand_voice()
    pillars = load_pillars()
    # Placeholder: implement consistency checks
    return {"score": 0.0, "issues": [], "pillar_coverage": {}}


if __name__ == "__main__":
    content = sys.argv[1] if len(sys.argv) > 1 else ""
    result = check_consistency(content)
    print(result)
