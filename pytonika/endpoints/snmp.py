from typing import Any

from ._base import Endpoint


class SNMP(Endpoint):
    def get_snmp_system_config(self) -> dict[str, Any]:
        """Returns the general SNMP configuration in an array."""
        endpoint = "/snmp/system/config"

        return self._api_client.get(endpoint)

    def update_snmp_system_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the general SNMP configuration in an array."""
        endpoint = "/snmp/system/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_snmp_system_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the general SNMP configuration."""
        endpoint = f"/snmp/system/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_snmp_system_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the general SNMP configuration."""
        endpoint = f"/snmp/system/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def snmp_system_download_mib(self, data: dict[str, Any]) -> dict[str, Any]:
        """Downloads MIB File."""
        endpoint = "/snmp/system/actions/download_mib"

        return self._api_client.post(endpoint, data={"data": data})

    def get_snmp_communities_v6_config(self) -> dict[str, Any]:
        """Returns all SNMP Communities V6 configurations."""
        endpoint = "/snmp/communities_v6/config"

        return self._api_client.get(endpoint)

    def create_snmp_communities_v6_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates SNMP Communities V6 configuration."""
        endpoint = "/snmp/communities_v6/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_snmp_communities_v6_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the specified SNMP Communities V6 configurations."""
        endpoint = "/snmp/communities_v6/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_snmp_communities_v6_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified SNMP Communities V6 configurations."""
        return [self.delete_snmp_communities_v6_config_by_id(community_id) for community_id in config]

    def get_snmp_communities_v6_config_by_id(self, community_id: str) -> dict[str, Any]:
        """Returns the specified SNMP Communities V6 configuration."""
        endpoint = f"/snmp/communities_v6/config/{community_id}"

        return self._api_client.get(endpoint)

    def update_snmp_communities_v6_config_by_id(self, community_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified SNMP Communities V6 configuration."""
        endpoint = f"/snmp/communities_v6/config/{community_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_snmp_communities_v6_config_by_id(self, community_id: str) -> dict[str, Any]:
        """Deletes the specified SNMP Communities V6 configuration."""
        endpoint = f"/snmp/communities_v6/config/{community_id}"

        return self._api_client.delete(endpoint)

    def get_snmp_trap_options(self) -> dict[str, Any]:
        """Returns SNMP Trap Rules options."""
        endpoint = "/snmp/trap/options"

        return self._api_client.get(endpoint)

    def get_snmp_trap_config(self) -> dict[str, Any]:
        """Returns all SNMP Trap Rules configurations."""
        endpoint = "/snmp/trap/config"

        return self._api_client.get(endpoint)

    def create_snmp_trap_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new SNMP Trap Rules configuration."""
        endpoint = "/snmp/trap/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_snmp_trap_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the specified SNMP Trap Rules configurations."""
        endpoint = "/snmp/trap/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_snmp_trap_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes the specified SNMP Trap Rules configurations."""
        return [self.delete_snmp_trap_config_by_id(trap_id) for trap_id in config]

    def get_snmp_trap_config_by_id(self, trap_id: str) -> dict[str, Any]:
        """Returns the specified SNMP Trap Rules configuration."""
        endpoint = f"/snmp/trap/config/{trap_id}"

        return self._api_client.get(endpoint)

    def update_snmp_trap_config_by_id(self, trap_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified SNMP Trap Rules configuration."""
        endpoint = f"/snmp/trap/config/{trap_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_snmp_trap_config_by_id(self, trap_id: str) -> dict[str, Any]:
        """Deletes the specified SNMP Trap Rules configuration."""
        endpoint = f"/snmp/trap/config/{trap_id}"

        return self._api_client.delete(endpoint)

    def get_snmp_agent_config(self) -> dict[str, Any]:
        """Returns the general SNMP Settings configuration in an array."""
        endpoint = "/snmp/agent/config"

        return self._api_client.get(endpoint)

    def update_snmp_agent_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the general SNMP Settings configuration in an array."""
        endpoint = "/snmp/agent/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_snmp_agent_config_by_id(self, agent_id: str) -> dict[str, Any]:
        """Returns the general SNMP Settings configuration."""
        endpoint = f"/snmp/agent/config/{agent_id}"

        return self._api_client.get(endpoint)

    def update_snmp_agent_config_by_id(self, agent_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the general SNMP Settings configuration."""
        endpoint = f"/snmp/agent/config/{agent_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_snmp_users_config(self) -> dict[str, Any]:
        """Returns all SNMP V3 user configurations."""
        endpoint = "/snmp/users/config"

        return self._api_client.get(endpoint)

    def create_snmp_users_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new SNMP V3 user configuration."""
        endpoint = "/snmp/users/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_snmp_users_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the specified SNMP V3 user configurations."""
        endpoint = "/snmp/users/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_snmp_users_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes the specified SNMP V3 user configurations."""
        return [self.delete_snmp_users_config_by_id(user_id) for user_id in config]

    def get_snmp_users_config_by_id(self, user_id: str) -> dict[str, Any]:
        """Returns the specified SNMP V3 user configuration."""
        endpoint = f"/snmp/users/config/{user_id}"

        return self._api_client.get(endpoint)

    def update_snmp_users_config_by_id(self, user_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified SNMP V3 user configuration."""
        endpoint = f"/snmp/users/config/{user_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_snmp_users_config_by_id(self, user_id: str) -> dict[str, Any]:
        """Deletes the specified SNMP V3 user configuration."""
        endpoint = f"/snmp/users/config/{user_id}"

        return self._api_client.delete(endpoint)

    def get_snmp_communities_config(self) -> dict[str, Any]:
        """Returns all SNMP Communities configurations."""
        endpoint = "/snmp/communities/config"

        return self._api_client.get(endpoint)

    def create_snmp_communities_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates SNMP Communities configuration."""
        endpoint = "/snmp/communities/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_snmp_communities_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the specified SNMP Communities configurations."""
        endpoint = "/snmp/communities/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_snmp_communities_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified SNMP Communities configurations."""
        return [self.delete_snmp_communities_config_by_id(community_id) for community_id in config]

    def get_snmp_communities_config_by_id(self, community_id: str) -> dict[str, Any]:
        """Returns the specified SNMP Communities configuration."""
        endpoint = f"/snmp/communities/config/{community_id}"

        return self._api_client.get(endpoint)

    def update_snmp_communities_config_by_id(self, community_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified SNMP Communities configuration."""
        endpoint = f"/snmp/communities/config/{community_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_snmp_communities_config_by_id(self, community_id: str) -> dict[str, Any]:
        """Deletes the specified SNMP Communities configuration."""
        endpoint = f"/snmp/communities/config/{community_id}"

        return self._api_client.delete(endpoint)

    def get_snmp_trap_global(self) -> dict[str, Any]:
        """Returns the general SNMP trap settings configuration."""
        endpoint = "/snmp/trap/global"

        return self._api_client.get(endpoint)

    def update_snmp_trap_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the general SNMP trap settings configuration."""
        endpoint = "/snmp/trap/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
