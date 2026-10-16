from typing import Any

from ._endpoint import Endpoint


class NTRIP(Endpoint):
    def get_ntrip_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all NTRIP configurations."""
        return self._client.request("GET", "/ntrip/config", params={"all_options": all_options})

    def create_ntrip_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates NTRIP configuration."""
        return self._client.request("POST", "/ntrip/config", json={"data": config})

    def update_ntrip_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified NTRIP configurations."""
        return self._client.request("PUT", "/ntrip/config", json={"data": config})

    def delete_ntrip_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified NTRIP configurations."""
        return self._client.request("DELETE", "/ntrip/config", json={"data": config})

    def get_ntrip_config_by_id(self, ntrip_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified NTRIP configuration."""
        return self._client.request("GET", f"/ntrip/config/{ntrip_id}", params={"all_options": all_options})

    def update_ntrip_config_by_id(self, ntrip_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified NTRIP configuration."""
        return self._client.request("PUT", f"/ntrip/config/{ntrip_id}", json={"data": config})

    def delete_ntrip_config_by_id(self, ntrip_id: str) -> dict[str, Any]:
        """Deletes the specified NTRIP configuration."""
        return self._client.request("DELETE", f"/ntrip/config/{ntrip_id}")

    def get_ntrip_status(self) -> dict[str, Any]:
        """Returns NTRIP status."""
        return self._client.request("GET", "/ntrip/status")
