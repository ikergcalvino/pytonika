from typing import Any

from ._endpoint import Endpoint, File


class RIP(Endpoint):
    def get_rip_access_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all RIP access configurations."""
        return self._client.request("GET", "/rip/access/config", params={"all_options": all_options})

    def create_rip_access_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Creates RIP access configuration."""
        return self._client.request("POST", "/rip/access/config", json={"data": config})

    def update_rip_access_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified RIP access configurations."""
        return self._client.request("PUT", "/rip/access/config", json={"data": config})

    def delete_rip_access_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified RIP access configurations."""
        return self._client.request("DELETE", "/rip/access/config", json={"data": config})

    def get_rip_access_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified RIP access configuration."""
        return self._client.request("GET", f"/rip/access/config/{config_id}", params={"all_options": all_options})

    def update_rip_access_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified RIP access configuration."""
        return self._client.request("PUT", f"/rip/access/config/{config_id}", json={"data": config})

    def delete_rip_access_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified RIP access configuration."""
        return self._client.request("DELETE", f"/rip/access/config/{config_id}")

    def get_rip_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns RIP global configuration."""
        return self._client.request("GET", "/rip/global", params={"all_options": all_options})

    def upload_rip_global(self, file: File, *, option: str | None = None) -> dict[str, Any]:
        """Uploads custom RIP configuration file."""
        return self._client.request("POST", "/rip/global", files={"file": file}, form={"option": option})

    def update_rip_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified RIP global configuration."""
        return self._client.request("PUT", "/rip/global", json={"data": config})

    def get_rip_interface_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all RIP interface configurations."""
        return self._client.request("GET", "/rip/interface/config", params={"all_options": all_options})

    def create_rip_interface_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Creates rip interface configuration."""
        return self._client.request("POST", "/rip/interface/config", json={"data": config})

    def update_rip_interface_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified RIP interface configurations."""
        return self._client.request("PUT", "/rip/interface/config", json={"data": config})

    def delete_rip_interface_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified RIP interface configurations."""
        return self._client.request("DELETE", "/rip/interface/config", json={"data": config})

    def get_rip_interface_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified RIP interface configuration."""
        return self._client.request("GET", f"/rip/interface/config/{config_id}", params={"all_options": all_options})

    def update_rip_interface_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified RIP interface configuration."""
        return self._client.request("PUT", f"/rip/interface/config/{config_id}", json={"data": config})

    def delete_rip_interface_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified RIP interface configuration."""
        return self._client.request("DELETE", f"/rip/interface/config/{config_id}")

    def get_rip_interface_options(self) -> dict[str, Any]:
        """Your GET endpoint."""
        return self._client.request("GET", "/rip/interface/options")

    def get_rip_status(self) -> dict[str, Any]:
        """Fetches data about RIP neighbors."""
        return self._client.request("GET", "/rip/status")
