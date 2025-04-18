from typing import Any, Dict, List, Optional, Tuple, Union


class Users:
    def __init__(self, api_client):
        self._api_client = api_client

    def get_users_config(self) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = "/users/config"

        return self._api_client.get(endpoint)

    def create_users_config(self, data: Dict[str, Any]) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = "/users/config"

        return self._api_client.post(endpoint, data=data)

    def update_users_config(self, data: Dict[str, Any]) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = "/users/config"

        return self._api_client.put(endpoint, data=data)

    def delete_users_config(self, data: Dict[str, Any]) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = "/users/config"

        return self._api_client.delete(endpoint, data=data)

    def get_users_config_by_id(self, user_id: str) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = f"/users/config/{user_id}"

        return self._api_client.get(endpoint)

    def update_users_config_by_id(self, user_id: str, data: Dict[str, Any]) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = f"/users/config/{user_id}"

        return self._api_client.put(endpoint, data=data)

    def delete_users_config_by_id(self, user_id: str) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = f"/users/config/{user_id}"

        return self._api_client.delete(endpoint)
