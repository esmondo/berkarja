# Content Creation System — Setup Guide

Onboarding steps to run the system for your own brand and content.

## 1. Clone or Download

Ensure you have the full directory structure including `sub-agents/`, `scripts/`, and `knowledge-base/`.

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Configure

**Option A — Interactive setup:**
```bash
python sub-agents/setup-wizard/interview.py
```

**Option B — Manual:**
```bash
cp config.template.yaml config.yaml
```

Edit `config.yaml`:

- Set `preferences.default_platforms` (e.g. `[instagram, youtube]`)
- Set `preferences.timezone`
- Add API keys via environment variables or config (prefer env vars)

## 4. Customize Knowledge Base

- **Brand voice**: Copy `knowledge-base/template_brand_voice.yaml` to your own file (e.g. `my_brand_voice.yaml`) and fill in tone, vocabulary, themes.
- **Content archive**: Use `example_content_archive.json` as a reference. Create your archive (e.g. `my_content_archive.json`) with past content metadata.
- **Platform best practices**: Review `platform_best_practices.md` and update as needed for your niche.

## 5. Point Sub-Agents to Your Data

Update sub-agent configs (e.g. in `persona-voice/`, `content-idea-validator/`) to reference your knowledge-base files instead of templates.

## 6. Run

Invoke the skill when discussing content ideas, planning, or performance. Sub-agents will use your config and knowledge base.

## File Types

| Extension | Purpose |
|-----------|---------|
| `SKILL.md` | Skill definition (YAML frontmatter + instructions) |
| `.yaml` | Configuration, templates, structured data |
| `.py` | Executable logic (validation, API calls, data processing) |
| `.json` | Data storage (archives, trend data) |
| `.md` | Documentation, best practices |
