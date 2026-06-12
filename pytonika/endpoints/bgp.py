from typing import Any

from ._base import Endpoint


class BGP(Endpoint):
    def get_bgp_instance_config(self) -> dict[str, Any]:
        """Returns all BGP instances."""
        endpoint = "/bgp/instance/config/"

        return self._api_client.get(endpoint)

    def create_bgp_instance_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates BGP instance."""
        endpoint = "/bgp/instance/config/"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_bgp_instance_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates multiple BGP instances."""
        endpoint = "/bgp/instance/config/"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_bgp_instance_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes multiple BGP instances."""
        return [self.delete_bgp_instance_config_by_id(instance_id) for instance_id in config]

    def get_bgp_instance_config_by_id(self, instance_id: str) -> dict[str, Any]:
        """Returns specified BGP instance."""
        endpoint = f"/bgp/instance/config/{instance_id}"

        return self._api_client.get(endpoint)

    def update_bgp_instance_config_by_id(self, instance_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified BGP instance."""
        endpoint = f"/bgp/instance/config/{instance_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_bgp_instance_config_by_id(self, instance_id: str) -> dict[str, Any]:
        """Deletes specified BGP instance."""
        endpoint = f"/bgp/instance/config/{instance_id}"

        return self._api_client.delete(endpoint)

    def get_bgp_maps_config(self) -> dict[str, Any]:
        """Returns all BGP route map configurations."""
        endpoint = "/bgp/maps/config"

        return self._api_client.get(endpoint)

    def create_bgp_maps_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates BGP route map configuration."""
        endpoint = "/bgp/maps/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_bgp_maps_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates multiple BGP route map configurations."""
        endpoint = "/bgp/maps/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_bgp_maps_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes multiple BGP route map configurations."""
        return [self.delete_bgp_maps_config_by_id(map_id) for map_id in config]

    def get_bgp_maps_config_by_id(self, map_id: str) -> dict[str, Any]:
        """Returns specified BGP route map configuration."""
        endpoint = f"/bgp/maps/config/{map_id}"

        return self._api_client.get(endpoint)

    def update_bgp_maps_config_by_id(self, map_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified BGP route map configuration."""
        endpoint = f"/bgp/maps/config/{map_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_bgp_maps_config_by_id(self, map_id: str) -> dict[str, Any]:
        """Deletes specified BGP route map configuration."""
        endpoint = f"/bgp/maps/config/{map_id}"

        return self._api_client.delete(endpoint)

    def get_bgp_map_filters_config(self) -> dict[str, Any]:
        """Deprecated. Returns all BGP route map filter configurations."""
        endpoint = "/bgp/map_filters/config"

        return self._api_client.get(endpoint)

    def create_bgp_map_filters_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Deprecated. Creates BGP route map filter configuration."""
        endpoint = "/bgp/map_filters/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_bgp_map_filters_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Deprecated. Updates multiple BGP route map filter configurations."""
        endpoint = "/bgp/map_filters/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_bgp_map_filters_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deprecated. Deletes multiple BGP route map filter configurations."""
        return [self.delete_bgp_map_filters_config_by_id(filter_id) for filter_id in config]

    def get_bgp_map_filters_config_by_id(self, filter_id: str) -> dict[str, Any]:
        """Deprecated. Returns specified BGP route map filter configuration."""
        endpoint = f"/bgp/map_filters/config/{filter_id}"

        return self._api_client.get(endpoint)

    def update_bgp_map_filters_config_by_id(self, filter_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Deprecated. Updates specified BGP route map filter configuration."""
        endpoint = f"/bgp/map_filters/config/{filter_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_bgp_map_filters_config_by_id(self, filter_id: str) -> dict[str, Any]:
        """Deprecated. Deletes specified BGP route map filter configuration."""
        endpoint = f"/bgp/map_filters/config/{filter_id}"

        return self._api_client.delete(endpoint)

    def get_bgp_instance_map_filters_config(self, instance_id: str) -> dict[str, Any]:
        """Returns all BGP route map filter configurations."""
        endpoint = f"/bgp/instance/{instance_id}/map_filters/config"

        return self._api_client.get(endpoint)

    def create_bgp_instance_map_filters_config(self, instance_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates BGP route map filter configuration."""
        endpoint = f"/bgp/instance/{instance_id}/map_filters/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_bgp_instance_map_filters_config(self, instance_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates multiple BGP route map filter configurations."""
        endpoint = f"/bgp/instance/{instance_id}/map_filters/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_bgp_instance_map_filters_config(self, instance_id: str, config: list[str]) -> list[dict[str, Any]]:
        """Deletes multiple BGP route map filter configurations."""
        return [self.delete_bgp_instance_map_filters_config_by_id(instance_id, filter_id) for filter_id in config]

    def get_bgp_instance_map_filters_config_by_id(self, instance_id: str, map_filter_id: str) -> dict[str, Any]:
        """Returns specified BGP map filter configuration."""
        endpoint = f"/bgp/instance/{instance_id}/map_filters/config/{map_filter_id}"

        return self._api_client.get(endpoint)

    def update_bgp_instance_map_filters_config_by_id(
        self, instance_id: str, map_filter_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates specified BGP map filter configuration."""
        endpoint = f"/bgp/instance/{instance_id}/map_filters/config/{map_filter_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_bgp_instance_map_filters_config_by_id(self, instance_id: str, map_filter_id: str) -> dict[str, Any]:
        """Deletes specified BGP route map filter configuration."""
        endpoint = f"/bgp/instance/{instance_id}/map_filters/config/{map_filter_id}"

        return self._api_client.delete(endpoint)

    def get_bgp_peer_config(self) -> dict[str, Any]:
        """Deprecated. Returns all BGP peer configurations."""
        endpoint = "/bgp/peer/config"

        return self._api_client.get(endpoint)

    def create_bgp_peer_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Deprecated. Creates BGP peer configuration."""
        endpoint = "/bgp/peer/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_bgp_peer_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Deprecated. Updates multiple BGP peer configurations."""
        endpoint = "/bgp/peer/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_bgp_peer_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deprecated. Deletes multiple BGP peer configurations."""
        return [self.delete_bgp_peer_config_by_id(peer_id) for peer_id in config]

    def get_bgp_peer_config_by_id(self, peer_id: str) -> dict[str, Any]:
        """Deprecated. Returns specified BGP peer configuration."""
        endpoint = f"/bgp/peer/config/{peer_id}"

        return self._api_client.get(endpoint)

    def update_bgp_peer_config_by_id(self, peer_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Deprecated. Updates specified BGP peer configuration."""
        endpoint = f"/bgp/peer/config/{peer_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_bgp_peer_config_by_id(self, peer_id: str) -> dict[str, Any]:
        """Deprecated. Deletes specified BGP peer configuration."""
        endpoint = f"/bgp/peer/config/{peer_id}"

        return self._api_client.delete(endpoint)

    def get_bgp_instance_peer_config(self, instance_id: str) -> dict[str, Any]:
        """Returns all BGP peer configurations."""
        endpoint = f"/bgp/instance/{instance_id}/peer/config"

        return self._api_client.get(endpoint)

    def create_bgp_instance_peer_config(self, instance_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates BGP peer configuration."""
        endpoint = f"/bgp/instance/{instance_id}/peer/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_bgp_instance_peer_config(self, instance_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates multiple BGP peer configurations."""
        endpoint = f"/bgp/instance/{instance_id}/peer/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_bgp_instance_peer_config(self, instance_id: str, config: list[str]) -> list[dict[str, Any]]:
        """Deletes multiple BGP peer configurations."""
        return [self.delete_bgp_instance_peer_config_by_id(instance_id, peer_id) for peer_id in config]

    def get_bgp_instance_peer_config_by_id(self, instance_id: str, peer_id: str) -> dict[str, Any]:
        """Returns specified BGP peer configuration."""
        endpoint = f"/bgp/instance/{instance_id}/peer/config/{peer_id}"

        return self._api_client.get(endpoint)

    def update_bgp_instance_peer_config_by_id(
        self, instance_id: str, peer_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates specified BGP peer configuration."""
        endpoint = f"/bgp/instance/{instance_id}/peer/config/{peer_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_bgp_instance_peer_config_by_id(self, instance_id: str, peer_id: str) -> dict[str, Any]:
        """Deletes specified BGP peer configuration."""
        endpoint = f"/bgp/instance/{instance_id}/peer/config/{peer_id}"

        return self._api_client.delete(endpoint)

    def get_bgp_peer_group_config(self) -> dict[str, Any]:
        """Deprecated. Returns all BGP peer group configurations."""
        endpoint = "/bgp/peer_group/config"

        return self._api_client.get(endpoint)

    def create_bgp_peer_group_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Deprecated. Creates BGP peer group configuration."""
        endpoint = "/bgp/peer_group/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_bgp_peer_group_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Deprecated. Updates multiple BGP peer group configurations."""
        endpoint = "/bgp/peer_group/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_bgp_peer_group_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deprecated. Deletes multiple BGP peer group configurations."""
        return [self.delete_bgp_peer_group_config_by_id(group_id) for group_id in config]

    def get_bgp_peer_group_config_by_id(self, group_id: str) -> dict[str, Any]:
        """Deprecated. Returns specified BGP peer group configuration."""
        endpoint = f"/bgp/peer_group/config/{group_id}"

        return self._api_client.get(endpoint)

    def update_bgp_peer_group_config_by_id(self, group_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Deprecated. Updates specified BGP peer group configuration."""
        endpoint = f"/bgp/peer_group/config/{group_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_bgp_peer_group_config_by_id(self, group_id: str) -> dict[str, Any]:
        """Deprecated. Deletes specified BGP peer group configuration."""
        endpoint = f"/bgp/peer_group/config/{group_id}"

        return self._api_client.delete(endpoint)

    def get_bgp_instance_peer_group_config(self, instance_id: str) -> dict[str, Any]:
        """Returns all BGP peer group configurations."""
        endpoint = f"/bgp/instance/{instance_id}/peer_group/config"

        return self._api_client.get(endpoint)

    def create_bgp_instance_peer_group_config(self, instance_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates BGP peer group configuration."""
        endpoint = f"/bgp/instance/{instance_id}/peer_group/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_bgp_instance_peer_group_config(self, instance_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates multiple BGP peer group configurations."""
        endpoint = f"/bgp/instance/{instance_id}/peer_group/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_bgp_instance_peer_group_config(self, instance_id: str, config: list[str]) -> list[dict[str, Any]]:
        """Deletes multiple BGP peer group configurations."""
        return [self.delete_bgp_instance_peer_group_config_by_id(instance_id, group_id) for group_id in config]

    def get_bgp_instance_peer_group_config_by_id(self, instance_id: str, peer_group_id: str) -> dict[str, Any]:
        """Returns specified BGP peer group configuration."""
        endpoint = f"/bgp/instance/{instance_id}/peer_group/config/{peer_group_id}"

        return self._api_client.get(endpoint)

    def update_bgp_instance_peer_group_config_by_id(
        self, instance_id: str, peer_group_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates specified BGP peer group configuration."""
        endpoint = f"/bgp/instance/{instance_id}/peer_group/config/{peer_group_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_bgp_instance_peer_group_config_by_id(self, instance_id: str, peer_group_id: str) -> dict[str, Any]:
        """Deletes specified BGP peer group configuration."""
        endpoint = f"/bgp/instance/{instance_id}/peer_group/config/{peer_group_id}"

        return self._api_client.delete(endpoint)

    def get_bgp_global(self) -> dict[str, Any]:
        """Returns BGP global configuration."""
        endpoint = "/bgp/global"

        return self._api_client.get(endpoint)

    def upload_bgp_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Uploads custom BGP configuration file."""
        endpoint = "/bgp/global"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_bgp_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates BGP global configuration."""
        endpoint = "/bgp/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_bgp_status(self) -> dict[str, Any]:
        """Fetches data about BGP neighbors."""
        endpoint = "/bgp/status"

        return self._api_client.get(endpoint)

    def get_bgp_access_config(self) -> dict[str, Any]:
        """Returns all BGP access list filter configurations."""
        endpoint = "/bgp/access/config"

        return self._api_client.get(endpoint)

    def create_bgp_access_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates BGP access list filter configuration."""
        endpoint = "/bgp/access/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_bgp_access_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates multiple BGP access list filter configurations."""
        endpoint = "/bgp/access/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_bgp_access_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes multiple BGP access list filter configurations."""
        return [self.delete_bgp_access_config_by_id(access_id) for access_id in config]

    def get_bgp_access_config_by_id(self, access_id: str) -> dict[str, Any]:
        """Returns specified BGP access list filter configuration."""
        endpoint = f"/bgp/access/config/{access_id}"

        return self._api_client.get(endpoint)

    def update_bgp_access_config_by_id(self, access_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified BGP access list filter configuration."""
        endpoint = f"/bgp/access/config/{access_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_bgp_access_config_by_id(self, access_id: str) -> dict[str, Any]:
        """Deletes specified BGP access list filter configuration."""
        endpoint = f"/bgp/access/config/{access_id}"

        return self._api_client.delete(endpoint)
