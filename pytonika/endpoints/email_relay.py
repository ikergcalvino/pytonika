from typing import Any, Literal

from ._endpoint import Endpoint, File


class EmailRelay(Endpoint):
    def get_email_relay_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Email Relay configurations."""
        return self._client.request("GET", "/email_relay/config", params={"all_options": all_options})

    def create_email_relay_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Email Relay configuration."""
        return self._client.request("POST", "/email_relay/config", json={"data": config})

    def update_email_relay_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Email Relay configurations."""
        return self._client.request("PUT", "/email_relay/config", json={"data": config})

    def delete_email_relay_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified Email Relay configurations."""
        return self._client.request("DELETE", "/email_relay/config", json={"data": config})

    def get_email_relay_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified Email Relay configuration."""
        return self._client.request("GET", f"/email_relay/config/{config_id}", params={"all_options": all_options})

    def upload_email_relay_config_by_id(
        self, config_id: str, file: File, *, option: Literal["server_tls_certificate"] | None = None
    ) -> dict[str, Any]:
        """Uploads TLS certificate."""
        return self._client.request(
            "POST", f"/email_relay/config/{config_id}", files={"file": file}, form={"option": option}
        )

    def update_email_relay_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Email Relay configuration."""
        return self._client.request("PUT", f"/email_relay/config/{config_id}", json={"data": config})

    def delete_email_relay_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified Email Relay configuration."""
        return self._client.request("DELETE", f"/email_relay/config/{config_id}")
