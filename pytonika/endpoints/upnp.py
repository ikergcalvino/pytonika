from typing import Any

from ._base import Endpoint


class UPnP(Endpoint):
    def get_upnp_acls_config(self) -> dict[str, Any]:
        """Returns all UPnP ACL configurations."""
        endpoint = "/upnp/acls/config"

        return self._api_client.get(endpoint)

    def create_upnp_acls_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a UPnP ACL configuration."""
        endpoint = "/upnp/acls/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_upnp_acls_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the specified UPnP ACL configurations."""
        endpoint = "/upnp/acls/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_upnp_acls_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes the specified UPnP ACL configurations."""
        return [self.delete_upnp_acls_config_by_id(acl_id) for acl_id in config]

    def get_upnp_acls_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified UPnP ACL configuration."""
        endpoint = f"/upnp/acls/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_upnp_acls_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified UPnP ACL configuration."""
        endpoint = f"/upnp/acls/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_upnp_acls_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified UPnP ACL configuration."""
        endpoint = f"/upnp/acls/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_upnp_redirects_config(self) -> dict[str, Any]:
        """Returns all UPnP Redirect configurations."""
        endpoint = "/upnp/redirects/config"

        return self._api_client.get(endpoint)

    def delete_upnp_redirects_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified UPnP Redirect configurations."""
        return [self.delete_upnp_redirects_config_by_id(redirect_id) for redirect_id in config]

    def get_upnp_redirects_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified UPnP Redirect configuration."""
        endpoint = f"/upnp/redirects/config/{config_id}"

        return self._api_client.get(endpoint)

    def delete_upnp_redirects_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified UPnP Redirect configuration."""
        endpoint = f"/upnp/redirects/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_upnp_global(self) -> dict[str, Any]:
        """Returns UPnP settings."""
        endpoint = "/upnp/global"

        return self._api_client.get(endpoint)

    def update_upnp_global(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates UPnP settings."""
        endpoint = "/upnp/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
