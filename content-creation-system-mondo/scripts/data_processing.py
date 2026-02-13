#!/usr/bin/env python3
"""
Data processing utilities. Shared functions for transforming and aggregating data.
"""
from typing import List, Any


def normalize_scores(values: List[float], min_val: float = 0, max_val: float = 1) -> List[float]:
    """Normalize list of values to [min_val, max_val] range."""
    if not values:
        return []
    v_min, v_max = min(values), max(values)
    span = v_max - v_min or 1
    return [min_val + (v - v_min) / span * (max_val - min_val) for v in values]


def aggregate_by_key(items: List[dict], key: str) -> dict:
    """Aggregate items by key, returning counts or sums per key value."""
    result = {}
    for item in items:
        k = item.get(key)
        if k is not None:
            result[k] = result.get(k, 0) + 1
    return result
