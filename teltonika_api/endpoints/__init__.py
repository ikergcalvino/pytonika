"""
API endpoint modules for Teltonika router interfaces.

This package organizes the router's API functionality into logical groups
based on their purpose and authentication requirements. Each endpoint group
encapsulates related API operations, providing a clean and intuitive interface.
"""

from .authentication import Authentication
from .unauthorized import Unauthorized
from .users import Users

__all__ = ["Authentication", "Unauthorized", "Users"]
