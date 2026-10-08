from typing import Any, Literal

from ._endpoint import Endpoint, File


class DNS(Endpoint):
    def get_dns_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns DNS configurations."""
        return self._client.request("GET", "/dns/config", params={"all_options": all_options})

    def update_dns_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates DNS configurations."""
        return self._client.request("PUT", "/dns/config", json={"data": config})

    def get_dns_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns DNS configuration."""
        return self._client.request("GET", f"/dns/config/{config_id}", params={"all_options": all_options})

    def upload_dns_config_by_id(
        self, config_id: str, file: File, *, option: Literal["serversfile"] | None = None
    ) -> dict[str, Any]:
        """Uploads DNS servers file."""
        return self._client.request("POST", f"/dns/config/{config_id}", files={"file": file}, form={"option": option})

    def update_dns_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates DNS configuration."""
        return self._client.request("PUT", f"/dns/config/{config_id}", json={"data": config})

    def get_dns_https_proxy_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns HTTPS DNS Proxy configurations."""
        return self._client.request("GET", "/dns/https_proxy/config", params={"all_options": all_options})

    def create_dns_https_proxy_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates HTTPS DNS Proxy configuration."""
        return self._client.request("POST", "/dns/https_proxy/config", json={"data": config})

    def update_dns_https_proxy_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates HTTPS DNS Proxy configurations."""
        return self._client.request("PUT", "/dns/https_proxy/config", json={"data": config})

    def delete_dns_https_proxy_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes HTTPS DNS Proxy configuration."""
        return self._client.request("DELETE", "/dns/https_proxy/config", json={"data": config})

    def get_dns_https_proxy_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns HTTPS DNS Proxy configuration."""
        return self._client.request("GET", f"/dns/https_proxy/config/{config_id}", params={"all_options": all_options})

    def update_dns_https_proxy_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates HTTPS DNS Proxy configuration."""
        return self._client.request("PUT", f"/dns/https_proxy/config/{config_id}", json={"data": config})

    def delete_dns_https_proxy_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes HTTPS DNS Proxy configuration."""
        return self._client.request("DELETE", f"/dns/https_proxy/config/{config_id}")

    def get_dns_https_proxy_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns HTTPS DNS Proxy Global Settings."""
        return self._client.request("GET", "/dns/https_proxy/global", params={"all_options": all_options})

    def update_dns_https_proxy_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates HTTPS DNS Proxy Global Settings."""
        return self._client.request("PUT", "/dns/https_proxy/global", json={"data": config})
