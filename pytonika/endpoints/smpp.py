from typing import Any

from ._endpoint import Endpoint


class SMPP(Endpoint):
    def get_smpp_config(self) -> dict[str, Any]:
        """Returns SMPP configuration in an array."""
        endpoint = "/smpp/config"

        return self._client.request("GET", endpoint)

    def update_smpp_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates SMPP configuration in an array."""
        endpoint = "/smpp/config"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def get_smpp_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns SMPP configuration."""
        endpoint = f"/smpp/config/{config_id}"

        return self._client.request("GET", endpoint)

    def update_smpp_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates SMPP configuration."""
        endpoint = f"/smpp/config/{config_id}"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def upload_smpp_files(self, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads SMPP files."""
        endpoint = "/smpp/config"

        return self._client.request("POST", endpoint, json={"data": data})
