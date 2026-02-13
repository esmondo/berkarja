---
name: research
parent: content-creation-system
input: {claim: str, topic: str}
output: {verified: bool, sources: [str], context: str}
---

# Research & Fact-Check

## Task

Verify technical claims, fetch citations (critical for neurotechnology/AI content).

## Sources

- Trusted: PubMed, arXiv, IEEE, official docs
- Cross-reference: min 2 sources

## Output

```json
{
  "verified": true,
  "sources": ["doi.org/paper123", "arxiv.org/abs/456"],
  "context": "Claim accurate as of 2025 study, new research pending"
}
```

## Use Cases

- EEG accuracy claims
- AI model capabilities
- Market statistics
