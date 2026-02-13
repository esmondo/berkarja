---
name: trends
parent: content-creation-system
output: {active: [], rising: [], saturated: [], projection: str}
---

# Trend Intelligence

## Dependencies

- `persona-voice/content_pillars.yaml`
- `analyze_velocity.py`

## Task

Real-time trend scraping + forward projection (2-4 weeks).

## Sources

- APIs: EnsembleData (TikTok/IG/YT scraping)
- Platform updates: `knowledge-base/algorithm_updates_2026.md`
- Cultural calendar: events, product launches

## Analysis

- **Velocity**: Growth rate (views/hr, engagement delta)
- **Saturation**: Creator count, format repetition
- **Projection**: Trend lifecycle stage (emerging/peak/decline)

## Output Format

```json
{
  "active": ["Grammy reactions", "Thermostat Game"],
  "rising": ["Group Consensus debates"],
  "saturated": ["Old trend X"],
  "projection": "Trend Y peaks in 10 days, capitalize now"
}
```
