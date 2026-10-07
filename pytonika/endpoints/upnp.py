from typing import Any

from ._endpoint import Endpoint


class UPnP(Endpoint):
    def get_upnp_acls_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all UPnP ACL configurations."""
        return self._client.request("GET", "/upnp/acls/config", params={"all_options": all_options})

    def create_upnp_acls_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a UPnP ACL configuration."""
        return self._client.request("POST", "/upnp/acls/config", json={"data": config})

    def update_upnp_acls_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the specified UPnP ACL configurations."""
        return self._client.request("PUT", "/upnp/acls/config", json={"data": config})

    def delete_upnp_acls_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the specified UPnP ACL configurations."""
        return self._client.request("DELETE", "/upnp/acls/config", json={"data": config})

    def get_upnp_acls_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified UPnP ACL configuration."""
        return self._client.request("GET", f"/upnp/acls/config/{config_id}", params={"all_options": all_options})

    def update_upnp_acls_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified UPnP ACL configuration."""
        return self._client.request("PUT", f"/upnp/acls/config/{config_id}", json={"data": config})

    def delete_upnp_acls_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified UPnP ACL configuration."""
        return self._client.request("DELETE", f"/upnp/acls/config/{config_id}")

    def get_upnp_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns UPnP settings."""
        return self._client.request("GET", "/upnp/global", params={"all_options": all_options})

    def update_upnp_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates UPnP settings."""
        return self._client.request("PUT", "/upnp/global", json={"data": config})

    def get_upnp_redirects_config(self) -> dict[str, Any]:
        """Returns all UPnP Redirect configurations."""
        return self._client.request("GET", "/upnp/redirects/config")

    def delete_upnp_redirects_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified UPnP Redirect configurations."""
        return self._client.request("DELETE", "/upnp/redirects/config", json={"data": config})

    def get_upnp_redirects_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified UPnP Redirect configuration."""
        return self._client.request("GET", f"/upnp/redirects/config/{config_id}")

    def delete_upnp_redirects_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified UPnP Redirect configuration."""
        return self._client.request("DELETE", f"/upnp/redirects/config/{config_id}")
