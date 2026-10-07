from typing import Any

from ._endpoint import Endpoint


class ImpulseCounter(Endpoint):
    def impulse_counter_actions_clear_database(self) -> dict[str, Any]:
        """Clears collected count entries for all pins."""
        return self._client.request("POST", "/impulse_counter/actions/clear_database")

    def get_impulse_counter_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Impulse counter inputs configurations."""
        return self._client.request("GET", "/impulse_counter/config", params={"all_options": all_options})

    def create_impulse_counter_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Impulse counter input configuration."""
        return self._client.request("POST", "/impulse_counter/config", json={"data": config})

    def update_impulse_counter_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Impulse counter inputs configurations. If specified configuration is used as a data
        source for other service, updating it may invalidate configurations in data sources.
        """
        return self._client.request("PUT", "/impulse_counter/config", json={"data": config})

    def delete_impulse_counter_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified Impulse counter configurations. If specified configuration is used as a data source for
        other service, deleting it will invalidate configurations in data sources.
        """
        return self._client.request("DELETE", "/impulse_counter/config", json={"data": config})

    def get_impulse_counter_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified Impulse counter input configuration."""
        return self._client.request("GET", f"/impulse_counter/config/{config_id}", params={"all_options": all_options})

    def update_impulse_counter_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Impulse counter input configuration. If specified configuration is used as a data
        source for other service, updating it may invalidate configurations in data sources.
        """
        return self._client.request("PUT", f"/impulse_counter/config/{config_id}", json={"data": config})

    def delete_impulse_counter_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified Impulse counter input configuration. If specified configuration is used as a data
        source for other service, deleting it will invalidate configurations in data sources.
        """
        return self._client.request("DELETE", f"/impulse_counter/config/{config_id}")

    def get_impulse_counter_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get Impulse counter global configuration."""
        return self._client.request("GET", "/impulse_counter/global", params={"all_options": all_options})

    def update_impulse_counter_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Update Impulse counter global configuration."""
        return self._client.request("PUT", "/impulse_counter/global", json={"data": config})

    def get_impulse_counter_historic_status(self, *, filter: str | None = None) -> dict[str, Any]:
        """Returns database entries."""
        return self._client.request("GET", "/impulse_counter/historic/status", params={"filter": filter})

    def get_impulse_counter_status(self) -> dict[str, Any]:
        """Get Impulse counter General function status."""
        return self._client.request("GET", "/impulse_counter/status")
