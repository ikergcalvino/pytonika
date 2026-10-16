from typing import Any, Literal

from ._endpoint import Endpoint, File


class SSTP(Endpoint):
    def get_sstp_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get sstp configurations."""
        return self._client.request("GET", "/sstp/config", params={"all_options": all_options})

    def create_sstp_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create sstp configuration."""
        return self._client.request("POST", "/sstp/config", json={"data": config})

    def update_sstp_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update sstp configurations."""
        return self._client.request("PUT", "/sstp/config", json={"data": config})

    def delete_sstp_config(self, config: list[str]) -> dict[str, Any]:
        """Delete sstp configurations."""
        return self._client.request("DELETE", "/sstp/config", json={"data": config})

    def get_sstp_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get sstp configuration."""
        return self._client.request("GET", f"/sstp/config/{config_id}", params={"all_options": all_options})

    def upload_sstp_config_by_id(
        self, config_id: str, file: File, *, option: Literal["ca"] | None = None
    ) -> dict[str, Any]:
        """POST /sstp/config/{id}."""
        return self._client.request("POST", f"/sstp/config/{config_id}", files={"file": file}, form={"option": option})

    def update_sstp_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update sstp configuration."""
        return self._client.request("PUT", f"/sstp/config/{config_id}", json={"data": config})

    def delete_sstp_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Delete sstp configuration."""
        return self._client.request("DELETE", f"/sstp/config/{config_id}")

    def get_sstp_status(self) -> dict[str, Any]:
        """Returns the status of all sstp instances."""
        return self._client.request("GET", "/sstp/status")

    def get_sstp_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Return the status of the sstp instance."""
        return self._client.request("GET", f"/sstp/status/{status_id}")
