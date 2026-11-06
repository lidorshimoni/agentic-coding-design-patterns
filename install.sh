#!/usr/bin/env bash
set -euo pipefail

# Agentic Coding Design Patterns - Quick Installer Wrapper
# Usage: ./install.sh [--target claude,cursor,antigravity,...] [--output-dir /path/to/project]

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_BIN="$(command -v python3 || command -v python || true)"

if [ -z "$PYTHON_BIN" ]; then
    echo "Error: Python 3 is required to run the installer script." >&2
    exit 1
fi

"$PYTHON_BIN" "$SCRIPT_DIR/cli/sync.py" "$@"
