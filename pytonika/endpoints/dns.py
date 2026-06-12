from typing import Any

from ._base import Endpoint


class DNS(Endpoint):
    def get_dns_https_proxy_global(self) -> dict[str, Any]:
        """Returns HTTPS DNS Proxy Global Settings."""
        endpoint = "/dns/https_proxy/global"

        return self._api_client.get(endpoint)

    def update_dns_https_proxy_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates HTTPS DNS Proxy Global Settings."""
        endpoint = "/dns/https_proxy/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_dns_https_proxy_config(self) -> dict[str, Any]:
        """Returns HTTPS DNS Proxy configurations."""
        endpoint = "/dns/https_proxy/config"

        return self._api_client.get(endpoint)

    def create_dns_https_proxy_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates HTTPS DNS Proxy configuration."""
        endpoint = "/dns/https_proxy/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_dns_https_proxy_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates HTTPS DNS Proxy configurations."""
        endpoint = "/dns/https_proxy/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dns_https_proxy_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes HTTPS DNS Proxy configuration."""
        return [self.delete_dns_https_proxy_config_by_id(proxy_id) for proxy_id in config]

    def get_dns_https_proxy_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns HTTPS DNS Proxy configuration."""
        endpoint = f"/dns/https_proxy/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_dns_https_proxy_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates HTTPS DNS Proxy configuration."""
        endpoint = f"/dns/https_proxy/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dns_https_proxy_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes HTTPS DNS Proxy configuration."""
        endpoint = f"/dns/https_proxy/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_dns_config(self) -> dict[str, Any]:
        """Returns DNS configurations."""
        endpoint = "/dns/config"

        return self._api_client.get(endpoint)

    def update_dns_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates DNS configurations."""
        endpoint = "/dns/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_dns_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns DNS configuration."""
        endpoint = f"/dns/config/{config_id}"

        return self._api_client.get(endpoint)

    def upload_dns_servers_file(self, config_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads DNS servers file."""
        endpoint = f"/dns/config/{config_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_dns_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates DNS configuration."""
        endpoint = f"/dns/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
