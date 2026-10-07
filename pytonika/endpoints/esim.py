from typing import Any

from ._endpoint import Endpoint


class eSIM(Endpoint):
    def esim_actions_clear_errors(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Clear eSIM errors."""
        return self._client.request("POST", "/esim/actions/clear_errors", json=None if data is None else {"data": data})

    def esim_actions_download(
        self, data: dict[str, Any] | None = None, *, switch_sim: str | None = None
    ) -> dict[str, Any]:
        """Downloads eSIM profile."""
        return self._client.request(
            "POST",
            "/esim/actions/download",
            params={"switch_sim": switch_sim},
            json=None if data is None else {"data": data},
        )

    def esim_actions_process_notifications(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Processes pending eSIM noitifications."""
        return self._client.request(
            "POST", "/esim/actions/process_notifications", json=None if data is None else {"data": data}
        )

    def get_esim_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns multiple eSIM configurations."""
        return self._client.request("GET", "/esim/config", params={"all_options": all_options})

    def update_esim_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates multiple eSIM configurations."""
        return self._client.request("PUT", "/esim/config", json={"data": config})

    def delete_esim_config(self, config: list[str], *, skip_switch: str | None = None) -> dict[str, Any]:
        """Deletes multiple eSIM configurations."""
        return self._client.request(
            "DELETE", "/esim/config", params={"skip_switch": skip_switch}, json={"data": config}
        )

    def get_esim_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified eSIM configuration."""
        return self._client.request("GET", f"/esim/config/{config_id}", params={"all_options": all_options})

    def update_esim_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified eSIM configuration."""
        return self._client.request("PUT", f"/esim/config/{config_id}", json={"data": config})

    def delete_esim_config_by_id(self, config_id: str, *, skip_switch: str | None = None) -> dict[str, Any]:
        """Deletes specified eSIM configuration."""
        return self._client.request("DELETE", f"/esim/config/{config_id}", params={"skip_switch": skip_switch})

    def get_esim_status(self) -> dict[str, Any]:
        """Returns multiple eSIM statuses."""
        return self._client.request("GET", "/esim/status")

    def get_esim_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Returns specified eSIM status."""
        return self._client.request("GET", f"/esim/status/{status_id}")
