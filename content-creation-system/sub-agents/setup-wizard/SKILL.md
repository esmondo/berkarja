---
name: setup-wizard
parent: content-creation-system
description: Interactive onboarding to generate personalized config
triggers: ["first run", "setup", "reconfigure"]
---

# Setup Wizard

## Role

Conversational interviewer that generates config files from user responses.

## Interview Flow

### Phase 1: Brand Identity (2 min)
- Q: "What's your name and what do you create content about?"
- Q: "Describe your brand voice (e.g., technical but accessible, humorous, formal)"
- Q: "What topics do you cover? (3–5 content pillars)"
- Q: "Any forbidden topics or sensitive areas to avoid?"

### Phase 2: Platforms & Audience (1 min)
- Q: "Which platforms? (TikTok, Instagram, YouTube, LinkedIn)"
- Q: "Who's your target audience? (demographics, interests, pain points)"
- Q: "How often do you post? (daily, 3x/week, weekly)"

### Phase 3: Production (1 min)
- Q: "What equipment do you have? (camera, mic, lighting)"
- Q: "Where do you shoot? (home studio, office, outdoor)"
- Q: "Time constraints? (full production vs quick shoots)"

### Phase 4: Validation Boundaries (1 min)
- Q: "Effort threshold? (high-effort productions vs quick wins)"
- Q: "Novelty preference? (always innovate vs stick to proven formats)"
- Q: "Trend sensitivity? (chase trends vs evergreen content)"

## Output

Generates in `config/`:
- `brand_voice.yaml`
- `content_pillars.yaml`
- `platform_specs.yaml`
- `config.yaml` (master config)

## Execution

```bash
# Run interactive setup
python sub-agents/setup-wizard/interview.py

# Reconfigure single section (e.g. brand_voice)
python sub-agents/setup-wizard/interview.py --section brand_voice
```

## Integration

When user invokes `@content-creation-system setup` or `setup` / `reconfigure`, run this sub-agent before routing to validator/planner.

## Reconfiguration Mode

**Section-only re-interview** (no full reset):
- `reconfigure brand_voice` → Only Phase 1 (Brand Identity)
- `reconfigure platforms` → Only Phase 2 (Platforms & Audience)
- `reconfigure production` → Only Phase 3 (Production)
- `reconfigure validation` → Only Phase 4 (Validation Boundaries)

**Conversational reconfig**: User says e.g. *"Update my brand voice to be more casual"* → Ask follow-up (*"On a scale 1–5, how casual? Any specific changes?"*) → Update `brand_voice.yaml` → agents use new settings immediately.

## Templates

Output structure aligned with `config-templates/*.template.yaml`. Generated configs can be edited anytime.
