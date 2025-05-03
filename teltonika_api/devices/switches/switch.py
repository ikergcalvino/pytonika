from abc import ABC
from ...api_client import ApiClient


class Switch(ABC):
    def __init__(self, base_url: str):
        self._api_client = ApiClient(base_url)
