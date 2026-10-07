from typing import Any

from ._endpoint import Endpoint, File


class Bonding(Endpoint):
    def get_bonding_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Bonding global configuration."""
        return self._client.request("GET", "/bonding/global", params={"all_options": all_options})

    def upload_bonding_global(self, file: File, *, option: str | None = None) -> dict[str, Any]:
        """Uploads a Bonding certificate or key file."""
        return self._client.request("POST", "/bonding/global", files={"file": file}, form={"option": option})

    def update_bonding_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Bonding global configuration."""
        return self._client.request("PUT", "/bonding/global", json={"data": config})

    def get_bonding_interfaces_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Bonding interface configurations."""
        return self._client.request("GET", "/bonding/interfaces/config", params={"all_options": all_options})

    def create_bonding_interfaces_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a Bonding interface configuration."""
        return self._client.request("POST", "/bonding/interfaces/config", json={"data": config})

    def update_bonding_interfaces_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Bonding interface configurations."""
        return self._client.request("PUT", "/bonding/interfaces/config", json={"data": config})

    def delete_bonding_interfaces_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified Bonding interface configurations."""
        return self._client.request("DELETE", "/bonding/interfaces/config", json={"data": config})

    def get_bonding_interfaces_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified Bonding interface configuration."""
        return self._client.request(
            "GET", f"/bonding/interfaces/config/{config_id}", params={"all_options": all_options}
        )

    def update_bonding_interfaces_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Bonding interface configuration."""
        return self._client.request("PUT", f"/bonding/interfaces/config/{config_id}", json={"data": config})

    def delete_bonding_interfaces_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified Bonding interface configuration."""
        return self._client.request("DELETE", f"/bonding/interfaces/config/{config_id}")

    def get_bonding_status(self) -> dict[str, Any]:
        """Returns the current Bonding runtime status."""
        return self._client.request("GET", "/bonding/status")
