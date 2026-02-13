# Berkarja

Multi-agent content creation system with real-time trend intelligence. Coordinates content from ideation through planning to publishing.

## Install (copy-paste, works from any directory)

```bash
curl -fsSL https://raw.githubusercontent.com/esmondo/berkarja/main/scripts/install.sh | bash
```

Installs to `~/.berkarja` by default. Custom path: `curl -fsSL ... | bash -s -- ~/my-path`

## Overview

- **Idea validation** → novelty, platform fit, viability
- **Trend intelligence** → context, saturation, timing
- **Brand persona** → consistency checks
- **Production planning** → blueprints, repurposing
- **Distribution** → scheduling, platform optimization
- **Performance analysis** → post-publish tracking
- **Research** → fact-checking and citations

## Quick Start (after install)

```bash
cd ~/.berkarja/content-creation-system
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
