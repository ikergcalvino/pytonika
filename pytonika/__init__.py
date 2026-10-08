from importlib.metadata import version

from . import devices
from .devices import *

__version__ = version("pytonika")

__all__ = ["__version__"]
__all__ += devices.__all__
