from typing import Any

from ._base import Endpoint


class Certificates(Endpoint):
    def get_certificates_config(self) -> dict[str, Any]:
        """Returns all generated and uploaded certificates, keys, DH parameters and CAs."""
        endpoint = "/certificates/config"

        return self._api_client.get(endpoint)

    def upload_certificate(self, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads certificate."""
        endpoint = "/certificates/config"

        return self._api_client.post(endpoint, data={"data": data})

    def download_certificate(self, cert_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Downloads specified certificate file."""
        endpoint = f"/certificates/{cert_id}/actions/download"

        return self._api_client.post(endpoint, data={"data": data})

    def get_certificates_config_by_id(self, cert_id: str) -> dict[str, Any]:
        """Returns specified certificate file."""
        endpoint = f"/certificates/config/{cert_id}"

        return self._api_client.get(endpoint)

    def delete_certificates_config_by_id(self, cert_id: str) -> dict[str, Any]:
        """Deletes specified certificate file."""
        endpoint = f"/certificates/config/{cert_id}"

        return self._api_client.delete(endpoint)

    def get_certificates_certs_config(self) -> dict[str, Any]:
        """Returns all generated and uploaded signed certificates."""
        endpoint = "/certificates/certs/config"

        return self._api_client.get(endpoint)

    def get_certificates_ca_config(self) -> dict[str, Any]:
        """Returns all generated and uploaded certificate authorities."""
        endpoint = "/certificates/ca/config"

        return self._api_client.get(endpoint)

    def get_certificates_client_config(self) -> dict[str, Any]:
        """Returns all generated and uploaded client certificates."""
        endpoint = "/certificates/client/config"

        return self._api_client.get(endpoint)

    def get_certificates_server_config(self) -> dict[str, Any]:
        """Returns all generated and uploaded server certificates."""
        endpoint = "/certificates/server/config"

        return self._api_client.get(endpoint)

    def get_certificates_keys_config(self) -> dict[str, Any]:
        """Returns all generated and uploaded keys."""
        endpoint = "/certificates/keys/config"

        return self._api_client.get(endpoint)

    def get_certificates_dh_config(self) -> dict[str, Any]:
        """Returns all generated and uploaded DH parameters."""
        endpoint = "/certificates/dh/config"

        return self._api_client.get(endpoint)

    def certificates_generate(self, data: dict[str, Any]) -> dict[str, Any]:
        """Generates certificates based on provided parameters."""
        endpoint = "/certificates/actions/generate"

        return self._api_client.post(endpoint, data={"data": data})

    def certificates_sign(self, data: dict[str, Any]) -> dict[str, Any]:
        """Signs certificate based on provided parameters."""
        endpoint = "/certificates/actions/sign"

        return self._api_client.post(endpoint, data={"data": data})

    def get_certificates_root_ca_config(self) -> dict[str, Any]:
        """Returns Root CA file contents."""
        endpoint = "/certificates/root_ca/config"

        return self._api_client.get(endpoint)

    def upload_certificates_root_ca(self, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads Root CA file."""
        endpoint = "/certificates/root_ca/config"

        return self._api_client.post(endpoint, data={"data": data})

    def update_certificates_root_ca(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Root CA file with provided data."""
        endpoint = "/certificates/root_ca/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def certificates_root_ca_change(self, data: dict[str, Any]) -> dict[str, Any]:
        """Changes Root CA to new certificate from device."""
        endpoint = "/certificates/root_ca/actions/change"

        return self._api_client.post(endpoint, data={"data": data})

    def certificates_root_ca_reset(self, data: dict[str, Any]) -> dict[str, Any]:
        """Resets Root CA to its initial value."""
        endpoint = "/certificates/root_ca/actions/reset"

        return self._api_client.post(endpoint, data={"data": data})
