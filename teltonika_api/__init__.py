"""
Teltonika API Client

A clean, Pythonic interface for interacting with Teltonika routers through their REST API.
This package organizes API endpoints into logical namespaces reflecting the API structure,
providing an intuitive and maintainable way to manage Teltonika devices.
"""

from .router import Router

__version__ = "0.1.0"
__all__ = ["Router"]
