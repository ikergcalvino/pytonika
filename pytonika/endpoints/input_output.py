from typing import Any, Literal

from ._endpoint import Endpoint, File


class InputOutput(Endpoint):
    def get_io_config(self) -> dict[str, Any]:
        """Returns all I/O pin configurations."""
        return self._client.request("GET", "/io/config")

    def update_io_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected I/O pin configurations."""
        return self._client.request("PUT", "/io/config", json={"data": config})

    def get_io_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified I/O pin configuration."""
        return self._client.request("GET", f"/io/config/{config_id}")

    def update_io_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified I/O pin configuration."""
        return self._client.request("PUT", f"/io/config/{config_id}", json={"data": config})

    def get_io_juggler_conditions_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all I/O Juggler Condition configurations."""
        return self._client.request("GET", "/io/juggler/conditions/config", params={"all_options": all_options})

    def create_io_juggler_conditions_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new I/O Juggler Condition configuration."""
        return self._client.request("POST", "/io/juggler/conditions/config", json={"data": config})

    def update_io_juggler_conditions_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the specified I/O Juggler Condition configurations."""
        return self._client.request("PUT", "/io/juggler/conditions/config", json={"data": config})

    def delete_io_juggler_conditions_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the specified I/O Juggler Condition configurations."""
        return self._client.request("DELETE", "/io/juggler/conditions/config", json={"data": config})

    def get_io_juggler_conditions_config_by_id(
        self, condition_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified I/O Juggler Condition configuration."""
        return self._client.request(
            "GET", f"/io/juggler/conditions/config/{condition_id}", params={"all_options": all_options}
        )

    def update_io_juggler_conditions_config_by_id(self, condition_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified I/O Juggler Condition configuration."""
        return self._client.request("PUT", f"/io/juggler/conditions/config/{condition_id}", json={"data": config})

    def delete_io_juggler_conditions_config_by_id(self, condition_id: str) -> dict[str, Any]:
        """Deletes the specified I/O Juggler Condition configuration."""
        return self._client.request("DELETE", f"/io/juggler/conditions/config/{condition_id}")

    def get_io_juggler_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns general I/O Juggler configuration."""
        return self._client.request("GET", "/io/juggler/global", params={"all_options": all_options})

    def update_io_juggler_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates general I/O Juggler configuration."""
        return self._client.request("PUT", "/io/juggler/global", json={"data": config})

    def get_io_juggler_inputs_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all I/O Juggler Input configurations."""
        return self._client.request("GET", "/io/juggler/inputs/config", params={"all_options": all_options})

    def create_io_juggler_inputs_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new I/O Juggler Input configuration."""
        return self._client.request("POST", "/io/juggler/inputs/config", json={"data": config})

    def update_io_juggler_inputs_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the specified I/O Juggler Input configurations."""
        return self._client.request("PUT", "/io/juggler/inputs/config", json={"data": config})

    def delete_io_juggler_inputs_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the specified I/O Juggler Input configurations."""
        return self._client.request("DELETE", "/io/juggler/inputs/config", json={"data": config})

    def get_io_juggler_inputs_config_by_id(self, input_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified I/O Juggler Input configuration."""
        return self._client.request("GET", f"/io/juggler/inputs/config/{input_id}", params={"all_options": all_options})

    def update_io_juggler_inputs_config_by_id(self, input_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified I/O Juggler Input configuration."""
        return self._client.request("PUT", f"/io/juggler/inputs/config/{input_id}", json={"data": config})

    def delete_io_juggler_inputs_config_by_id(self, input_id: str) -> dict[str, Any]:
        """Deletes the specified I/O Juggler Input configuration."""
        return self._client.request("DELETE", f"/io/juggler/inputs/config/{input_id}")

    def get_io_juggler_operations_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all I/O Juggler Action configurations."""
        return self._client.request("GET", "/io/juggler/operations/config", params={"all_options": all_options})

    def create_io_juggler_operations_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new I/O Juggler Action configuration."""
        return self._client.request("POST", "/io/juggler/operations/config", json={"data": config})

    def update_io_juggler_operations_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the specified I/O Juggler Action configurations."""
        return self._client.request("PUT", "/io/juggler/operations/config", json={"data": config})

    def delete_io_juggler_operations_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the specified I/O Juggler Action configurations."""
        return self._client.request("DELETE", "/io/juggler/operations/config", json={"data": config})

    def get_io_juggler_operations_config_by_id(
        self, operation_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified I/O Juggler Action configuration."""
        return self._client.request(
            "GET", f"/io/juggler/operations/config/{operation_id}", params={"all_options": all_options}
        )

    def upload_io_juggler_operations_config_by_id(
        self, operation_id: str, file: File, *, option: Literal["cafile", "certfile", "keyfile", "upload"] | None = None
    ) -> dict[str, Any]:
        """Uploads I/O Juggler Action certificate files or script file."""
        return self._client.request(
            "POST", f"/io/juggler/operations/config/{operation_id}", files={"file": file}, form={"option": option}
        )

    def update_io_juggler_operations_config_by_id(self, operation_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified I/O Juggler Action configuration."""
        return self._client.request("PUT", f"/io/juggler/operations/config/{operation_id}", json={"data": config})

    def delete_io_juggler_operations_config_by_id(self, operation_id: str) -> dict[str, Any]:
        """Deletes the specified I/O Juggler Action configuration."""
        return self._client.request("DELETE", f"/io/juggler/operations/config/{operation_id}")

    def get_io_juggler_operations_options(self) -> dict[str, Any]:
        """Returns options needed for I/O juggler action configuration."""
        return self._client.request("GET", "/io/juggler/operations/options")

    def get_io_post_get_config(self) -> dict[str, Any]:
        """Returns the I/O Post/Get configuration in an array."""
        return self._client.request("GET", "/io/post_get/config")

    def update_io_post_get_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the I/O Post/Get configuration in an array."""
        return self._client.request("PUT", "/io/post_get/config", json={"data": config})

    def get_io_post_get_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the I/O Post/Get configuration."""
        return self._client.request("GET", f"/io/post_get/config/{config_id}")

    def update_io_post_get_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the I/O Post/Get configuration."""
        return self._client.request("PUT", f"/io/post_get/config/{config_id}", json={"data": config})

    def get_io_scheduler_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all I/O Scheduler Instance configurations."""
        return self._client.request("GET", "/io/scheduler/config", params={"all_options": all_options})

    def create_io_scheduler_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new I/O Scheduler Instance configuration."""
        return self._client.request("POST", "/io/scheduler/config", json={"data": config})

    def update_io_scheduler_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the specified I/O Scheduler Instance configurations."""
        return self._client.request("PUT", "/io/scheduler/config", json={"data": config})

    def delete_io_scheduler_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the specified I/O Scheduler Instance configurations."""
        return self._client.request("DELETE", "/io/scheduler/config", json={"data": config})

    def get_io_scheduler_config_by_id(self, instance_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified I/O Scheduler Instance configuration."""
        return self._client.request("GET", f"/io/scheduler/config/{instance_id}", params={"all_options": all_options})

    def update_io_scheduler_config_by_id(self, instance_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified I/O Scheduler Instance configuration."""
        return self._client.request("PUT", f"/io/scheduler/config/{instance_id}", json={"data": config})

    def delete_io_scheduler_config_by_id(self, instance_id: str) -> dict[str, Any]:
        """Deletes the specified I/O Scheduler Instance configuration."""
        return self._client.request("DELETE", f"/io/scheduler/config/{instance_id}")

    def get_io_scheduler_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the general I/O Scheduler configuration."""
        return self._client.request("GET", "/io/scheduler/global", params={"all_options": all_options})

    def update_io_scheduler_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the general I/O Scheduler configuration."""
        return self._client.request("PUT", "/io/scheduler/global", json={"data": config})

    def get_io_status(self) -> dict[str, Any]:
        """Returns all I/O Status pin configurations."""
        return self._client.request("GET", "/io/status")

    def io_actions_change_state(self, io_id: str, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Updates the specified I/O Status pin configuration."""
        return self._client.request(
            "POST", f"/io/{io_id}/actions/change_state", json=None if data is None else {"data": data}
        )

    def get_io_status_by_id(self, io_id: str) -> dict[str, Any]:
        """Returns the specified I/O Status pin configuration."""
        return self._client.request("GET", f"/io/{io_id}/status")
