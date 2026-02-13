---
name: persona
parent: content-creation-system
input: {content_draft: str}
output: {aligned: bool, issues: [str], suggestions: [str]}
---

# Persona & Voice

## Task

Verify brand consistency against user's voice profile.

## Check Points

- Tone matches `brand_voice.yaml` (technical + accessible)
- Topics align with `content_pillars.yaml` (neurotechnology, AI product, personal journey)
- Style consistent with past high-performers

## Memory Access

- `memory/past_content_index.json` (successful formats)
- `memory/audience_profile.json` (what resonates)

## Output

```json
{
  "aligned": false,
  "issues": ["Too technical, loses accessibility"],
  "suggestions": ["Add relatable analogy", "Simplify jargon"]
}
```
