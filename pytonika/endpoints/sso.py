from typing import Any, Literal

from ._endpoint import Endpoint, File


class SSO(Endpoint):
    def get_sso_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns SSO configurations."""
        return self._client.request("GET", "/sso/config", params={"all_options": all_options})

    def create_sso_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Creates SSO configuration."""
        return self._client.request("POST", "/sso/config", json={"data": config})

    def update_sso_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates SSO configurations."""
        return self._client.request("PUT", "/sso/config", json={"data": config})

    def delete_sso_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes SSO configurations."""
        return self._client.request("DELETE", "/sso/config", json={"data": config})

    def get_sso_config_by_id(self, sso_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns SSO configuration."""
        return self._client.request("GET", f"/sso/config/{sso_id}", params={"all_options": all_options})

    def upload_sso_config_by_id(
        self, sso_id: str, file: File, *, option: Literal["icon"] | None = None
    ) -> dict[str, Any]:
        """Uploads icon file for SSO configuration."""
        return self._client.request("POST", f"/sso/config/{sso_id}", files={"file": file}, form={"option": option})

    def update_sso_config_by_id(self, sso_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates SSO configuration."""
        return self._client.request("PUT", f"/sso/config/{sso_id}", json={"data": config})

    def delete_sso_config_by_id(self, sso_id: str) -> dict[str, Any]:
        """Deletes SSO configuration."""
        return self._client.request("DELETE", f"/sso/config/{sso_id}")
