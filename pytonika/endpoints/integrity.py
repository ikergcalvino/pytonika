from typing import Any

from ._endpoint import Endpoint, File


class Integrity(Endpoint):
    def integrity_actions_download(self) -> bytes | dict[str, Any]:
        """Downloads integrity database."""
        return self._client.request("POST", "/integrity/actions/download", download=True)

    def integrity_actions_generate(self, config: dict[str, Any] | None = None) -> dict[str, Any]:
        """Generates integrity database."""
        return self._client.request(
            "POST", "/integrity/actions/generate", json=None if config is None else {"data": config}
        )

    def integrity_actions_validate(self) -> dict[str, Any]:
        """Validates integrity database."""
        return self._client.request("POST", "/integrity/actions/validate")

    def integrity_actions_validate_file(self, file: File) -> dict[str, Any]:
        """Validates uploaded integrity database."""
        return self._client.request("POST", "/integrity/actions/validate_file", files={"file": file})

    def get_integrity_status(self) -> dict[str, Any]:
        """Returns integrity status."""
        return self._client.request("GET", "/integrity/status")
