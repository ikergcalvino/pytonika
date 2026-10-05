from typing import Any

from ._base import Endpoint


class APNDatabase(Endpoint):
    def get_apn_database_config(self) -> dict[str, Any]:
        """Returns multiple entries of APN database."""
        endpoint = "/apn_database/config"

        return self._client.request("GET", endpoint)

    def create_apn_database_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates entry in APN database."""
        endpoint = "/apn_database/config"

        data = {"data": config}

        return self._client.request("POST", endpoint, json=data)

    def update_apn_database_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates multiple entries of APN database."""
        endpoint = "/apn_database/config"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def delete_apn_database_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes multiple entries of APN database."""
        return [self.delete_apn_database_config_by_id(config_id) for config_id in config]

    def get_apn_database_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns specified entry of APN database."""
        endpoint = f"/apn_database/config/{config_id}"

        return self._client.request("GET", endpoint)

    def update_apn_database_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified entry of APN database."""
        endpoint = f"/apn_database/config/{config_id}"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def delete_apn_database_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified entry of APN database."""
        endpoint = f"/apn_database/config/{config_id}"

        return self._client.request("DELETE", endpoint)
