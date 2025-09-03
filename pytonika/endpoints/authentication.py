from .._client import APIClient


class Authentication:
    def __init__(self, api_client: APIClient) -> None:
        self._api_client = api_client

    def login(self, username: str, password: str) -> dict[str, object]:
        endpoint = "/login"

        data = {
            "username": username,
            "password": password
        }

        response = self._api_client.post(endpoint, data=data)

        token = response["data"].get("token")

        if token:
            self._api_client.set_token(token)

        return response

    def logout(self) -> dict[str, object]:
        endpoint = "/logout"

        response = self._api_client.post(endpoint)

        self._api_client.clear_token()

        return response

    def get_session_status(self) -> dict[str, object]:
        endpoint = "/session/status"

        return self._api_client.get(endpoint)
