---
name: analyst
parent: content-creation-system
input: {content_id: str}
output: {metrics: {}, insights: [str], next_action: str}
---

# Performance Analyst

## Dependencies

- Loads: `platform_templates.yaml` (TikTok specs, IG specs, YT specs)
- Uses: persona (voice check), trends (timing optimization)

## Task

Post-mortem analysis + pattern detection.

## Metrics Track

- Views, engagement rate, retention curve
- TikTok completion%, IG saves, YT watch time

## Pattern Detection

- **High-performers**: common traits (format, topic, length)
- **Underperformers**: failure patterns
- **A/B test results**: what moved needle

## Output

```json
{
  "metrics": {"views": 5000, "engagement": 0.08},
  "insights": ["Hook too slow", "Topic resonated with audience"],
  "next_action": "Replicate format, tighten first 5s"
}
```
