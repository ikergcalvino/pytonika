from typing import Any

from ._base import Endpoint


class Messages(Endpoint):
    def get_messages_storage_status(self) -> dict[str, Any]:
        """Returns SMS storage status."""
        endpoint = "/messages/storage/status"

        return self._api_client.get(endpoint)

    def get_messages_storage_config(self) -> dict[str, Any]:
        """Returns all SMS storage configurations."""
        endpoint = "/messages/storage/config"

        return self._api_client.get(endpoint)

    def update_messages_storage_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected SMS storage configurations."""
        endpoint = "/messages/storage/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_messages_storage_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the selected SMS storage configuration."""
        endpoint = f"/messages/storage/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_messages_storage_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected SMS storage configuration."""
        endpoint = f"/messages/storage/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_messages_status(self) -> dict[str, Any]:
        """Returns all SMS Messages."""
        endpoint = "/messages/status"

        return self._api_client.get(endpoint)

    def messages_actions_remove_messages(self, data: dict[str, Any]) -> dict[str, Any]:
        """Deletes the selected SMS Messages."""
        endpoint = "/messages/actions/remove_messages"

        return self._api_client.post(endpoint, data={"data": data})

    def messages_actions_send(self, data: dict[str, Any]) -> dict[str, Any]:
        """Sends SMS message."""
        endpoint = "/messages/actions/send"

        return self._api_client.post(endpoint, data={"data": data})
