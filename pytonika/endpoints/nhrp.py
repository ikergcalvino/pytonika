from typing import Any

from ._endpoint import Endpoint


class NHRP(Endpoint):
    def get_nhrp_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns NHRP global configuration."""
        return self._client.request("GET", "/nhrp/global", params={"all_options": all_options})

    def update_nhrp_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified NHRP global configuration."""
        return self._client.request("PUT", "/nhrp/global", json={"data": config})

    def get_nhrp_interface_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all NHRP interface configurations."""
        return self._client.request("GET", "/nhrp/interface/config", params={"all_options": all_options})

    def create_nhrp_interface_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates NHRP interface configuration."""
        return self._client.request("POST", "/nhrp/interface/config", json={"data": config})

    def update_nhrp_interface_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified nhrp interface configurations."""
        return self._client.request("PUT", "/nhrp/interface/config", json={"data": config})

    def delete_nhrp_interface_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified nhrp interface configurations."""
        return self._client.request("DELETE", "/nhrp/interface/config", json={"data": config})

    def get_nhrp_interface_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified NHRP interface configuration."""
        return self._client.request("GET", f"/nhrp/interface/config/{config_id}", params={"all_options": all_options})

    def update_nhrp_interface_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified NHRP interface configuration."""
        return self._client.request("PUT", f"/nhrp/interface/config/{config_id}", json={"data": config})

    def delete_nhrp_interface_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified NHRP interface configuration."""
        return self._client.request("DELETE", f"/nhrp/interface/config/{config_id}")

    def get_nhrp_interface_mapping_config(
        self, interface_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns all NHRP mapping configurations."""
        return self._client.request(
            "GET", f"/nhrp/interface/{interface_id}/mapping/config", params={"all_options": all_options}
        )

    def create_nhrp_interface_mapping_config(self, interface_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates NHRP mapping configuration."""
        return self._client.request("POST", f"/nhrp/interface/{interface_id}/mapping/config", json={"data": config})

    def update_nhrp_interface_mapping_config(self, interface_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified NHRP mapping configurations."""
        return self._client.request("PUT", f"/nhrp/interface/{interface_id}/mapping/config", json={"data": config})

    def delete_nhrp_interface_mapping_config(self, interface_id: str, config: list[str]) -> dict[str, Any]:
        """Deletes specified NHRP mapping configurations."""
        return self._client.request("DELETE", f"/nhrp/interface/{interface_id}/mapping/config", json={"data": config})

    def get_nhrp_interface_mapping_config_by_id(
        self, interface_id: str, mapping_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns specified NHRP mapping configuration."""
        return self._client.request(
            "GET", f"/nhrp/interface/{interface_id}/mapping/config/{mapping_id}", params={"all_options": all_options}
        )

    def update_nhrp_interface_mapping_config_by_id(
        self, interface_id: str, mapping_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates specified NHRP mapping configuration."""
        return self._client.request(
            "PUT", f"/nhrp/interface/{interface_id}/mapping/config/{mapping_id}", json={"data": config}
        )

    def delete_nhrp_interface_mapping_config_by_id(self, interface_id: str, mapping_id: str) -> dict[str, Any]:
        """Deletes specified NHRP mapping configuration."""
        return self._client.request("DELETE", f"/nhrp/interface/{interface_id}/mapping/config/{mapping_id}")

    def get_nhrp_interface_nhs_config(self, interface_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all NHRP NHS configurations."""
        return self._client.request(
            "GET", f"/nhrp/interface/{interface_id}/nhs/config", params={"all_options": all_options}
        )

    def create_nhrp_interface_nhs_config(self, interface_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates NHRP NHS configuration."""
        return self._client.request("POST", f"/nhrp/interface/{interface_id}/nhs/config", json={"data": config})

    def update_nhrp_interface_nhs_config(self, interface_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified NHRP NHS configurations."""
        return self._client.request("PUT", f"/nhrp/interface/{interface_id}/nhs/config", json={"data": config})

    def delete_nhrp_interface_nhs_config(self, interface_id: str, config: list[str]) -> dict[str, Any]:
        """Deletes specified NHRP NHS configurations."""
        return self._client.request("DELETE", f"/nhrp/interface/{interface_id}/nhs/config", json={"data": config})

    def get_nhrp_interface_nhs_config_by_id(
        self, interface_id: str, nhs_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns specified NHRP NHS configuration."""
        return self._client.request(
            "GET", f"/nhrp/interface/{interface_id}/nhs/config/{nhs_id}", params={"all_options": all_options}
        )

    def update_nhrp_interface_nhs_config_by_id(
        self, interface_id: str, nhs_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates specified NHRP NHS configuration."""
        return self._client.request("PUT", f"/nhrp/interface/{interface_id}/nhs/config/{nhs_id}", json={"data": config})

    def delete_nhrp_interface_nhs_config_by_id(self, interface_id: str, nhs_id: str) -> dict[str, Any]:
        """Deletes specified NHRP NHS configuration."""
        return self._client.request("DELETE", f"/nhrp/interface/{interface_id}/nhs/config/{nhs_id}")

    def get_nhrp_status(self) -> dict[str, Any]:
        """Fetches data about NHRP neighbors."""
        return self._client.request("GET", "/nhrp/status")
