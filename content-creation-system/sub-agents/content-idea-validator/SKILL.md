---
name: validator
parent: content-creation-system
input: {idea: str, platforms: [str]}
output: {novelty: float, fit: {}, viable: bool, rec: [str]}
---

# Content Idea Validator

## Task

Score ideas on novelty (0-1), platform fit, viability.

## Logic

- **Novelty**: Query `persona-voice/memory/past_content_index.json` + trends/saturation check
- **Platform Fit**:
  - **TikTok**: hook (3s), trend-ready, audio-driven
  - **IG**: visual quality, 15-90s, editing complexity
  - **YT**: depth potential, 8-15min, retention structure
- **Viability**: Check effort (L/M/H), resources, brand_pillars alignment

## Output Format

```json
{
  "novelty": 0.75,
  "fit": {
    "tiktok": 0.9,
    "ig": 0.7,
    "yt": 0.5
  },
  "viable": true,
  "rec": [
    "Strong TikTok hook",
    "Add visual B-roll for IG"
  ]
}
```
