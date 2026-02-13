# Berkarja

Multi-agent content creation system with real-time trend intelligence. Coordinates content from ideation through planning to publishing.

## Overview

- **Idea validation** → novelty, platform fit, viability
- **Trend intelligence** → context, saturation, timing
- **Brand persona** → consistency checks
- **Production planning** → blueprints, repurposing
- **Distribution** → scheduling, platform optimization
- **Performance analysis** → post-publish tracking
- **Research** → fact-checking and citations

## Quick Start

```bash
cd content-creation-system
pip install -r requirements.txt
cp config.template.yaml config.yaml
# Edit config.yaml with your brand, platforms, and API keys
```

Or use the interactive setup wizard:

```bash
python sub-agents/setup-wizard/interview.py
```

See [content-creation-system/SETUP.md](content-creation-system/SETUP.md) for full onboarding.

## Repository Structure

```
content-creation-system/     # Single package — configure for your brand
├── sub-agents/              # Validator, planner, trends, persona, analyst, distributor, research, setup-wizard
├── knowledge-base/          # Templates and best practices
├── scripts/                 # Shared utilities
├── config.template.yaml     # Copy to config.yaml and customize
└── SETUP.md                 # Detailed setup guide
```

## Sub-Agents

Each sub-agent is a focused skill (see `SKILL.md` in each folder):

| Agent | Purpose |
|-------|---------|
| `setup-wizard` | Interactive onboarding, generates config from interview |
| `content-idea-validator` | Score ideas against rubric |
| `content-planner` | Generate production blueprints |
| `trend-intelligence` | Crawl and analyze trends |
| `persona-voice` | Brand alignment |
| `performance-analyst` | Metrics and patterns |
| `distribution-timing` | Scheduling and repurposing |
| `research-factcheck` | Citations and verification |

## License

MIT
