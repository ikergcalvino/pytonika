from typing import IO, TypeAlias

from .._client import APIClient

File: TypeAlias = bytes | IO[bytes] | tuple[str, bytes | IO[bytes]]
"""A file to upload: its content, an open binary file, or a ``(filename, content)`` pair."""


class Endpoint:
    def __init__(self, client: APIClient) -> None:
        self._client = client
