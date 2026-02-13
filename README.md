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

## Repository Structure

| Folder | Purpose |
|--------|---------|
| **`content-creation-system-oss/`** | **Start here.** Generic, template-based instance. Use this for your own brand. See [SETUP.md](content-creation-system-oss/SETUP.md). |
| `content-creation-system/` | Full instance with config templates and setup wizard. |
| `content-creation-system-mondo/` | Example instance (Mondo config). |

For new users: clone and use **`content-creation-system-oss/`**.

## Quick Start

```bash
cd content-creation-system-oss
pip install -r requirements.txt
cp config.template.yaml config.yaml
# Edit config.yaml with your brand, platforms, and API keys
```

## Sub-Agents

Each sub-agent is a focused skill (see `SKILL.md` in each folder):

- `content-idea-validator` — Score ideas against rubric
- `content-planner` — Generate production blueprints
- `trend-intelligence` — Crawl and analyze trends
- `persona-voice` — Brand alignment
- `performance-analyst` — Metrics and patterns
- `distribution-timing` — Scheduling and repurposing
- `research-factcheck` — Citations and verification

## License

MIT
