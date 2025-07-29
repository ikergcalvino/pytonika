from typing import Any, Dict, List, Tuple, Union


class Unauthorized:
    def __init__(self, api_client):
        self._api_client = api_client

    def get_unauthorized_status(self) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = "/unauthorized/status"

        return self._api_client.get(endpoint)
