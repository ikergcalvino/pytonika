"""
API endpoint modules for Teltonika router interfaces.

This package organizes the router's API functionality into logical groups
based on their purpose and authentication requirements. Each endpoint group
encapsulates related API operations, providing a clean and intuitive interface.
"""

from .unauthorized import Unauthorized
from .authentication import Authentication

__all__ = ["Unauthorized", "Authentication"]
