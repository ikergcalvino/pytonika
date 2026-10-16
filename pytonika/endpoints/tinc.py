from typing import Any

from ._endpoint import Endpoint


class Tinc(Endpoint):
    def get_tinc_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Tinc VPN configurations."""
        return self._client.request("GET", "/tinc/config", params={"all_options": all_options})

    def create_tinc_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Tinc VPN configuration."""
        return self._client.request("POST", "/tinc/config", json={"data": config})

    def update_tinc_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Tinc VPN configurations."""
        return self._client.request("PUT", "/tinc/config", json={"data": config})

    def delete_tinc_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified Tinc VPN configurations."""
        return self._client.request("DELETE", "/tinc/config", json={"data": config})

    def get_tinc_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified Tinc VPN configuration."""
        return self._client.request("GET", f"/tinc/config/{config_id}", params={"all_options": all_options})

    def upload_tinc_config_by_id(self, config_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads key file."""
        return self._client.request("POST", f"/tinc/config/{config_id}", json=data)

    def update_tinc_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Tinc VPN configuration."""
        return self._client.request("PUT", f"/tinc/config/{config_id}", json={"data": config})

    def delete_tinc_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified Tinc VPN configuration."""
        return self._client.request("DELETE", f"/tinc/config/{config_id}")

    def tinc_actions_generate_keys(self, tinc_id: str) -> dict[str, Any]:
        """Generates a new RSA private and public key pair for a Tinc instance."""
        return self._client.request("POST", f"/tinc/{tinc_id}/actions/generate_keys")

    def get_tinc_hosts_config(self, tinc_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Tinc VPN Host configurations."""
        return self._client.request("GET", f"/tinc/{tinc_id}/hosts/config", params={"all_options": all_options})

    def create_tinc_hosts_config(self, tinc_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Tinc VPN Host configuration."""
        return self._client.request("POST", f"/tinc/{tinc_id}/hosts/config", json={"data": config})

    def update_tinc_hosts_config(self, tinc_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Tinc VPN Hosts configurations."""
        return self._client.request("PUT", f"/tinc/{tinc_id}/hosts/config", json={"data": config})

    def delete_tinc_hosts_config(self, tinc_id: str, config: list[str]) -> dict[str, Any]:
        """Deletes specified Tinc VPN Host configurations."""
        return self._client.request("DELETE", f"/tinc/{tinc_id}/hosts/config", json={"data": config})

    def get_tinc_hosts_config_by_id(
        self, tinc_id: str, host_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified Tinc VPN Host configuration."""
        return self._client.request(
            "GET", f"/tinc/{tinc_id}/hosts/config/{host_id}", params={"all_options": all_options}
        )

    def upload_tinc_hosts_config_by_id(self, tinc_id: str, host_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads key file."""
        return self._client.request("POST", f"/tinc/{tinc_id}/hosts/config/{host_id}", json=data)

    def update_tinc_hosts_config_by_id(self, tinc_id: str, host_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Tinc VPN Host configuration."""
        return self._client.request("PUT", f"/tinc/{tinc_id}/hosts/config/{host_id}", json={"data": config})

    def delete_tinc_hosts_config_by_id(self, tinc_id: str, host_id: str) -> dict[str, Any]:
        """Deletes the specified Tinc VPN Host configuration."""
        return self._client.request("DELETE", f"/tinc/{tinc_id}/hosts/config/{host_id}")
