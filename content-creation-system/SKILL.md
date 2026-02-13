---
name: content-creation-system
version: 1.0.0
description: Multi-agent content workflow with real-time trend intelligence
sub_agents:
  - setup-wizard
  - validator
  - planner
  - trends
  - persona
  - analyst
  - distributor
  - research
---

# Content Creation System (Open-Source)

Generic, configurable instance. See [SETUP.md](SETUP.md) for onboarding.

## Role

Coordinate content creation from ideation to publishing. Route tasks to specialized agents. Customize via templates and `config.template.yaml`.

## Workflow

1. Idea → validator → trends + persona → planner → distributor
2. Post-publish → analyst
3. research available throughout

## Routing Logic

- User says "setup", "reconfigure", or first run: **setup-wizard** (run `python sub-agents/setup-wizard/interview.py`)
- User submits idea: validator + trends
- User asks planning: planner (assumes validated)
- User asks performance: analyst
- Fact-checking needed: research
- Persona invoked when brand consistency questioned

## Memory

- Accesses: `knowledge-base/`, `scripts/`, `config.yaml`
- Sub-agents share context via `memory_management.py`
