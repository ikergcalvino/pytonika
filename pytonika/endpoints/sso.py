from typing import Any

from ._base import Endpoint


class SSO(Endpoint):
    def get_sso_config(self) -> dict[str, Any]:
        """Returns SSO configurations."""
        endpoint = "/sso/config"

        return self._client.request("GET", endpoint)

    def create_sso_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates SSO configuration."""
        endpoint = "/sso/config"

        data = {"data": config}

        return self._client.request("POST", endpoint, json=data)

    def update_sso_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates SSO configurations."""
        endpoint = "/sso/config"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def delete_sso_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes SSO configurations."""
        return [self.delete_sso_config_by_id(sso_id) for sso_id in config]

    def get_sso_config_by_id(self, sso_id: str) -> dict[str, Any]:
        """Returns SSO configuration."""
        endpoint = f"/sso/config/{sso_id}"

        return self._client.request("GET", endpoint)

    def upload_sso_config_by_id(self, sso_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads icon file for SSO configuration."""
        endpoint = f"/sso/config/{sso_id}"

        return self._client.request("POST", endpoint, json=data)

    def update_sso_config_by_id(self, sso_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates SSO configuration."""
        endpoint = f"/sso/config/{sso_id}"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def delete_sso_config_by_id(self, sso_id: str) -> dict[str, Any]:
        """Deletes SSO configuration."""
        endpoint = f"/sso/config/{sso_id}"

        return self._client.request("DELETE", endpoint)
