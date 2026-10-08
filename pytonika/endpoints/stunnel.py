from typing import Any, Literal

from ._endpoint import Endpoint, File


class Stunnel(Endpoint):
    def get_stunnel_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all stunnel configuration sections."""
        return self._client.request("GET", "/stunnel/config", params={"all_options": all_options})

    def create_stunnel_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates stunnel section."""
        return self._client.request("POST", "/stunnel/config", json={"data": config})

    def update_stunnel_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update all section options."""
        return self._client.request("PUT", "/stunnel/config", json={"data": config})

    def delete_stunnel_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified stunnel configurations."""
        return self._client.request("DELETE", "/stunnel/config", json={"data": config})

    def get_stunnel_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified stunnel section."""
        return self._client.request("GET", f"/stunnel/config/{config_id}", params={"all_options": all_options})

    def upload_stunnel_config_by_id(
        self, config_id: str, file: File, *, option: Literal["CAfile", "cert", "key"] | None = None
    ) -> dict[str, Any]:
        """Uploads certificates."""
        return self._client.request(
            "POST", f"/stunnel/config/{config_id}", files={"file": file}, form={"option": option}
        )

    def update_stunnel_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified stunnel configuration."""
        return self._client.request("PUT", f"/stunnel/config/{config_id}", json={"data": config})

    def delete_stunnel_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified stunnel configuration."""
        return self._client.request("DELETE", f"/stunnel/config/{config_id}")

    def get_stunnel_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified stunnel global section."""
        return self._client.request("GET", "/stunnel/global", params={"all_options": all_options})

    def update_stunnel_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified stunnel global configuration."""
        return self._client.request("PUT", "/stunnel/global", json={"data": config})
