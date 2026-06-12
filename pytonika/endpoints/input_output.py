from typing import Any

from ._base import Endpoint


class InputOutput(Endpoint):
    def get_io_scheduler_global(self) -> dict[str, Any]:
        """Returns the general I/O Scheduler configuration."""
        endpoint = "/io/scheduler/global"

        return self._api_client.get(endpoint)

    def update_io_scheduler_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the general I/O Scheduler configuration."""
        endpoint = "/io/scheduler/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_io_scheduler_config(self) -> dict[str, Any]:
        """Returns all I/O Scheduler Instance configurations."""
        endpoint = "/io/scheduler/config"

        return self._api_client.get(endpoint)

    def create_io_scheduler_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new I/O Scheduler Instance configuration."""
        endpoint = "/io/scheduler/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_io_scheduler_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the specified I/O Scheduler Instance configurations."""
        endpoint = "/io/scheduler/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_io_scheduler_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes the specified I/O Scheduler Instance configurations."""
        return [self.delete_io_scheduler_config_by_id(instance_id) for instance_id in config]

    def get_io_scheduler_config_by_id(self, instance_id: str) -> dict[str, Any]:
        """Returns the specified I/O Scheduler Instance configuration."""
        endpoint = f"/io/scheduler/config/{instance_id}"

        return self._api_client.get(endpoint)

    def update_io_scheduler_config_by_id(self, instance_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified I/O Scheduler Instance configuration."""
        endpoint = f"/io/scheduler/config/{instance_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_io_scheduler_config_by_id(self, instance_id: str) -> dict[str, Any]:
        """Deletes the specified I/O Scheduler Instance configuration."""
        endpoint = f"/io/scheduler/config/{instance_id}"

        return self._api_client.delete(endpoint)

    def get_io_juggler_conditions_config(self) -> dict[str, Any]:
        """Deprecated. Returns all I/O Juggler Condition configurations."""
        endpoint = "/io/juggler/conditions/config"

        return self._api_client.get(endpoint)

    def create_io_juggler_conditions_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Deprecated. Creates a new I/O Juggler Condition configuration."""
        endpoint = "/io/juggler/conditions/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_io_juggler_conditions_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Deprecated. Updates the specified I/O Juggler Condition configurations."""
        endpoint = "/io/juggler/conditions/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_io_juggler_conditions_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deprecated. Deletes the specified I/O Juggler Condition configurations."""
        return [self.delete_io_juggler_conditions_config_by_id(condition_id) for condition_id in config]

    def get_io_juggler_conditions_config_by_id(self, condition_id: str) -> dict[str, Any]:
        """Deprecated. Returns the specified I/O Juggler Condition configuration."""
        endpoint = f"/io/juggler/conditions/config/{condition_id}"

        return self._api_client.get(endpoint)

    def update_io_juggler_conditions_config_by_id(self, condition_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Deprecated. Updates the specified I/O Juggler Condition configuration."""
        endpoint = f"/io/juggler/conditions/config/{condition_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_io_juggler_conditions_config_by_id(self, condition_id: str) -> dict[str, Any]:
        """Deprecated. Deletes the specified I/O Juggler Condition configuration."""
        endpoint = f"/io/juggler/conditions/config/{condition_id}"

        return self._api_client.delete(endpoint)

    def get_io_juggler_global(self) -> dict[str, Any]:
        """Deprecated. Returns general I/O Juggler configuration."""
        endpoint = "/io/juggler/global"

        return self._api_client.get(endpoint)

    def update_io_juggler_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Deprecated. Updates general I/O Juggler configuration."""
        endpoint = "/io/juggler/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_io_juggler_operations_options(self) -> dict[str, Any]:
        """Deprecated. Returns options needed for I/O juggler action configuration."""
        endpoint = "/io/juggler/operations/options"

        return self._api_client.get(endpoint)

    def get_io_juggler_operations_config(self) -> dict[str, Any]:
        """Deprecated. Returns all I/O Juggler Action configurations."""
        endpoint = "/io/juggler/operations/config"

        return self._api_client.get(endpoint)

    def create_io_juggler_operations_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Deprecated. Creates a new I/O Juggler Action configuration."""
        endpoint = "/io/juggler/operations/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_io_juggler_operations_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Deprecated. Updates the specified I/O Juggler Action configurations."""
        endpoint = "/io/juggler/operations/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_io_juggler_operations_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deprecated. Deletes the specified I/O Juggler Action configurations."""
        return [self.delete_io_juggler_operations_config_by_id(operation_id) for operation_id in config]

    def get_io_juggler_operations_config_by_id(self, operation_id: str) -> dict[str, Any]:
        """Deprecated. Returns the specified I/O Juggler Action configuration."""
        endpoint = f"/io/juggler/operations/config/{operation_id}"

        return self._api_client.get(endpoint)

    def upload_io_juggler_operations_config_by_id(self, operation_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Deprecated. Uploads I/O Juggler Action certificate files or script file."""
        endpoint = f"/io/juggler/operations/config/{operation_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_io_juggler_operations_config_by_id(self, operation_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Deprecated. Updates the specified I/O Juggler Action configuration."""
        endpoint = f"/io/juggler/operations/config/{operation_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_io_juggler_operations_config_by_id(self, operation_id: str) -> dict[str, Any]:
        """Deprecated. Deletes the specified I/O Juggler Action configuration."""
        endpoint = f"/io/juggler/operations/config/{operation_id}"

        return self._api_client.delete(endpoint)

    def get_io_juggler_inputs_config(self) -> dict[str, Any]:
        """Deprecated. Returns all I/O Juggler Input configurations."""
        endpoint = "/io/juggler/inputs/config"

        return self._api_client.get(endpoint)

    def create_io_juggler_inputs_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Deprecated. Creates a new I/O Juggler Input configuration."""
        endpoint = "/io/juggler/inputs/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_io_juggler_inputs_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Deprecated. Updates the specified I/O Juggler Input configurations."""
        endpoint = "/io/juggler/inputs/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_io_juggler_inputs_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deprecated. Deletes the specified I/O Juggler Input configurations."""
        return [self.delete_io_juggler_inputs_config_by_id(input_id) for input_id in config]

    def get_io_juggler_inputs_config_by_id(self, input_id: str) -> dict[str, Any]:
        """Deprecated. Returns the specified I/O Juggler Input configuration."""
        endpoint = f"/io/juggler/inputs/config/{input_id}"

        return self._api_client.get(endpoint)

    def update_io_juggler_inputs_config_by_id(self, input_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Deprecated. Updates the specified I/O Juggler Input configuration."""
        endpoint = f"/io/juggler/inputs/config/{input_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_io_juggler_inputs_config_by_id(self, input_id: str) -> dict[str, Any]:
        """Deprecated. Deletes the specified I/O Juggler Input configuration."""
        endpoint = f"/io/juggler/inputs/config/{input_id}"

        return self._api_client.delete(endpoint)

    def get_io_status(self) -> dict[str, Any]:
        """Returns all I/O Status pin configurations."""
        endpoint = "/io/status"

        return self._api_client.get(endpoint)

    def get_io_status_by_id(self, io_id: str) -> dict[str, Any]:
        """Returns the specified I/O Status pin configuration."""
        endpoint = f"/io/{io_id}/status"

        return self._api_client.get(endpoint)

    def io_actions_change_state(self, io_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified I/O Status pin configuration."""
        endpoint = f"/io/{io_id}/actions/change_state"

        return self._api_client.post(endpoint, data={"data": data})
