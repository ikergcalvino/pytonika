from typing import Any, Dict, List, Tuple, Union


class Authentication:
    def __init__(self, api_client):
        self._api_client = api_client

    def login(self, username: str, password: str) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = "/login"

        data = {
            "username": username,
            "password": password
        }

        success, response = self._api_client.post(endpoint, data=data)

        if success and "token" in response:
            self._api_client._auth_token = response.get("token")

        return success, response

    def logout(self) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = "/logout"

        success, response = self._api_client.post(endpoint)

        if success:
            self._api_client._auth_token = None
            self._api_client._session.cookies.clear()

        return success, response

    def get_session_status(self) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = "/session/status"

        return self._api_client.get(endpoint)
