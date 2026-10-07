from typing import Any

from ._endpoint import Endpoint, File


class IPSec(Endpoint):
    def get_ipsec_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all IPsec configurations."""
        return self._client.request("GET", "/ipsec/config", params={"all_options": all_options})

    def create_ipsec_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates IPsec configuration."""
        return self._client.request("POST", "/ipsec/config", json={"data": config})

    def update_ipsec_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified IPsec configurations."""
        return self._client.request("PUT", "/ipsec/config", json={"data": config})

    def delete_ipsec_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified IPsec configurations."""
        return self._client.request("DELETE", "/ipsec/config", json={"data": config})

    def get_ipsec_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified IPsec configuration."""
        return self._client.request("GET", f"/ipsec/config/{config_id}", params={"all_options": all_options})

    def upload_ipsec_config_by_id(self, config_id: str, file: File, *, option: str | None = None) -> dict[str, Any]:
        """Uploads certificates."""
        return self._client.request("POST", f"/ipsec/config/{config_id}", files={"file": file}, form={"option": option})

    def update_ipsec_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified IPsec configuration."""
        return self._client.request("PUT", f"/ipsec/config/{config_id}", json={"data": config})

    def delete_ipsec_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified IPsec configuration."""
        return self._client.request("DELETE", f"/ipsec/config/{config_id}")

    def get_ipsec_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns IPsec global section."""
        return self._client.request("GET", "/ipsec/global", params={"all_options": all_options})

    def update_ipsec_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates IPsec global configuration."""
        return self._client.request("PUT", "/ipsec/global", json={"data": config})

    def get_ipsec_secrets_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all IPsec secrets configurations."""
        return self._client.request("GET", "/ipsec/secrets/config", params={"all_options": all_options})

    def create_ipsec_secrets_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates IPsec secret configuration."""
        return self._client.request("POST", "/ipsec/secrets/config", json={"data": config})

    def update_ipsec_secrets_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified IPsec secret configurations."""
        return self._client.request("PUT", "/ipsec/secrets/config", json={"data": config})

    def delete_ipsec_secrets_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified IPsec secret configurations."""
        return self._client.request("DELETE", "/ipsec/secrets/config", json={"data": config})

    def get_ipsec_secrets_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified IPsec secret configuration."""
        return self._client.request("GET", f"/ipsec/secrets/config/{config_id}", params={"all_options": all_options})

    def upload_ipsec_secrets_config_by_id(
        self, config_id: str, file: File, *, option: str | None = None
    ) -> dict[str, Any]:
        """Uploads certificates."""
        return self._client.request(
            "POST", f"/ipsec/secrets/config/{config_id}", files={"file": file}, form={"option": option}
        )

    def update_ipsec_secrets_config_by_id(self, config_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the specified IPsec secret configuration."""
        return self._client.request("PUT", f"/ipsec/secrets/config/{config_id}", json={"data": config})

    def delete_ipsec_secrets_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified IPsec secret configuration."""
        return self._client.request("DELETE", f"/ipsec/secrets/config/{config_id}")

    def get_ipsec_status(self) -> dict[str, Any]:
        """Returns the status of all ipsec instances."""
        return self._client.request("GET", "/ipsec/status")

    def get_ipsec_status_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the status of the ipsec instance."""
        return self._client.request("GET", f"/ipsec/status/{config_id}")
