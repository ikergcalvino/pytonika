from typing import Any, Literal

from ._endpoint import Endpoint, File


class OpenConnect(Endpoint):
    def openconnect_client_actions_check_fingerprint(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """POST /openconnect/client/actions/check_fingerprint."""
        return self._client.request(
            "POST", "/openconnect/client/actions/check_fingerprint", json=None if data is None else data
        )

    def get_openconnect_client_config(self) -> dict[str, Any]:
        """Returns all OpenConnect configuration sections."""
        return self._client.request("GET", "/openconnect/client/config")

    def create_openconnect_client_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates OpenConnect client section."""
        return self._client.request("POST", "/openconnect/client/config", json={"data": config})

    def update_openconnect_client_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the specified OpenConnect configurations."""
        return self._client.request("PUT", "/openconnect/client/config", json={"data": config})

    def delete_openconnect_client_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified OpenConnect configurations."""
        return self._client.request("DELETE", "/openconnect/client/config", json={"data": config})

    def get_openconnect_client_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified OpenConnect client section."""
        return self._client.request("GET", f"/openconnect/client/config/{config_id}")

    def upload_openconnect_client_config_by_id(
        self, config_id: str, file: File, *, option: Literal["ca_cert", "user_cert", "user_key"] | None = None
    ) -> dict[str, Any]:
        """Uploads OpenConnect client certificates."""
        return self._client.request(
            "POST", f"/openconnect/client/config/{config_id}", files={"file": file}, form={"option": option}
        )

    def update_openconnect_client_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified OpenConnect configuration."""
        return self._client.request("PUT", f"/openconnect/client/config/{config_id}", json={"data": config})

    def delete_openconnect_client_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified OpenConnect configuration."""
        return self._client.request("DELETE", f"/openconnect/client/config/{config_id}")

    def get_openconnect_client_status(self) -> dict[str, Any]:
        """Returns status of OpenConnect instances."""
        return self._client.request("GET", "/openconnect/client/status")

    def get_openconnect_client_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Returns status of OpenConnect instance."""
        return self._client.request("GET", f"/openconnect/client/status/{status_id}")
