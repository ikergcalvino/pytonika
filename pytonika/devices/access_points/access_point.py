from ..._client import APIClient
from ...endpoints import *


class AccessPoint:
    def __init__(self, base_url: str, *, timeout: float = 10.0, verify: bool | str = True) -> None:
        self._client = APIClient(base_url, timeout=timeout, verify=verify)
