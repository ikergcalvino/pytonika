from typing import Any

from ._base import Endpoint


class Integrity(Endpoint):
    def get_integrity_status(self) -> dict[str, Any]:
        """Returns integrity status."""
        endpoint = "/integrity/status"

        return self._api_client.get(endpoint)

    def integrity_actions_generate(self, config: dict[str, Any]) -> dict[str, Any]:
        """Generates integrity database."""
        endpoint = "/integrity/actions/generate"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def integrity_actions_validate(self) -> dict[str, Any]:
        """Validates integrity database."""
        endpoint = "/integrity/actions/validate"

        return self._api_client.post(endpoint)

    def integrity_actions_download(self) -> dict[str, Any]:
        """Downloads integrity database."""
        endpoint = "/integrity/actions/download"

        return self._api_client.post(endpoint)

    def integrity_actions_validate_file(self, config: dict[str, Any]) -> dict[str, Any]:
        """Validates uploaded integrity database."""
        endpoint = "/integrity/actions/validate_file"

        return self._api_client.post(endpoint, data=config)
