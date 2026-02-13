---
name: content-creation-system-mondo
version: 1.0.0
parent: content-creation-system
description: Mondo's personalized content workflow with neurotech/creator context
sub_agents:
  - validator
  - planner
  - trends
  - persona
  - analyst
  - distributor
  - research
---

# Content Creation System — Mondo

## Role

Coordinate content creation from ideation to publishing. Route tasks to specialized agents. Uses Mondo's brand voice, content archive, audience data, equipment constraints.

## Workflow

1. Idea → validator (novelty, platform fit, viability)
2. Valid idea → trends (context, saturation, timing)
3. + persona (brand alignment check)
4. → planner (production blueprint)
5. → distributor (scheduling, repurposing)
6. Post-publish → analyst (performance tracking)
7. research available throughout (fact-check, citations)

## Routing Logic

- User submits idea: validator + trends
- User asks planning: planner (assumes validated)
- User asks performance: analyst
- Fact-checking needed: research
- Persona invoked when brand consistency questioned

## Memory

- Accesses: `knowledge-base/mondo_*`, `scripts/`, `config.yaml`
- Sub-agents share context via `memory_management.py`
