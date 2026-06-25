from typing import Self

from ..._client import APIClient
from ...endpoints import *


class Gateway:
    def __init__(self, base_url: str, *, timeout: float = 10.0, verify: bool | str = True) -> None:
        self._client = APIClient(base_url, timeout=timeout, verify=verify)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()
