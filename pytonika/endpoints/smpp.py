from typing import Any, Literal

from ._endpoint import Endpoint, File


class SMPP(Endpoint):
    def get_smpp_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns SMPP configuration in an array."""
        return self._client.request("GET", "/smpp/config", params={"all_options": all_options})

    def upload_smpp_config(
        self, file: File, *, option: Literal["tls_ciphers", "tls_crt", "tls_key"] | None = None
    ) -> dict[str, Any]:
        """Uploads SMPP files."""
        return self._client.request("POST", "/smpp/config", files={"file": file}, form={"option": option})

    def update_smpp_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates SMPP configuration in an array."""
        return self._client.request("PUT", "/smpp/config", json={"data": config})

    def get_smpp_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns SMPP configuration."""
        return self._client.request("GET", f"/smpp/config/{config_id}", params={"all_options": all_options})

    def update_smpp_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates SMPP configuration."""
        return self._client.request("PUT", f"/smpp/config/{config_id}", json={"data": config})
