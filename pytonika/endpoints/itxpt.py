from typing import Any

from ._base import Endpoint


class ITxPT(Endpoint):
    def get_itxpt_global(self) -> dict[str, Any]:
        """Returns all ITxPT configurations."""
        endpoint = "/itxpt/global"

        return self._api_client.get(endpoint)

    def update_itxpt_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified ITxPT configurations."""
        endpoint = "/itxpt/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_itxpt_services_config(self) -> dict[str, Any]:
        """Returns all ITxPT service configurations."""
        endpoint = "/itxpt/services/config"

        return self._api_client.get(endpoint)

    def update_itxpt_services_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified ITxPT service configurations."""
        endpoint = "/itxpt/services/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_itxpt_services_config_by_id(self, service_id: str) -> dict[str, Any]:
        """Returns the specified ITxPT service configuration."""
        endpoint = f"/itxpt/services/config/{service_id}"

        return self._api_client.get(endpoint)

    def update_itxpt_services_config_by_id(self, service_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified ITxPT service configuration."""
        endpoint = f"/itxpt/services/config/{service_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
