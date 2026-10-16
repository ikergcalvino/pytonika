from typing import Any

from ._endpoint import Endpoint


class AutoReboot(Endpoint):
    def get_auto_reboot_ping_wget_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Ping/Wget Reboot configurations."""
        return self._client.request("GET", "/auto_reboot/ping_wget/config", params={"all_options": all_options})

    def create_auto_reboot_ping_wget_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new Ping/Wget Reboot configuration."""
        return self._client.request("POST", "/auto_reboot/ping_wget/config", json={"data": config})

    def update_auto_reboot_ping_wget_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Ping/Wget Reboot configurations."""
        return self._client.request("PUT", "/auto_reboot/ping_wget/config", json={"data": config})

    def delete_auto_reboot_ping_wget_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the selected Ping/Wget Reboot configurations."""
        return self._client.request("DELETE", "/auto_reboot/ping_wget/config", json={"data": config})

    def get_auto_reboot_ping_wget_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the selected Ping/Wget Reboot configuration."""
        return self._client.request(
            "GET", f"/auto_reboot/ping_wget/config/{config_id}", params={"all_options": all_options}
        )

    def update_auto_reboot_ping_wget_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected Ping/Wget Reboot configuration."""
        return self._client.request("PUT", f"/auto_reboot/ping_wget/config/{config_id}", json={"data": config})

    def delete_auto_reboot_ping_wget_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the selected Ping/Wget Reboot configuration."""
        return self._client.request("DELETE", f"/auto_reboot/ping_wget/config/{config_id}")

    def get_auto_reboot_ping_wget_options(self) -> dict[str, Any]:
        """Returns Ping/Wget Reboot options."""
        return self._client.request("GET", "/auto_reboot/ping_wget/options")

    def get_auto_reboot_scheduler_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Reboot Scheduler configurations."""
        return self._client.request("GET", "/auto_reboot/scheduler/config", params={"all_options": all_options})

    def create_auto_reboot_scheduler_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new Reboot Scheduler configuration."""
        return self._client.request("POST", "/auto_reboot/scheduler/config", json={"data": config})

    def update_auto_reboot_scheduler_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Reboot Scheduler configurations."""
        return self._client.request("PUT", "/auto_reboot/scheduler/config", json={"data": config})

    def delete_auto_reboot_scheduler_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the selected Reboot Scheduler configurations."""
        return self._client.request("DELETE", "/auto_reboot/scheduler/config", json={"data": config})

    def get_auto_reboot_scheduler_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the selected Reboot Scheduler configuration."""
        return self._client.request(
            "GET", f"/auto_reboot/scheduler/config/{config_id}", params={"all_options": all_options}
        )

    def update_auto_reboot_scheduler_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected Reboot Scheduler configuration."""
        return self._client.request("PUT", f"/auto_reboot/scheduler/config/{config_id}", json={"data": config})

    def delete_auto_reboot_scheduler_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the selected Reboot Scheduler configuration."""
        return self._client.request("DELETE", f"/auto_reboot/scheduler/config/{config_id}")
