from typing import Any

from ._base import Endpoint


class SSTP(Endpoint):
    def get_sstp_config(self) -> dict[str, Any]:
        """Get sstp configurations."""
        endpoint = "/sstp/config"

        return self._api_client.get(endpoint)

    def create_sstp_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create sstp configuration."""
        endpoint = "/sstp/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_sstp_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update sstp configurations."""
        endpoint = "/sstp/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_sstp_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Delete sstp configurations."""
        return [self.delete_sstp_config_by_id(sstp_id) for sstp_id in config]

    def get_sstp_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Get sstp configuration."""
        endpoint = f"/sstp/config/{config_id}"

        return self._api_client.get(endpoint)

    def upload_sstp_files(self, config_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads SSTP configuration files."""
        endpoint = f"/sstp/config/{config_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_sstp_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update sstp configuration."""
        endpoint = f"/sstp/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_sstp_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Delete sstp configuration."""
        endpoint = f"/sstp/config/{config_id}"

        return self._api_client.delete(endpoint)
