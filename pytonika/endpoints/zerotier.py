from typing import Any, Literal

from ._endpoint import Endpoint, File


class Zerotier(Endpoint):
    def get_zerotier_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Zerotier configurations."""
        return self._client.request("GET", "/zerotier/config", params={"all_options": all_options})

    def create_zerotier_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Zerotier configuration."""
        return self._client.request("POST", "/zerotier/config", json={"data": config})

    def update_zerotier_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Zerotier configurations."""
        return self._client.request("PUT", "/zerotier/config", json={"data": config})

    def delete_zerotier_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified Zerotier configurations."""
        return self._client.request("DELETE", "/zerotier/config", json={"data": config})

    def get_zerotier_config_by_id(self, zerotier_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified Zerotier configuration."""
        return self._client.request("GET", f"/zerotier/config/{zerotier_id}", params={"all_options": all_options})

    def update_zerotier_config_by_id(self, zerotier_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Zerotier configuration."""
        return self._client.request("PUT", f"/zerotier/config/{zerotier_id}", json={"data": config})

    def delete_zerotier_config_by_id(self, zerotier_id: str) -> dict[str, Any]:
        """Deletes the specified Zerotier configuration."""
        return self._client.request("DELETE", f"/zerotier/config/{zerotier_id}")

    def get_zerotier_networks_config(self, zerotier_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Zerotier Network configurations."""
        return self._client.request(
            "GET", f"/zerotier/{zerotier_id}/networks/config", params={"all_options": all_options}
        )

    def create_zerotier_networks_config(self, zerotier_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Zerotier Network configuration."""
        return self._client.request("POST", f"/zerotier/{zerotier_id}/networks/config", json={"data": config})

    def update_zerotier_networks_config(self, zerotier_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Zerotier Network configurations."""
        return self._client.request("PUT", f"/zerotier/{zerotier_id}/networks/config", json={"data": config})

    def delete_zerotier_networks_config(self, zerotier_id: str, config: list[str]) -> dict[str, Any]:
        """Deletes specified Zerotier network configurations."""
        return self._client.request("DELETE", f"/zerotier/{zerotier_id}/networks/config", json={"data": config})

    def get_zerotier_networks_config_by_id(
        self, zerotier_id: str, network_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified Zerotier Network configuration."""
        return self._client.request(
            "GET", f"/zerotier/{zerotier_id}/networks/config/{network_id}", params={"all_options": all_options}
        )

    def upload_zerotier_networks_config_by_id(
        self, zerotier_id: str, network_id: str, file: File, *, option: Literal["custom_planet_file"] | None = None
    ) -> dict[str, Any]:
        """Uploads planet file for the specified Zerotier Network configuration."""
        return self._client.request(
            "POST",
            f"/zerotier/{zerotier_id}/networks/config/{network_id}",
            files={"file": file},
            form={"option": option},
        )

    def update_zerotier_networks_config_by_id(
        self, zerotier_id: str, network_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the specified Zerotier Network configuration."""
        return self._client.request(
            "PUT", f"/zerotier/{zerotier_id}/networks/config/{network_id}", json={"data": config}
        )

    def delete_zerotier_networks_config_by_id(self, zerotier_id: str, network_id: str) -> dict[str, Any]:
        """Deletes the specified Zerotier Network configuration."""
        return self._client.request("DELETE", f"/zerotier/{zerotier_id}/networks/config/{network_id}")
