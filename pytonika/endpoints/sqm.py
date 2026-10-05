from typing import Any

from ._base import Endpoint


class SQM(Endpoint):
    def get_sqm_config(self) -> dict[str, Any]:
        """Returns SQM configurations."""
        endpoint = "/sqm/config"

        return self._client.request("GET", endpoint)

    def create_sqm_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create SQM configuration."""
        endpoint = "/sqm/config"

        data = {"data": config}

        return self._client.request("POST", endpoint, json=data)

    def update_sqm_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates SQM configurations."""
        endpoint = "/sqm/config"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def delete_sqm_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes SQM configurations."""
        return [self.delete_sqm_config_by_id(sqm_id) for sqm_id in config]

    def get_sqm_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns SQM configuration."""
        endpoint = f"/sqm/config/{config_id}"

        return self._client.request("GET", endpoint)

    def update_sqm_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates SQM configuration."""
        endpoint = f"/sqm/config/{config_id}"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def delete_sqm_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes SQM configuration."""
        endpoint = f"/sqm/config/{config_id}"

        return self._client.request("DELETE", endpoint)

    def get_sqm_options(self) -> dict[str, Any]:
        """Returns SQM options."""
        endpoint = "/sqm/options"

        return self._client.request("GET", endpoint)
