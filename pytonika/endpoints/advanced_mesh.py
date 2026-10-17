from typing import Any

from ._endpoint import Endpoint


class AdvancedMesh(Endpoint):
    """Endpoints of the "Advanced Mesh" page of the Teltonika Web API reference."""

    def get_advanced_mesh_config(
        self,
        *,
        all_options: bool | None = None,
    ) -> dict[str, Any]:
        """Returns all advanced mesh configurations."""
        return self._client.request(
            "GET",
            "/advanced_mesh/config",
            params={"all_options": all_options},
        )

    def create_advanced_mesh_config(
        self,
        config: dict[str, Any],
    ) -> dict[str, Any]:
        """Creates advanced mesh configuration."""
        return self._client.request(
            "POST",
            "/advanced_mesh/config",
            json={"data": config},
        )

    def update_advanced_mesh_config(
        self,
        config: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """Updates specified advanced mesh configurations."""
        return self._client.request(
            "PUT",
            "/advanced_mesh/config",
            json={"data": config},
        )

    def delete_advanced_mesh_config(
        self,
        config: list[str],
    ) -> dict[str, Any]:
        """Deletes specified advanced mesh configurations."""
        return self._client.request(
            "DELETE",
            "/advanced_mesh/config",
            json={"data": config},
        )

    def get_advanced_mesh_config_by_id(
        self,
        config_id: str,
        *,
        all_options: bool | None = None,
    ) -> dict[str, Any]:
        """Returns the specified advanced mesh configuration."""
        return self._client.request(
            "GET",
            f"/advanced_mesh/config/{config_id}",
            params={"all_options": all_options},
        )

    def update_advanced_mesh_config_by_id(
        self,
        config_id: str,
        config: dict[str, Any],
    ) -> dict[str, Any]:
        """Updates the specified advanced mesh configuration."""
        return self._client.request(
            "PUT",
            f"/advanced_mesh/config/{config_id}",
            json={"data": config},
        )

    def delete_advanced_mesh_config_by_id(
        self,
        config_id: str,
    ) -> dict[str, Any]:
        """Deletes the specified advanced mesh configuration."""
        return self._client.request("DELETE", f"/advanced_mesh/config/{config_id}")

    def get_advanced_mesh_status(self) -> dict[str, Any]:
        """Returns advanced mesh status information."""
        return self._client.request("GET", "/advanced_mesh/status")

    def get_advanced_mesh_mesh_links_config(
        self,
        advanced_mesh_id: str,
        *,
        all_options: bool | None = None,
    ) -> dict[str, Any]:
        """Returns all mesh link configurations."""
        return self._client.request(
            "GET",
            f"/advanced_mesh/{advanced_mesh_id}/mesh_links/config",
            params={"all_options": all_options},
        )

    def create_advanced_mesh_mesh_links_config(
        self,
        advanced_mesh_id: str,
        config: dict[str, Any],
    ) -> dict[str, Any]:
        """Creates mesh link configuration."""
        return self._client.request(
            "POST",
            f"/advanced_mesh/{advanced_mesh_id}/mesh_links/config",
            json={"data": config},
        )

    def update_advanced_mesh_mesh_links_config(
        self,
        advanced_mesh_id: str,
        config: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """Updates specified mesh link configurations."""
        return self._client.request(
            "PUT",
            f"/advanced_mesh/{advanced_mesh_id}/mesh_links/config",
            json={"data": config},
        )

    def delete_advanced_mesh_mesh_links_config(
        self,
        advanced_mesh_id: str,
        config: list[str],
    ) -> dict[str, Any]:
        """Deletes specified mesh link configurations."""
        return self._client.request(
            "DELETE",
            f"/advanced_mesh/{advanced_mesh_id}/mesh_links/config",
            json={"data": config},
        )

    def get_advanced_mesh_mesh_links_config_by_id(
        self,
        advanced_mesh_id: str,
        mesh_link_id: str,
        *,
        all_options: bool | None = None,
    ) -> dict[str, Any]:
        """Returns the specified mesh link configuration."""
        return self._client.request(
            "GET",
            f"/advanced_mesh/{advanced_mesh_id}/mesh_links/config/{mesh_link_id}",
            params={"all_options": all_options},
        )

    def update_advanced_mesh_mesh_links_config_by_id(
        self,
        advanced_mesh_id: str,
        mesh_link_id: str,
        config: dict[str, Any],
    ) -> dict[str, Any]:
        """Updates the specified mesh link configuration."""
        return self._client.request(
            "PUT",
            f"/advanced_mesh/{advanced_mesh_id}/mesh_links/config/{mesh_link_id}",
            json={"data": config},
        )

    def delete_advanced_mesh_mesh_links_config_by_id(
        self,
        advanced_mesh_id: str,
        mesh_link_id: str,
    ) -> dict[str, Any]:
        """Deletes the specified mesh link configuration."""
        return self._client.request("DELETE", f"/advanced_mesh/{advanced_mesh_id}/mesh_links/config/{mesh_link_id}")
