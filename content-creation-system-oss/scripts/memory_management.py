#!/usr/bin/env python3
"""
Memory management utilities. Read/write for persona memory and content index.
"""
import json
from pathlib import Path
from typing import Any


def load_json(path: str) -> Any:
    """Load JSON file. Returns empty dict/list if missing."""
    p = Path(path)
    if not p.exists():
        return {} if "index" in path.lower() else []
    with open(p) as f:
        return json.load(f)


def save_json(path: str, data: Any) -> None:
    """Save data to JSON file. Ensures parent dir exists."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w") as f:
        json.dump(data, f, indent=2)
