from typing import Any

from ._endpoint import Endpoint


class SQM(Endpoint):
    def get_sqm_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns SQM configurations."""
        return self._client.request("GET", "/sqm/config", params={"all_options": all_options})

    def create_sqm_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create SQM configuration."""
        return self._client.request("POST", "/sqm/config", json={"data": config})

    def update_sqm_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates SQM configurations."""
        return self._client.request("PUT", "/sqm/config", json={"data": config})

    def delete_sqm_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes SQM configurations."""
        return self._client.request("DELETE", "/sqm/config", json={"data": config})

    def get_sqm_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns SQM configuration."""
        return self._client.request("GET", f"/sqm/config/{config_id}", params={"all_options": all_options})

    def update_sqm_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates SQM configuration."""
        return self._client.request("PUT", f"/sqm/config/{config_id}", json={"data": config})

    def delete_sqm_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes SQM configuration."""
        return self._client.request("DELETE", f"/sqm/config/{config_id}")

    def get_sqm_options(self) -> dict[str, Any]:
        """Returns SQM options."""
        return self._client.request("GET", "/sqm/options")
