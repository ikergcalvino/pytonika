from typing import Any

from ._base import Endpoint


class ImpulseCounter(Endpoint):
    def get_impulse_counter_config(self) -> dict[str, Any]:
        """Returns all Impulse counter inputs configurations."""
        endpoint = "/impulse_counter/config"

        return self._api_client.get(endpoint)

    def create_impulse_counter_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Impulse counter input configuration."""
        endpoint = "/impulse_counter/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_impulse_counter_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Impulse counter inputs configurations."""
        endpoint = "/impulse_counter/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_impulse_counter_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified Impulse counter configurations."""
        return [self.delete_impulse_counter_config_by_id(config_id) for config_id in config]

    def get_impulse_counter_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified Impulse counter input configuration."""
        endpoint = f"/impulse_counter/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_impulse_counter_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Impulse counter input configuration."""
        endpoint = f"/impulse_counter/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_impulse_counter_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified Impulse counter input configuration."""
        endpoint = f"/impulse_counter/config/{config_id}"

        return self._api_client.delete(endpoint)

    def impulse_counter_actions_clear_database(self) -> dict[str, Any]:
        """Clears collected count entries for all pins."""
        endpoint = "/impulse_counter/actions/clear_database"

        return self._api_client.post(endpoint)

    def get_impulse_counter_historic_status(self) -> dict[str, Any]:
        """Returns database entries."""
        endpoint = "/impulse_counter/historic/status"

        return self._api_client.get(endpoint)

    def get_impulse_counter_global(self) -> dict[str, Any]:
        """Get Impulse counter global configuration."""
        endpoint = "/impulse_counter/global"

        return self._api_client.get(endpoint)

    def update_impulse_counter_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Update Impulse counter global configuration."""
        endpoint = "/impulse_counter/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_impulse_counter_status(self) -> dict[str, Any]:
        """Get Impulse counter General function status."""
        endpoint = "/impulse_counter/status"

        return self._api_client.get(endpoint)
