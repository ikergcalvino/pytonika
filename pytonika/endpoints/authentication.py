from typing import Any

from ._base import Endpoint


class Authentication(Endpoint):
    def login(self, username: str, password: str) -> dict[str, Any]:
        """Authenticates user for API access."""
        endpoint = "/login"

        data = {"username": username, "password": password}

        response = self._client.request("POST", endpoint, json=data)

        token = (response.get("data") or {}).get("token")

        if isinstance(token, str):
            self._client.set_token(token)

        return response

    def logout(self) -> dict[str, Any]:
        """Logs out user from API."""
        endpoint = "/logout"

        response = self._client.request("POST", endpoint)

        self._client.clear_token()

        return response

    def get_session_status(self) -> dict[str, Any]:
        """Returns if API session is alive and resets session's timer."""
        endpoint = "/session/status"

        return self._client.request("GET", endpoint)
