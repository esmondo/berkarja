#!/usr/bin/env bash
# Berkarja — skills-only install (no Python, no config)
# Adds content-creation skill to Cursor. Works from any directory.
# Usage: curl -fsSL https://raw.githubusercontent.com/esmondo/berkarja/main/scripts/install-skill-only.sh | bash

set -e

REPO_URL="https://github.com/esmondo/berkarja.git"
SKILLS_DIR="${CURSOR_SKILLS_HOME:-$HOME/.cursor/skills}"
TEMP_DIR=$(mktemp -d)
trap 'rm -rf "$TEMP_DIR"' EXIT

echo "→ Berkarja skills-only installer"
echo "  Installing to: $SKILLS_DIR/content-creation-system"
echo ""

mkdir -p "$SKILLS_DIR"
git clone --depth 1 "$REPO_URL" "$TEMP_DIR"
cp -r "$TEMP_DIR/content-creation-system" "$SKILLS_DIR/"

echo "✓ Skill installed at: $SKILLS_DIR/content-creation-system"
echo ""
echo "Restart Cursor to load the skill. No Python or config required."
