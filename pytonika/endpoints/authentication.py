from typing import Any

from ._endpoint import Endpoint


class Authentication(Endpoint):
    def login(self, username: str, password: str) -> dict[str, Any]:
        """Authenticates user for API access and stores the session token for later requests."""
        response = self._client.request("POST", "/login", json={"username": username, "password": password})

        token = (response.get("data") or {}).get("token")

        if isinstance(token, str):
            self._client.set_token(token)

        return response

    def logout(self) -> dict[str, Any]:
        """Logs out user from API and forgets the session token."""
        response = self._client.request("POST", "/logout")

        self._client.clear_token()

        return response

    def get_session_status(self) -> dict[str, Any]:
        """Returns if API session is alive and resets session's timer."""
        return self._client.request("GET", "/session/status")
