from typing import Any

from ._base import Endpoint


class EventJuggler(Endpoint):
    def get_event_juggler_events_options(self) -> dict[str, Any]:
        """Returns Event Juggler events options."""
        endpoint = "/event_juggler/events/options"

        return self._api_client.get(endpoint)

    def get_event_juggler_events_config(self) -> dict[str, Any]:
        """Returns all Event Juggler service event configurations."""
        endpoint = "/event_juggler/events/config"

        return self._api_client.get(endpoint)

    def create_event_juggler_events_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new Event Juggler service event configuration with one automatically created action."""
        endpoint = "/event_juggler/events/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_event_juggler_events_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Event Juggler events configurations."""
        endpoint = "/event_juggler/events/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_event_juggler_events_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes the selected Event Juggler event configurations."""
        return [self.delete_event_juggler_events_config_by_id(event_id) for event_id in config]

    def get_event_juggler_events_config_by_id(self, event_id: str) -> dict[str, Any]:
        """Returns the specified Event Juggler service event configuration."""
        endpoint = f"/event_juggler/events/config/{event_id}"

        return self._api_client.get(endpoint)

    def update_event_juggler_events_config_by_id(self, event_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Event Juggler service event configuration."""
        endpoint = f"/event_juggler/events/config/{event_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_event_juggler_events_config_by_id(self, event_id: str) -> dict[str, Any]:
        """Deletes the specified Event Juggler service event configuration."""
        endpoint = f"/event_juggler/events/config/{event_id}"

        return self._api_client.delete(endpoint)

    def get_event_juggler_operations_options(self) -> dict[str, Any]:
        """Returns Event Juggler actions options."""
        endpoint = "/event_juggler/operations/options"

        return self._api_client.get(endpoint)

    def create_event_juggler_operations_config(self, event_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new Event Juggler service action configuration."""
        endpoint = f"/event_juggler/events/{event_id}/operations/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def get_event_juggler_operations_config(self) -> dict[str, Any]:
        """Returns all Event Juggler service action configurations."""
        endpoint = "/event_juggler/operations/config"

        return self._api_client.get(endpoint)

    def update_event_juggler_operations_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Event Juggler action configurations."""
        endpoint = "/event_juggler/operations/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_event_juggler_operations_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes the selected Event Juggler action configurations."""
        return [self.delete_event_juggler_operations_config_by_id(op_id) for op_id in config]

    def get_event_juggler_operations_config_by_id(self, operation_id: str) -> dict[str, Any]:
        """Returns the specified Event Juggler service action configuration."""
        endpoint = f"/event_juggler/operations/config/{operation_id}"

        return self._api_client.get(endpoint)

    def upload_event_juggler_operations_files(self, operation_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads the Action necessary files."""
        endpoint = f"/event_juggler/operations/config/{operation_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_event_juggler_operations_config_by_id(self, operation_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Event Juggler service action configuration."""
        endpoint = f"/event_juggler/operations/config/{operation_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_event_juggler_operations_config_by_id(self, operation_id: str) -> dict[str, Any]:
        """Deletes the specified Event Juggler service action configuration."""
        endpoint = f"/event_juggler/operations/config/{operation_id}"

        return self._api_client.delete(endpoint)

    def download_example_operation_lua(self, data: dict[str, Any]) -> dict[str, Any]:
        """Downloads Lua script example file."""
        endpoint = "/event_juggler/operations/actions/download_example_operation_lua"

        return self._api_client.post(endpoint, data={"data": data})

    def get_event_juggler_conditions_options(self) -> dict[str, Any]:
        """Returns Event Juggler conditions options."""
        endpoint = "/event_juggler/conditions/options"

        return self._api_client.get(endpoint)

    def create_event_juggler_conditions_config(self, event_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new Event Juggler service condition configuration."""
        endpoint = f"/event_juggler/events/{event_id}/conditions/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def get_event_juggler_conditions_config(self) -> dict[str, Any]:
        """Returns all Event Juggler service condition configurations."""
        endpoint = "/event_juggler/conditions/config"

        return self._api_client.get(endpoint)

    def update_event_juggler_conditions_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Event Juggler condition configurations."""
        endpoint = "/event_juggler/conditions/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_event_juggler_conditions_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes the selected Event Juggler condition configurations."""
        return [self.delete_event_juggler_conditions_config_by_id(cond_id) for cond_id in config]

    def get_event_juggler_conditions_config_by_id(self, condition_id: str) -> dict[str, Any]:
        """Returns the specified Event Juggler service condition configuration."""
        endpoint = f"/event_juggler/conditions/config/{condition_id}"

        return self._api_client.get(endpoint)

    def upload_event_juggler_conditions_files(self, condition_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads the Condition necessary files."""
        endpoint = f"/event_juggler/conditions/config/{condition_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_event_juggler_conditions_config_by_id(self, condition_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Event Juggler service condition configuration."""
        endpoint = f"/event_juggler/conditions/config/{condition_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_event_juggler_conditions_config_by_id(self, condition_id: str) -> dict[str, Any]:
        """Deletes the specified Event Juggler service condition configuration."""
        endpoint = f"/event_juggler/conditions/config/{condition_id}"

        return self._api_client.delete(endpoint)

    def download_example_condition_lua(self, data: dict[str, Any]) -> dict[str, Any]:
        """Downloads Lua script example file."""
        endpoint = "/event_juggler/conditions/actions/download_example_condition_lua"

        return self._api_client.post(endpoint, data={"data": data})
