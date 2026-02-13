---
name: distributor
parent: content-creation-system
input: {content: {}, platforms: [str]}
output: {schedule: {}, repurpose_plan: {}}
---

# Distribution & Timing

## Task

Optimal posting schedule + cross-platform repurposing.

## Timing Logic

- Platform-specific windows (based on user's audience behavior)
- Engagement window: respond within 1-2 hours post-publish
- Avoid saturation: content spaced 48-72 hours apart

## Repurposing Strategy

- **YouTube** (16:9, 10min) → **IG Reels** (9:16, 60s), **TikTok** (9:16, 30s hook)
- Extract key quotes → carousel posts

## Memory Update

Writes: `persona-voice/memory/past_content_index.json` (performance data)

## Output Example

```json
{
  "schedule": {
    "tiktok": "2026-02-15 18:00 WIB",
    "ig": "2026-02-15 19:00 WIB"
  },
  "repurpose_plan": [
    "Cut YT intro for TikTok",
    "3 quote cards for IG"
  ]
}
```
