#!/usr/bin/env python3
"""
API helpers. Shared utilities for platform and external API calls.
"""
import requests


def get(url: str, params: dict = None, headers: dict = None) -> requests.Response:
    """Wrapper for GET requests with common defaults."""
    return requests.get(url, params=params, headers=headers or {})


def post(url: str, data: dict = None, headers: dict = None) -> requests.Response:
    """Wrapper for POST requests with common defaults."""
    return requests.post(url, json=data, headers=headers or {})
