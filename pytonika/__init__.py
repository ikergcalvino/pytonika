from importlib.metadata import version

from . import devices
from ._connect import connect
from .devices import *

__version__ = version("pytonika")

__all__ = ["__version__", "connect"]
__all__ += devices.__all__
