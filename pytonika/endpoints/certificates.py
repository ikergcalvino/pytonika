from typing import Any

from ._endpoint import Endpoint, File


class Certificates(Endpoint):
    def certificates_actions_generate(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Generates certificates based on provided parameters."""
        return self._client.request(
            "POST", "/certificates/actions/generate", json=None if data is None else {"data": data}
        )

    def certificates_actions_import_tpm2(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Import key to tpm2 storage."""
        return self._client.request(
            "POST", "/certificates/actions/import_tpm2", json=None if data is None else {"data": data}
        )

    def certificates_actions_sign(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Signs certificate based on provided parameters."""
        return self._client.request("POST", "/certificates/actions/sign", json=None if data is None else {"data": data})

    def get_certificates_ca_config(self) -> dict[str, Any]:
        """Returns all generated and uploaded certificate authorities."""
        return self._client.request("GET", "/certificates/ca/config")

    def get_certificates_certs_config(self) -> dict[str, Any]:
        """Returns all generated and uploaded signed certificates."""
        return self._client.request("GET", "/certificates/certs/config")

    def get_certificates_client_config(self) -> dict[str, Any]:
        """Returns all generated and uploaded client certificates."""
        return self._client.request("GET", "/certificates/client/config")

    def get_certificates_config(self, *, include_tpm2: bool | None = None) -> dict[str, Any]:
        """Returns all generated and uploaded certificates, keys, DH parameters and CAs."""
        return self._client.request("GET", "/certificates/config", params={"include_tpm2": include_tpm2})

    def upload_certificates_config(self, file: File) -> dict[str, Any]:
        """Uploads certificate."""
        return self._client.request("POST", "/certificates/config", files={"file": file})

    def get_certificates_config_by_id(self, cert_id: str) -> dict[str, Any]:
        """Returns specified certificate file."""
        return self._client.request("GET", f"/certificates/config/{cert_id}")

    def delete_certificates_config_by_id(self, cert_id: str) -> dict[str, Any]:
        """Deletes specified certificate file."""
        return self._client.request("DELETE", f"/certificates/config/{cert_id}")

    def get_certificates_dh_config(self) -> dict[str, Any]:
        """Returns all generated and uploaded DH parameters."""
        return self._client.request("GET", "/certificates/dh/config")

    def get_certificates_keys_config(self) -> dict[str, Any]:
        """Returns all generated and uploaded keys."""
        return self._client.request("GET", "/certificates/keys/config")

    def certificates_root_ca_actions_change(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Changes Root CA to new certificate from device."""
        return self._client.request(
            "POST", "/certificates/root_ca/actions/change", json=None if data is None else {"data": data}
        )

    def certificates_root_ca_actions_reset(self) -> dict[str, Any]:
        """Resets Root CA to its initial value."""
        return self._client.request("POST", "/certificates/root_ca/actions/reset")

    def get_certificates_root_ca_config(self) -> dict[str, Any]:
        """Returns Root CA file contents."""
        return self._client.request("GET", "/certificates/root_ca/config")

    def upload_certificates_root_ca_config(self, file: File) -> dict[str, Any]:
        """Uploads Root CA file."""
        return self._client.request("POST", "/certificates/root_ca/config", files={"file": file})

    def update_certificates_root_ca_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Root CA file with provided data."""
        return self._client.request("PUT", "/certificates/root_ca/config", json={"data": config})

    def get_certificates_server_config(self) -> dict[str, Any]:
        """Returns all generated and uploaded server certificates."""
        return self._client.request("GET", "/certificates/server/config")

    def certificates_actions_download(self, cert_id: str) -> bytes | dict[str, Any]:
        """Downloads specified certificate file."""
        return self._client.request("POST", f"/certificates/{cert_id}/actions/download", download=True)
