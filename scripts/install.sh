#!/usr/bin/env bash
# Berkarja — one-line install from any directory
# Usage: curl -fsSL https://raw.githubusercontent.com/esmondo/berkarja/main/scripts/install.sh | bash
# Or:    curl -fsSL https://raw.githubusercontent.com/esmondo/berkarja/main/scripts/install.sh | bash -s -- ~/my-berkarja

set -e

REPO_URL="https://github.com/esmondo/berkarja.git"
INSTALL_DIR="${1:-$HOME/.berkarja}"

echo "→ Berkarja installer"
echo "  Installing to: $INSTALL_DIR"
echo ""

if [[ -d "$INSTALL_DIR" ]]; then
  echo "  Directory exists. Pulling latest..."
  (cd "$INSTALL_DIR" && git pull --quiet 2>/dev/null || true)
else
  echo "  Cloning repository..."
  git clone --depth 1 "$REPO_URL" "$INSTALL_DIR"
fi

cd "$INSTALL_DIR/content-creation-system"

echo "  Installing dependencies..."
pip install -q -r requirements.txt

if [[ ! -f config.yaml ]]; then
  cp config.template.yaml config.yaml
  echo "  Created config.yaml from template"
fi

echo ""
echo "✓ Berkarja installed at: $INSTALL_DIR"
echo ""
echo "Next steps:"
echo "  1. Run setup wizard:  cd $INSTALL_DIR/content-creation-system && python sub-agents/setup-wizard/interview.py"
echo "  2. Or edit config:     $INSTALL_DIR/content-creation-system/config.yaml"
echo ""
echo "Quick start:  cd $INSTALL_DIR/content-creation-system && python sub-agents/setup-wizard/interview.py"
