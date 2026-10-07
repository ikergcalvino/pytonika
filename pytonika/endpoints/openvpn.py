from typing import Any

from ._endpoint import Endpoint, File


class OpenVPN(Endpoint):
    def get_openvpn_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all openvpn configuration sections."""
        return self._client.request("GET", "/openvpn/config", params={"all_options": all_options})

    def create_openvpn_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates openvpn section."""
        return self._client.request("POST", "/openvpn/config", json={"data": config})

    def update_openvpn_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified openvpn configurations."""
        return self._client.request("PUT", "/openvpn/config", json={"data": config})

    def delete_openvpn_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified openvpn child configurations."""
        return self._client.request("DELETE", "/openvpn/config", json={"data": config})

    def get_openvpn_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified openvpn section."""
        return self._client.request("GET", f"/openvpn/config/{config_id}", params={"all_options": all_options})

    def upload_openvpn_config_by_id(self, config_id: str, file: File, *, option: str | None = None) -> dict[str, Any]:
        """Uploads custom configuration file."""
        return self._client.request(
            "POST", f"/openvpn/config/{config_id}", files={"file": file}, form={"option": option}
        )

    def update_openvpn_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified openvpn configuration."""
        return self._client.request("PUT", f"/openvpn/config/{config_id}", json={"data": config})

    def delete_openvpn_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified openvpn configuration."""
        return self._client.request("DELETE", f"/openvpn/config/{config_id}")

    def get_openvpn_status(self, *, array: int | None = None) -> dict[str, Any]:
        """Returns all openvpn configuration sections statuses."""
        return self._client.request("GET", "/openvpn/status", params={"array": array})

    def get_openvpn_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Returns single openvpn configuration instance status."""
        return self._client.request("GET", f"/openvpn/status/{status_id}")

    def openvpn_actions_download(self, openvpn_id: str) -> bytes | dict[str, Any]:
        """Downloads specified configuration file."""
        return self._client.request("POST", f"/openvpn/{openvpn_id}/actions/download", download=True)

    def openvpn_actions_generate(self, openvpn_id: str, data: dict[str, Any] | None = None) -> bytes | dict[str, Any]:
        """Generate client configuration file."""
        return self._client.request(
            "POST",
            f"/openvpn/{openvpn_id}/actions/generate",
            json=None if data is None else {"data": data},
            download=True,
        )

    def get_openvpn_clients_config(self, openvpn_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all openvpn tls client configuration sections."""
        return self._client.request("GET", f"/openvpn/{openvpn_id}/clients/config", params={"all_options": all_options})

    def create_openvpn_clients_config(self, openvpn_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates openvpn tls section."""
        return self._client.request("POST", f"/openvpn/{openvpn_id}/clients/config", json={"data": config})

    def update_openvpn_clients_config(self, openvpn_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified openvpn tls client configurations."""
        return self._client.request("PUT", f"/openvpn/{openvpn_id}/clients/config", json={"data": config})

    def delete_openvpn_clients_config(self, openvpn_id: str, config: list[str]) -> dict[str, Any]:
        """Deletes specified openvpn tls client configurations."""
        return self._client.request("DELETE", f"/openvpn/{openvpn_id}/clients/config", json={"data": config})

    def get_openvpn_clients_config_by_id(
        self, openvpn_id: str, clients_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns specified openvpn tls client section."""
        return self._client.request(
            "GET", f"/openvpn/{openvpn_id}/clients/config/{clients_id}", params={"all_options": all_options}
        )

    def update_openvpn_clients_config_by_id(
        self, openvpn_id: str, clients_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates specified OpenVPN TLS client configuration."""
        return self._client.request("PUT", f"/openvpn/{openvpn_id}/clients/config/{clients_id}", json={"data": config})

    def delete_openvpn_clients_config_by_id(self, openvpn_id: str, clients_id: str) -> dict[str, Any]:
        """Deletes specified openvpn tls client configuration."""
        return self._client.request("DELETE", f"/openvpn/{openvpn_id}/clients/config/{clients_id}")
