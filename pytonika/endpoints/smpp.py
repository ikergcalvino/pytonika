from typing import Any

from ._base import Endpoint


class SMPP(Endpoint):
    def get_smpp_config(self) -> dict[str, Any]:
        """Returns SMPP configuration in an array."""
        endpoint = "/smpp/config"

        return self._api_client.get(endpoint)

    def update_smpp_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates SMPP configuration in an array."""
        endpoint = "/smpp/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_smpp_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns SMPP configuration."""
        endpoint = f"/smpp/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_smpp_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates SMPP configuration."""
        endpoint = f"/smpp/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def upload_smpp_files(self, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads SMPP files."""
        endpoint = "/smpp/config"

        return self._api_client.post(endpoint, data={"data": data})
