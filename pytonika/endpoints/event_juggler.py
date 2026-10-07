from typing import Any

from ._endpoint import Endpoint, File


class EventJuggler(Endpoint):
    def event_juggler_conditions_actions_download_example_condition_lua(self) -> bytes | dict[str, Any]:
        """Downloads Lua script example file."""
        return self._client.request(
            "POST", "/event_juggler/conditions/actions/download_example_condition_lua", download=True
        )

    def get_event_juggler_conditions_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Event Juggler service condition configurations."""
        return self._client.request("GET", "/event_juggler/conditions/config", params={"all_options": all_options})

    def update_event_juggler_conditions_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Event Juggler condition configurations."""
        return self._client.request("PUT", "/event_juggler/conditions/config", json={"data": config})

    def delete_event_juggler_conditions_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the selected Event Juggler condition configurations."""
        return self._client.request("DELETE", "/event_juggler/conditions/config", json={"data": config})

    def get_event_juggler_conditions_config_by_id(
        self, condition_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified Event Juggler service condition configuration."""
        return self._client.request(
            "GET", f"/event_juggler/conditions/config/{condition_id}", params={"all_options": all_options}
        )

    def upload_event_juggler_conditions_config_by_id(
        self, condition_id: str, file: File, *, option: str | None = None
    ) -> dict[str, Any]:
        """Uploads the Condition necessary files."""
        return self._client.request(
            "POST", f"/event_juggler/conditions/config/{condition_id}", files={"file": file}, form={"option": option}
        )

    def update_event_juggler_conditions_config_by_id(self, condition_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Event Juggler service condition configuration."""
        return self._client.request("PUT", f"/event_juggler/conditions/config/{condition_id}", json={"data": config})

    def delete_event_juggler_conditions_config_by_id(self, condition_id: str) -> dict[str, Any]:
        """Deletes the specified Event Juggler service condition configuration."""
        return self._client.request("DELETE", f"/event_juggler/conditions/config/{condition_id}")

    def get_event_juggler_conditions_options(self) -> dict[str, Any]:
        """Returns Event Juggler conditions options."""
        return self._client.request("GET", "/event_juggler/conditions/options")

    def get_event_juggler_events_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Event Juggler service event configurations."""
        return self._client.request("GET", "/event_juggler/events/config", params={"all_options": all_options})

    def create_event_juggler_events_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new Event Juggler service event configuration with one automatically created action."""
        return self._client.request("POST", "/event_juggler/events/config", json={"data": config})

    def update_event_juggler_events_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Event Juggler events configurations."""
        return self._client.request("PUT", "/event_juggler/events/config", json={"data": config})

    def delete_event_juggler_events_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the selected Event Juggler event configurations."""
        return self._client.request("DELETE", "/event_juggler/events/config", json={"data": config})

    def get_event_juggler_events_config_by_id(
        self, event_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified Event Juggler service event configuration."""
        return self._client.request(
            "GET", f"/event_juggler/events/config/{event_id}", params={"all_options": all_options}
        )

    def update_event_juggler_events_config_by_id(self, event_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Event Juggler service event configuration."""
        return self._client.request("PUT", f"/event_juggler/events/config/{event_id}", json={"data": config})

    def delete_event_juggler_events_config_by_id(self, event_id: str) -> dict[str, Any]:
        """Deletes the specified Event Juggler service event configuration."""
        return self._client.request("DELETE", f"/event_juggler/events/config/{event_id}")

    def get_event_juggler_events_options(self) -> dict[str, Any]:
        """Returns Event Juggler events options."""
        return self._client.request("GET", "/event_juggler/events/options")

    def get_event_juggler_events_conditions_config(self, events_id: str) -> dict[str, Any]:
        """Returns all Event Juggler service condition configurations associated with the specified event."""
        return self._client.request("GET", f"/event_juggler/events/{events_id}/conditions/config")

    def create_event_juggler_events_conditions_config(
        self, event_id: str, config: dict[str, Any], *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Creates a new Event Juggler service condition configuration."""
        return self._client.request(
            "POST",
            f"/event_juggler/events/{event_id}/conditions/config",
            params={"all_options": all_options},
            json={"data": config},
        )

    def update_event_juggler_events_conditions_config(
        self, events_id: str, config: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """Updates the selected Event Juggler condition configurations associated with the specified event."""
        return self._client.request(
            "PUT", f"/event_juggler/events/{events_id}/conditions/config", json={"data": config}
        )

    def delete_event_juggler_events_conditions_config(self, events_id: str, config: list[str]) -> dict[str, Any]:
        """Deletes the selected Event Juggler condition configurations associated with the specified event."""
        return self._client.request(
            "DELETE", f"/event_juggler/events/{events_id}/conditions/config", json={"data": config}
        )

    def get_event_juggler_events_operations_config(
        self, events_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns all Event Juggler service action configurations associated with the specified event."""
        return self._client.request(
            "GET", f"/event_juggler/events/{events_id}/operations/config", params={"all_options": all_options}
        )

    def create_event_juggler_events_operations_config(self, event_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new Event Juggler service action configuration."""
        return self._client.request(
            "POST", f"/event_juggler/events/{event_id}/operations/config", json={"data": config}
        )

    def update_event_juggler_events_operations_config(
        self, events_id: str, config: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """Updates the selected Event Juggler action configurations associated with the specified event."""
        return self._client.request(
            "PUT", f"/event_juggler/events/{events_id}/operations/config", json={"data": config}
        )

    def delete_event_juggler_events_operations_config(self, events_id: str, config: list[str]) -> dict[str, Any]:
        """Deletes the selected Event Juggler action configurations associated with the specified event."""
        return self._client.request(
            "DELETE", f"/event_juggler/events/{events_id}/operations/config", json={"data": config}
        )

    def event_juggler_operations_actions_download_example_operation_lua(self) -> bytes | dict[str, Any]:
        """Downloads Lua script example file."""
        return self._client.request(
            "POST", "/event_juggler/operations/actions/download_example_operation_lua", download=True
        )

    def get_event_juggler_operations_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Event Juggler service action configurations."""
        return self._client.request("GET", "/event_juggler/operations/config", params={"all_options": all_options})

    def update_event_juggler_operations_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Event Juggler action configurations."""
        return self._client.request("PUT", "/event_juggler/operations/config", json={"data": config})

    def delete_event_juggler_operations_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the selected Event Juggler action configurations."""
        return self._client.request("DELETE", "/event_juggler/operations/config", json={"data": config})

    def get_event_juggler_operations_config_by_id(
        self, operation_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified Event Juggler service action configuration."""
        return self._client.request(
            "GET", f"/event_juggler/operations/config/{operation_id}", params={"all_options": all_options}
        )

    def upload_event_juggler_operations_config_by_id(
        self, operation_id: str, file: File, *, option: str | None = None
    ) -> dict[str, Any]:
        """Uploads the Action necessary files."""
        return self._client.request(
            "POST", f"/event_juggler/operations/config/{operation_id}", files={"file": file}, form={"option": option}
        )

    def update_event_juggler_operations_config_by_id(self, operation_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Event Juggler service action configuration."""
        return self._client.request("PUT", f"/event_juggler/operations/config/{operation_id}", json={"data": config})

    def delete_event_juggler_operations_config_by_id(self, operation_id: str) -> dict[str, Any]:
        """Deletes the specified Event Juggler service action configuration."""
        return self._client.request("DELETE", f"/event_juggler/operations/config/{operation_id}")

    def get_event_juggler_operations_options(self) -> dict[str, Any]:
        """Returns Event Juggler actions options."""
        return self._client.request("GET", "/event_juggler/operations/options")
