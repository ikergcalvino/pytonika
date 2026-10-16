from typing import Any, Literal

from ._endpoint import Endpoint, File


class BGP(Endpoint):
    def get_bgp_access_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all BGP access list filter configurations."""
        return self._client.request("GET", "/bgp/access/config", params={"all_options": all_options})

    def create_bgp_access_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates BGP access list filter configuration."""
        return self._client.request("POST", "/bgp/access/config", json={"data": config})

    def update_bgp_access_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates multiple BGP access list filter configurations."""
        return self._client.request("PUT", "/bgp/access/config", json={"data": config})

    def delete_bgp_access_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes multiple BGP access list filter configurations."""
        return self._client.request("DELETE", "/bgp/access/config", json={"data": config})

    def get_bgp_access_config_by_id(self, access_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified BGP access list filter configuration."""
        return self._client.request("GET", f"/bgp/access/config/{access_id}", params={"all_options": all_options})

    def update_bgp_access_config_by_id(self, access_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified BGP access list filter configuration."""
        return self._client.request("PUT", f"/bgp/access/config/{access_id}", json={"data": config})

    def delete_bgp_access_config_by_id(self, access_id: str) -> dict[str, Any]:
        """Deletes specified BGP access list filter configuration."""
        return self._client.request("DELETE", f"/bgp/access/config/{access_id}")

    def get_bgp_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns BGP global configuration."""
        return self._client.request("GET", "/bgp/global", params={"all_options": all_options})

    def upload_bgp_global(self, file: File, *, option: Literal["bgpd_custom_conf"] | None = None) -> dict[str, Any]:
        """Uploads custom BGP configuration file."""
        return self._client.request("POST", "/bgp/global", files={"file": file}, form={"option": option})

    def update_bgp_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates BGP global configuration."""
        return self._client.request("PUT", "/bgp/global", json={"data": config})

    def get_bgp_instance_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all BGP instances."""
        return self._client.request("GET", "/bgp/instance/config", params={"all_options": all_options})

    def create_bgp_instance_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates BGP instance."""
        return self._client.request("POST", "/bgp/instance/config", json={"data": config})

    def update_bgp_instance_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates multiple BGP instances."""
        return self._client.request("PUT", "/bgp/instance/config", json={"data": config})

    def delete_bgp_instance_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes multiple BGP instances."""
        return self._client.request("DELETE", "/bgp/instance/config", json={"data": config})

    def get_bgp_instance_config_by_id(self, instance_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified BGP instance."""
        return self._client.request("GET", f"/bgp/instance/config/{instance_id}", params={"all_options": all_options})

    def update_bgp_instance_config_by_id(self, instance_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified BGP instance."""
        return self._client.request("PUT", f"/bgp/instance/config/{instance_id}", json={"data": config})

    def delete_bgp_instance_config_by_id(self, instance_id: str) -> dict[str, Any]:
        """Deletes specified BGP instance."""
        return self._client.request("DELETE", f"/bgp/instance/config/{instance_id}")

    def get_bgp_instance_map_filters_config(
        self, instance_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns all BGP route map filter configurations."""
        return self._client.request(
            "GET", f"/bgp/instance/{instance_id}/map_filters/config", params={"all_options": all_options}
        )

    def create_bgp_instance_map_filters_config(self, instance_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates BGP route map filter configuration."""
        return self._client.request("POST", f"/bgp/instance/{instance_id}/map_filters/config", json={"data": config})

    def update_bgp_instance_map_filters_config(self, instance_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates multiple BGP route map filter configurations."""
        return self._client.request("PUT", f"/bgp/instance/{instance_id}/map_filters/config", json={"data": config})

    def delete_bgp_instance_map_filters_config(self, instance_id: str, config: list[str]) -> dict[str, Any]:
        """Deletes multiple BGP route map filter configurations."""
        return self._client.request("DELETE", f"/bgp/instance/{instance_id}/map_filters/config", json={"data": config})

    def get_bgp_instance_map_filters_config_by_id(
        self, instance_id: str, map_filter_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns specified BGP map filter configuration."""
        return self._client.request(
            "GET",
            f"/bgp/instance/{instance_id}/map_filters/config/{map_filter_id}",
            params={"all_options": all_options},
        )

    def update_bgp_instance_map_filters_config_by_id(
        self, instance_id: str, map_filter_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates specified BGP map filter configuration."""
        return self._client.request(
            "PUT", f"/bgp/instance/{instance_id}/map_filters/config/{map_filter_id}", json={"data": config}
        )

    def delete_bgp_instance_map_filters_config_by_id(self, instance_id: str, map_filter_id: str) -> dict[str, Any]:
        """Deletes specified BGP route map filter configuration."""
        return self._client.request("DELETE", f"/bgp/instance/{instance_id}/map_filters/config/{map_filter_id}")

    def get_bgp_instance_peer_config(self, instance_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all BGP peer configurations."""
        return self._client.request(
            "GET", f"/bgp/instance/{instance_id}/peer/config", params={"all_options": all_options}
        )

    def create_bgp_instance_peer_config(self, instance_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates BGP peer configuration."""
        return self._client.request("POST", f"/bgp/instance/{instance_id}/peer/config", json={"data": config})

    def update_bgp_instance_peer_config(self, instance_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates multiple BGP peer configurations."""
        return self._client.request("PUT", f"/bgp/instance/{instance_id}/peer/config", json={"data": config})

    def delete_bgp_instance_peer_config(self, instance_id: str, config: list[str]) -> dict[str, Any]:
        """Deletes multiple BGP peer configurations."""
        return self._client.request("DELETE", f"/bgp/instance/{instance_id}/peer/config", json={"data": config})

    def get_bgp_instance_peer_config_by_id(
        self, instance_id: str, peer_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns specified BGP peer configuration."""
        return self._client.request(
            "GET", f"/bgp/instance/{instance_id}/peer/config/{peer_id}", params={"all_options": all_options}
        )

    def update_bgp_instance_peer_config_by_id(
        self, instance_id: str, peer_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates specified BGP peer configuration."""
        return self._client.request("PUT", f"/bgp/instance/{instance_id}/peer/config/{peer_id}", json={"data": config})

    def delete_bgp_instance_peer_config_by_id(self, instance_id: str, peer_id: str) -> dict[str, Any]:
        """Deletes specified BGP peer configuration."""
        return self._client.request("DELETE", f"/bgp/instance/{instance_id}/peer/config/{peer_id}")

    def get_bgp_instance_peer_group_config(
        self, instance_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns all BGP peer group configurations."""
        return self._client.request(
            "GET", f"/bgp/instance/{instance_id}/peer_group/config", params={"all_options": all_options}
        )

    def create_bgp_instance_peer_group_config(self, instance_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates BGP peer group configuration."""
        return self._client.request("POST", f"/bgp/instance/{instance_id}/peer_group/config", json={"data": config})

    def update_bgp_instance_peer_group_config(self, instance_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates multiple BGP peer group configurations."""
        return self._client.request("PUT", f"/bgp/instance/{instance_id}/peer_group/config", json={"data": config})

    def delete_bgp_instance_peer_group_config(self, instance_id: str, config: list[str]) -> dict[str, Any]:
        """Deletes multiple BGP peer group configurations."""
        return self._client.request("DELETE", f"/bgp/instance/{instance_id}/peer_group/config", json={"data": config})

    def get_bgp_instance_peer_group_config_by_id(
        self, instance_id: str, peer_group_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns specified BGP peer group configuration."""
        return self._client.request(
            "GET", f"/bgp/instance/{instance_id}/peer_group/config/{peer_group_id}", params={"all_options": all_options}
        )

    def update_bgp_instance_peer_group_config_by_id(
        self, instance_id: str, peer_group_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates specified BGP peer group configuration."""
        return self._client.request(
            "PUT", f"/bgp/instance/{instance_id}/peer_group/config/{peer_group_id}", json={"data": config}
        )

    def delete_bgp_instance_peer_group_config_by_id(self, instance_id: str, peer_group_id: str) -> dict[str, Any]:
        """Deletes specified BGP peer group configuration."""
        return self._client.request("DELETE", f"/bgp/instance/{instance_id}/peer_group/config/{peer_group_id}")

    def get_bgp_map_filters_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all BGP route map filter configurations."""
        return self._client.request("GET", "/bgp/map_filters/config", params={"all_options": all_options})

    def create_bgp_map_filters_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates BGP route map filter configuration."""
        return self._client.request("POST", "/bgp/map_filters/config", json={"data": config})

    def update_bgp_map_filters_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates multiple BGP route map filter configurations."""
        return self._client.request("PUT", "/bgp/map_filters/config", json={"data": config})

    def delete_bgp_map_filters_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes multiple BGP route map filter configurations."""
        return self._client.request("DELETE", "/bgp/map_filters/config", json={"data": config})

    def get_bgp_map_filters_config_by_id(self, filter_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified BGP route map filter configuration."""
        return self._client.request("GET", f"/bgp/map_filters/config/{filter_id}", params={"all_options": all_options})

    def update_bgp_map_filters_config_by_id(self, filter_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified BGP route map filter configuration."""
        return self._client.request("PUT", f"/bgp/map_filters/config/{filter_id}", json={"data": config})

    def delete_bgp_map_filters_config_by_id(self, filter_id: str) -> dict[str, Any]:
        """Deletes specified BGP route map filter configuration."""
        return self._client.request("DELETE", f"/bgp/map_filters/config/{filter_id}")

    def get_bgp_maps_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all BGP route map configurations."""
        return self._client.request("GET", "/bgp/maps/config", params={"all_options": all_options})

    def create_bgp_maps_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates BGP route map configuration."""
        return self._client.request("POST", "/bgp/maps/config", json={"data": config})

    def update_bgp_maps_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates multiple BGP route map configurations."""
        return self._client.request("PUT", "/bgp/maps/config", json={"data": config})

    def delete_bgp_maps_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes multiple BGP route map configurations."""
        return self._client.request("DELETE", "/bgp/maps/config", json={"data": config})

    def get_bgp_maps_config_by_id(self, map_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified BGP route map configuration."""
        return self._client.request("GET", f"/bgp/maps/config/{map_id}", params={"all_options": all_options})

    def update_bgp_maps_config_by_id(self, map_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified BGP route map configuration."""
        return self._client.request("PUT", f"/bgp/maps/config/{map_id}", json={"data": config})

    def delete_bgp_maps_config_by_id(self, map_id: str) -> dict[str, Any]:
        """Deletes specified BGP route map configuration."""
        return self._client.request("DELETE", f"/bgp/maps/config/{map_id}")

    def get_bgp_peer_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all BGP peer configurations."""
        return self._client.request("GET", "/bgp/peer/config", params={"all_options": all_options})

    def create_bgp_peer_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates BGP peer configuration."""
        return self._client.request("POST", "/bgp/peer/config", json={"data": config})

    def update_bgp_peer_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates multiple BGP peer configurations."""
        return self._client.request("PUT", "/bgp/peer/config", json={"data": config})

    def delete_bgp_peer_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes multiple BGP peer configurations."""
        return self._client.request("DELETE", "/bgp/peer/config", json={"data": config})

    def get_bgp_peer_config_by_id(self, peer_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified BGP peer configuration."""
        return self._client.request("GET", f"/bgp/peer/config/{peer_id}", params={"all_options": all_options})

    def update_bgp_peer_config_by_id(self, peer_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified BGP peer configuration."""
        return self._client.request("PUT", f"/bgp/peer/config/{peer_id}", json={"data": config})

    def delete_bgp_peer_config_by_id(self, peer_id: str) -> dict[str, Any]:
        """Deletes specified BGP peer configuration."""
        return self._client.request("DELETE", f"/bgp/peer/config/{peer_id}")

    def get_bgp_peer_config_options(self, config_id: str) -> dict[str, Any]:
        """Your GET endpoint."""
        return self._client.request("GET", f"/bgp/peer/config/{config_id}/options")

    def get_bgp_peer_options(self) -> dict[str, Any]:
        """Lists available interfaces for selection."""
        return self._client.request("GET", "/bgp/peer/options")

    def get_bgp_peer_group_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all BGP peer group configurations."""
        return self._client.request("GET", "/bgp/peer_group/config", params={"all_options": all_options})

    def create_bgp_peer_group_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates BGP peer group configuration."""
        return self._client.request("POST", "/bgp/peer_group/config", json={"data": config})

    def update_bgp_peer_group_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates multiple BGP peer group configurations."""
        return self._client.request("PUT", "/bgp/peer_group/config", json={"data": config})

    def delete_bgp_peer_group_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes multiple BGP peer group configurations."""
        return self._client.request("DELETE", "/bgp/peer_group/config", json={"data": config})

    def get_bgp_peer_group_config_by_id(self, group_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified BGP peer group configuration."""
        return self._client.request("GET", f"/bgp/peer_group/config/{group_id}", params={"all_options": all_options})

    def update_bgp_peer_group_config_by_id(self, group_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified BGP peer group configuration."""
        return self._client.request("PUT", f"/bgp/peer_group/config/{group_id}", json={"data": config})

    def delete_bgp_peer_group_config_by_id(self, group_id: str) -> dict[str, Any]:
        """Deletes specified BGP peer group configuration."""
        return self._client.request("DELETE", f"/bgp/peer_group/config/{group_id}")

    def get_bgp_status(self) -> dict[str, Any]:
        """Fetches data about BGP neighbors."""
        return self._client.request("GET", "/bgp/status")
