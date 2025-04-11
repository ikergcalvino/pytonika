"""
Teltonika API Client

A clean, Pythonic interface for interacting with Teltonika routers through their REST API.

This package provides a comprehensive client library for Teltonika routers,
organizing API endpoints into logical groups that reflect the router's API structure.
The design focuses on simplicity, consistency, and developer experience.

Features:
- Complete API coverage with intuitive organization
- Consistent error handling and response formatting
- Both direct access to common methods and structured endpoint access
- Pythonic interface with type hints for better IDE integration
"""

from .router import Router

__version__ = "0.1.0"
__all__ = ["Router"]
