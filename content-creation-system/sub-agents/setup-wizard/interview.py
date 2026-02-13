#!/usr/bin/env python3
"""
Setup Wizard — Conversational onboarding to generate personalized config.
Run: python interview.py
"""

import argparse
import sys
from pathlib import Path

from generate_config import generate_config, write_to_disk


def _prompt(text: str, default: str = "") -> str:
    """Prompt user, return trimmed response or default."""
    suffix = f" [{default}]" if default else ""
    try:
        ans = input(f"\n{text}{suffix}: ").strip()
        return ans if ans else default
    except (EOFError, KeyboardInterrupt):
        return default


def _prompt_list(text: str, example: str = "e.g. topic1, topic2") -> list[str]:
    """Prompt for comma-separated list, return list of trimmed non-empty items."""
    raw = _prompt(f"{text} ({example})")
    return [x.strip() for x in raw.split(",") if x.strip()]


def conversational_interview(section: str | None = None) -> dict:
    """
    Run the interview and return a responses dict.
    If section is set, only ask questions for that section.
    """
    responses: dict = {}

    # Phase 1: Brand Identity
    if section is None or section == "brand_voice":
        print("\n--- Phase 1: Brand Identity ---")
        responses["name"] = _prompt("What's your name?", "Creator")
        responses["about"] = _prompt("What do you create content about?")
        responses["brand_voice"] = _prompt(
            "Describe your brand voice (tone + style)",
            "e.g. technical but accessible, humorous, formal",
        )
        responses["pillars"] = _prompt_list(
            "What topics do you cover? (3–5 content pillars)",
            "e.g. neurotech, AI, productivity",
        )
        responses["forbidden"] = _prompt("Any forbidden topics or sensitive areas to avoid?", "")
        responses["good_example"] = _prompt(
            "Example of content that fits your voice",
            'e.g. "Explaining BCI like Shazam for your brain"',
        )
        responses["bad_example"] = _prompt(
            "Example of content that does NOT fit",
            "e.g. Dense academic paper style",
        )

    if section == "brand_voice":
        return responses

    # Phase 2: Platforms & Audience
    if section is None or section == "platforms":
        print("\n--- Phase 2: Platforms & Audience ---")
        responses["platforms"] = _prompt_list(
            "Which platforms?",
            "TikTok, Instagram, YouTube, LinkedIn",
        )
        responses["audience"] = _prompt(
            "Who's your target audience?",
            "e.g. technical professionals exploring neurotechnology",
        )
        responses["pain_points"] = _prompt(
            "Their pain points? (comma-separated)",
            "e.g. understanding BCI complexity, career transitions",
        )
        responses["velocity"] = _prompt(
            "How often do you post?",
            "daily, 3x/week, weekly",
        )

    if section == "platforms":
        return responses

    # Phase 3: Production
    if section is None or section == "production":
        print("\n--- Phase 3: Production ---")
        responses["equipment"] = _prompt(
            "What equipment do you have?",
            "camera, mic, lighting",
        )
        responses["location"] = _prompt(
            "Where do you shoot?",
            "home studio, office, outdoor",
        )
        responses["time_constraints"] = _prompt(
            "Time constraints?",
            "full production vs quick shoots",
        )

    if section == "production":
        return responses

    # Phase 4: Validation Boundaries
    if section is None or section == "validation":
        print("\n--- Phase 4: Validation Boundaries ---")
        responses["effort"] = _prompt(
            "Effort threshold?",
            "high-effort productions vs quick wins",
        )
        responses["novelty"] = _prompt(
            "Novelty preference?",
            "always innovate vs stick to proven formats",
        )
        responses["trend_sensitivity"] = _prompt(
            "Trend sensitivity?",
            "chase trends vs evergreen content",
        )

    return responses


def main() -> int:
    parser = argparse.ArgumentParser(description="Content Creation System — Setup Wizard")
    parser.add_argument(
        "--section",
        choices=["brand_voice", "platforms", "production", "validation"],
        help="Reconfigure only this section",
    )
    parser.add_argument(
        "--config-dir",
        type=Path,
        default=None,
        help="Config output directory (default: content-creation-system/config/)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print generated configs without writing",
    )
    args = parser.parse_args()

    # Resolve config dir: default to content-creation-system/config/
    if args.config_dir is None:
        script_dir = Path(__file__).resolve().parent
        root = script_dir.parent.parent  # sub-agents/setup-wizard -> content-creation-system
        args.config_dir = root / "config"

    print("Content Creation System — Setup Wizard")
    print("Answer the questions below. Press Enter for defaults.\n")

    responses = conversational_interview(args.section)

    # If section-only, we need full responses for config generation
    # Merge with minimal defaults for missing phases
    if args.section:
        full = {
            "name": "Creator",
            "about": "",
            "brand_voice": "professional, accessible",
            "pillars": ["education", "inspiration", "community"],
            "forbidden": "",
            "good_example": "Explaining complex topics with clear analogies",
            "bad_example": "Dense jargon-heavy academic style",
            "platforms": ["tiktok", "instagram", "youtube"],
            "audience": "",
            "pain_points": [],
            "velocity": "3x/week",
            "equipment": "",
            "location": "",
            "time_constraints": "",
            "effort": "medium",
            "novelty": "medium",
            "trend_sensitivity": "medium",
        }
        full.update(responses)
        responses = full

    configs = generate_config(responses)

    if args.dry_run:
        for name, content in configs.items():
            print(f"\n--- {name} ---\n{content}")
        return 0

    written = write_to_disk(configs, args.config_dir)
    print("\n✓ Setup complete. Config written to:")
    for p in written:
        print(f"  {p}")
    print("\nStart creating: 'I have a content idea...'")
    return 0


if __name__ == "__main__":
    sys.exit(main())
