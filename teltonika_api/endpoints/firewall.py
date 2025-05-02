from typing import Any, Dict, List, Tuple, Union


class Firewall:
    def __init__(self, api_client):
        self._api_client = api_client

    def get_firewall_connections_status(self) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = "/firewall/connections/status"

        return self._api_client.get(endpoint)

    def get_firewall_port_forwards_config(self) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = "/firewall/port_forwards/config"

        return self._api_client.get(endpoint)

    def create_firewall_port_forwards_config(self, config: Dict[str, Any]) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = "/firewall/port_forwards/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_firewall_port_forwards_config(self, config: List[Dict[str, Any]]) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = "/firewall/port_forwards/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_firewall_port_forwards_config(self, config: List[str]) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = "/firewall/port_forwards/config"

        data = {"data": config}

        return self._api_client.delete(endpoint, data=data)

    def get_firewall_port_forwards_config_by_id(self, port_forward_id: str) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = f"/firewall/port_forwards/config/{port_forward_id}"

        return self._api_client.get(endpoint)

    def update_firewall_port_forwards_config_by_id(self, port_forward_id: str, config: Dict[str, Any]) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = f"/firewall/port_forwards/config/{port_forward_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_firewall_port_forwards_config_by_id(self, port_forward_id: str) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = f"/firewall/port_forwards/config/{port_forward_id}"

        return self._api_client.delete(endpoint)
