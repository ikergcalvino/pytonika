from typing import Any

from ._endpoint import Endpoint, File


class OverIP(Endpoint):
    def get_overip_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all OverIP configurations."""
        return self._client.request("GET", "/overip/config", params={"all_options": all_options})

    def create_overip_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates OverIP configuration."""
        return self._client.request("POST", "/overip/config", json={"data": config})

    def update_overip_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified OverIP configurations."""
        return self._client.request("PUT", "/overip/config", json={"data": config})

    def delete_overip_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified OverIP configurations."""
        return self._client.request("DELETE", "/overip/config", json={"data": config})

    def get_overip_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified OverIP configuration."""
        return self._client.request("GET", f"/overip/config/{config_id}", params={"all_options": all_options})

    def upload_overip_config_by_id(self, config_id: str, file: File, *, option: str | None = None) -> dict[str, Any]:
        """Uploads the specified OverIP configuration certificate files."""
        return self._client.request(
            "POST", f"/overip/config/{config_id}", files={"file": file}, form={"option": option}
        )

    def update_overip_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified OverIP configuration."""
        return self._client.request("PUT", f"/overip/config/{config_id}", json={"data": config})

    def delete_overip_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified OverIP configuration."""
        return self._client.request("DELETE", f"/overip/config/{config_id}")

    def get_overip_status(self) -> dict[str, Any]:
        """Returns OverIP status."""
        return self._client.request("GET", "/overip/status")

    def get_overip_filters_config(self, overip_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all OverIP IP Filter rules."""
        return self._client.request("GET", f"/overip/{overip_id}/filters/config", params={"all_options": all_options})

    def create_overip_filters_config(self, overip_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates OverIP IP Filter rule."""
        return self._client.request("POST", f"/overip/{overip_id}/filters/config", json={"data": config})

    def update_overip_filters_config(self, overip_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified OverIP IP Filter rules."""
        return self._client.request("PUT", f"/overip/{overip_id}/filters/config", json={"data": config})

    def delete_overip_filters_config(self, overip_id: str, config: list[str]) -> dict[str, Any]:
        """Deletes specified OverIP IP Filter rules."""
        return self._client.request("DELETE", f"/overip/{overip_id}/filters/config", json={"data": config})

    def get_overip_filters_config_by_id(
        self, overip_id: str, filter_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified OverIP IP Filter rule."""
        return self._client.request(
            "GET", f"/overip/{overip_id}/filters/config/{filter_id}", params={"all_options": all_options}
        )

    def update_overip_filters_config_by_id(
        self, overip_id: str, filter_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the specified OverIP IP Filter rule."""
        return self._client.request("PUT", f"/overip/{overip_id}/filters/config/{filter_id}", json={"data": config})

    def delete_overip_filters_config_by_id(self, overip_id: str, filter_id: str) -> dict[str, Any]:
        """Deletes the specified OverIP IP Filter rule."""
        return self._client.request("DELETE", f"/overip/{overip_id}/filters/config/{filter_id}")
