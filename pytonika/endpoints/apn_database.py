from typing import Any

from ._endpoint import Endpoint


class APNDatabase(Endpoint):
    def get_apn_database_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns multiple entries of APN database."""
        return self._client.request("GET", "/apn_database/config", params={"all_options": all_options})

    def create_apn_database_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates entry in APN database."""
        return self._client.request("POST", "/apn_database/config", json={"data": config})

    def update_apn_database_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates multiple entries of APN database."""
        return self._client.request("PUT", "/apn_database/config", json={"data": config})

    def delete_apn_database_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes multiple entries of APN database."""
        return self._client.request("DELETE", "/apn_database/config", json={"data": config})

    def get_apn_database_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified entry of APN database."""
        return self._client.request("GET", f"/apn_database/config/{config_id}", params={"all_options": all_options})

    def update_apn_database_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified entry of APN database."""
        return self._client.request("PUT", f"/apn_database/config/{config_id}", json={"data": config})

    def delete_apn_database_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified entry of APN database."""
        return self._client.request("DELETE", f"/apn_database/config/{config_id}")
