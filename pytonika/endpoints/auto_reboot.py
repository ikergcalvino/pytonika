from typing import Any

from ._base import Endpoint


class AutoReboot(Endpoint):
    def get_auto_reboot_scheduler_config(self) -> dict[str, Any]:
        """Returns all Reboot Scheduler configurations."""
        endpoint = "/auto_reboot/scheduler/config"

        return self._api_client.get(endpoint)

    def create_auto_reboot_scheduler_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new Reboot Scheduler configuration."""
        endpoint = "/auto_reboot/scheduler/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_auto_reboot_scheduler_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Reboot Scheduler configurations."""
        endpoint = "/auto_reboot/scheduler/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_auto_reboot_scheduler_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes the selected Reboot Scheduler configurations."""
        return [self.delete_auto_reboot_scheduler_config_by_id(config_id) for config_id in config]

    def get_auto_reboot_scheduler_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the selected Reboot Scheduler configuration."""
        endpoint = f"/auto_reboot/scheduler/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_auto_reboot_scheduler_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected Reboot Scheduler configuration."""
        endpoint = f"/auto_reboot/scheduler/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_auto_reboot_scheduler_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the selected Reboot Scheduler configuration."""
        endpoint = f"/auto_reboot/scheduler/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_auto_reboot_ping_wget_config(self) -> dict[str, Any]:
        """Returns all Ping/Wget Reboot configurations."""
        endpoint = "/auto_reboot/ping_wget/config"

        return self._api_client.get(endpoint)

    def create_auto_reboot_ping_wget_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new Ping/Wget Reboot configuration."""
        endpoint = "/auto_reboot/ping_wget/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_auto_reboot_ping_wget_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Ping/Wget Reboot configurations."""
        endpoint = "/auto_reboot/ping_wget/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_auto_reboot_ping_wget_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes the selected Ping/Wget Reboot configurations."""
        return [self.delete_auto_reboot_ping_wget_config_by_id(config_id) for config_id in config]

    def get_auto_reboot_ping_wget_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the selected Ping/Wget Reboot configuration."""
        endpoint = f"/auto_reboot/ping_wget/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_auto_reboot_ping_wget_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected Ping/Wget Reboot configuration."""
        endpoint = f"/auto_reboot/ping_wget/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_auto_reboot_ping_wget_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the selected Ping/Wget Reboot configuration."""
        endpoint = f"/auto_reboot/ping_wget/config/{config_id}"

        return self._api_client.delete(endpoint)
