from typing import Any, Dict, List, Tuple, Union


class Interfaces:
    def __init__(self, api_client):
        self._api_client = api_client

    def get_interfaces_config(self) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = "/interfaces/config"

        return self._api_client.get(endpoint)

    def create_interfaces_config(self, config: Dict[str, Any]) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = "/interfaces/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_interfaces_config(self, config: List[Dict[str, Any]]) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = "/interfaces/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_interfaces_config(self, config: List[str]) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = "/interfaces/config"

        data = {"data": config}

        return self._api_client.delete(endpoint, data=data)

    def get_interfaces_config_by_id(self, interface_id: str) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = f"/interfaces/config/{interface_id}"

        return self._api_client.get(endpoint)

    def update_interfaces_config_by_id(self, interface_id: str, config: Dict[str, Any]) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = f"/interfaces/config/{interface_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_interfaces_config_by_id(self, interface_id: str) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = f"/interfaces/config/{interface_id}"

        return self._api_client.delete(endpoint)

    def get_interfaces_status(self) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = "/interfaces/status"

        return self._api_client.get(endpoint)

    def get_interfaces_status_by_id(self, interface_id: str) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = f"/interfaces/status/{interface_id}"

        return self._api_client.get(endpoint)
