from typing import Any

from ._endpoint import Endpoint


class Messages(Endpoint):
    def messages_actions_remove_messages(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Deletes the selected SMS Messages."""
        return self._client.request(
            "POST", "/messages/actions/remove_messages", json=None if data is None else {"data": data}
        )

    def messages_actions_send(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Sends SMS message."""
        return self._client.request("POST", "/messages/actions/send", json=None if data is None else {"data": data})

    def get_messages_status(self) -> dict[str, Any]:
        """Returns all SMS Messages."""
        return self._client.request("GET", "/messages/status")

    def get_messages_storage_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all SMS storage configurations."""
        return self._client.request("GET", "/messages/storage/config", params={"all_options": all_options})

    def update_messages_storage_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected SMS storage configurations."""
        return self._client.request("PUT", "/messages/storage/config", json={"data": config})

    def get_messages_storage_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the selected SMS storage configuration."""
        return self._client.request("GET", f"/messages/storage/config/{config_id}", params={"all_options": all_options})

    def update_messages_storage_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected SMS storage configuration."""
        return self._client.request("PUT", f"/messages/storage/config/{config_id}", json={"data": config})

    def get_messages_storage_status(self) -> dict[str, Any]:
        """Returns SMS storage status."""
        return self._client.request("GET", "/messages/storage/status")
