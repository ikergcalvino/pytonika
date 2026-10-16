from typing import Any

from ._endpoint import Endpoint


class ITxPT(Endpoint):
    def get_itxpt_global(self) -> dict[str, Any]:
        """Returns all ITxPT configurations."""
        return self._client.request("GET", "/itxpt/global")

    def update_itxpt_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified ITxPT configurations."""
        return self._client.request("PUT", "/itxpt/global", json={"data": config})

    def get_itxpt_services_config(self) -> dict[str, Any]:
        """Returns all ITxPT service configurations."""
        return self._client.request("GET", "/itxpt/services/config")

    def update_itxpt_services_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified ITxPT service configurations."""
        return self._client.request("PUT", "/itxpt/services/config", json={"data": config})

    def get_itxpt_services_config_by_id(self, service_id: str) -> dict[str, Any]:
        """Returns the specified ITxPT service configuration."""
        return self._client.request("GET", f"/itxpt/services/config/{service_id}")

    def update_itxpt_services_config_by_id(self, service_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified ITxPT service configuration."""
        return self._client.request("PUT", f"/itxpt/services/config/{service_id}", json={"data": config})
