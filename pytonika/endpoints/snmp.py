from typing import Any

from ._endpoint import Endpoint


class SNMP(Endpoint):
    def get_snmp_agent_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the general SNMP Settings configuration in an array."""
        return self._client.request("GET", "/snmp/agent/config", params={"all_options": all_options})

    def update_snmp_agent_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the general SNMP Settings configuration in an array."""
        return self._client.request("PUT", "/snmp/agent/config", json={"data": config})

    def get_snmp_agent_config_by_id(self, agent_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the general SNMP Settings configuration."""
        return self._client.request("GET", f"/snmp/agent/config/{agent_id}", params={"all_options": all_options})

    def update_snmp_agent_config_by_id(self, agent_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the general SNMP Settings configuration."""
        return self._client.request("PUT", f"/snmp/agent/config/{agent_id}", json={"data": config})

    def get_snmp_agent_objects_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all object configurations. Data sources can be found using /universal_gateway/options endpoint."""
        return self._client.request("GET", "/snmp/agent/objects/config", params={"all_options": all_options})

    def create_snmp_agent_objects_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new object configuration."""
        return self._client.request("POST", "/snmp/agent/objects/config", json={"data": config})

    def update_snmp_agent_objects_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified object configuration. Data sources can be found using /universal_gateway/options
        endpoint.
        """
        return self._client.request("PUT", "/snmp/agent/objects/config", json={"data": config})

    def delete_snmp_agent_objects_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified object configurations."""
        return self._client.request("DELETE", "/snmp/agent/objects/config", json={"data": config})

    def get_snmp_agent_objects_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Return object configuration. Data sources can be found using /universal_gateway/options endpoint."""
        return self._client.request(
            "GET", f"/snmp/agent/objects/config/{config_id}", params={"all_options": all_options}
        )

    def update_snmp_agent_objects_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified object configuration. Data sources can be found using /universal_gateway/options
        endpoint.
        """
        return self._client.request("PUT", f"/snmp/agent/objects/config/{config_id}", json={"data": config})

    def delete_snmp_agent_objects_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified object configuration."""
        return self._client.request("DELETE", f"/snmp/agent/objects/config/{config_id}")

    def get_snmp_communities_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all SNMP Communities configurations."""
        return self._client.request("GET", "/snmp/communities/config", params={"all_options": all_options})

    def create_snmp_communities_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates SNMP Communities configuration."""
        return self._client.request("POST", "/snmp/communities/config", json={"data": config})

    def update_snmp_communities_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the specified SNMP Communities configurations."""
        return self._client.request("PUT", "/snmp/communities/config", json={"data": config})

    def delete_snmp_communities_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified SNMP Communities configurations."""
        return self._client.request("DELETE", "/snmp/communities/config", json={"data": config})

    def get_snmp_communities_config_by_id(
        self, community_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified SNMP Communities configuration."""
        return self._client.request(
            "GET", f"/snmp/communities/config/{community_id}", params={"all_options": all_options}
        )

    def update_snmp_communities_config_by_id(self, community_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified SNMP Communities configuration."""
        return self._client.request("PUT", f"/snmp/communities/config/{community_id}", json={"data": config})

    def delete_snmp_communities_config_by_id(self, community_id: str) -> dict[str, Any]:
        """Deletes the specified SNMP Communities configuration."""
        return self._client.request("DELETE", f"/snmp/communities/config/{community_id}")

    def get_snmp_communities_v6_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all SNMP Communities V6 configurations."""
        return self._client.request("GET", "/snmp/communities_v6/config", params={"all_options": all_options})

    def create_snmp_communities_v6_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates SNMP Communities V6 configuration."""
        return self._client.request("POST", "/snmp/communities_v6/config", json={"data": config})

    def update_snmp_communities_v6_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the specified SNMP Communities V6 configurations."""
        return self._client.request("PUT", "/snmp/communities_v6/config", json={"data": config})

    def delete_snmp_communities_v6_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified SNMP Communities V6 configurations."""
        return self._client.request("DELETE", "/snmp/communities_v6/config", json={"data": config})

    def get_snmp_communities_v6_config_by_id(
        self, community_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified SNMP Communities V6 configuration."""
        return self._client.request(
            "GET", f"/snmp/communities_v6/config/{community_id}", params={"all_options": all_options}
        )

    def update_snmp_communities_v6_config_by_id(self, community_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified SNMP Communities V6 configuration."""
        return self._client.request("PUT", f"/snmp/communities_v6/config/{community_id}", json={"data": config})

    def delete_snmp_communities_v6_config_by_id(self, community_id: str) -> dict[str, Any]:
        """Deletes the specified SNMP Communities V6 configuration."""
        return self._client.request("DELETE", f"/snmp/communities_v6/config/{community_id}")

    def snmp_system_actions_download_mib(self) -> bytes | dict[str, Any]:
        """Downloads MIB File."""
        return self._client.request("POST", "/snmp/system/actions/download_mib", download=True)

    def get_snmp_system_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the general SNMP configuration in an array."""
        return self._client.request("GET", "/snmp/system/config", params={"all_options": all_options})

    def update_snmp_system_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the general SNMP configuration in an array."""
        return self._client.request("PUT", "/snmp/system/config", json={"data": config})

    def get_snmp_system_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the general SNMP configuration."""
        return self._client.request("GET", f"/snmp/system/config/{config_id}", params={"all_options": all_options})

    def update_snmp_system_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the general SNMP configuration."""
        return self._client.request("PUT", f"/snmp/system/config/{config_id}", json={"data": config})

    def get_snmp_trap_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all SNMP Trap Rules configurations."""
        return self._client.request("GET", "/snmp/trap/config", params={"all_options": all_options})

    def create_snmp_trap_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new SNMP Trap Rules configuration."""
        return self._client.request("POST", "/snmp/trap/config", json={"data": config})

    def update_snmp_trap_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the specified SNMP Trap Rules configurations."""
        return self._client.request("PUT", "/snmp/trap/config", json={"data": config})

    def delete_snmp_trap_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the specified SNMP Trap Rules configurations."""
        return self._client.request("DELETE", "/snmp/trap/config", json={"data": config})

    def get_snmp_trap_config_by_id(self, trap_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified SNMP Trap Rules configuration."""
        return self._client.request("GET", f"/snmp/trap/config/{trap_id}", params={"all_options": all_options})

    def update_snmp_trap_config_by_id(self, trap_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified SNMP Trap Rules configuration."""
        return self._client.request("PUT", f"/snmp/trap/config/{trap_id}", json={"data": config})

    def delete_snmp_trap_config_by_id(self, trap_id: str) -> dict[str, Any]:
        """Deletes the specified SNMP Trap Rules configuration."""
        return self._client.request("DELETE", f"/snmp/trap/config/{trap_id}")

    def get_snmp_trap_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the general SNMP trap settings configuration."""
        return self._client.request("GET", "/snmp/trap/global", params={"all_options": all_options})

    def update_snmp_trap_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the general SNMP trap settings configuration."""
        return self._client.request("PUT", "/snmp/trap/global", json={"data": config})

    def get_snmp_trap_options(self) -> dict[str, Any]:
        """Returns SNMP Trap Rules options."""
        return self._client.request("GET", "/snmp/trap/options")

    def get_snmp_users_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all SNMP V3 user configurations."""
        return self._client.request("GET", "/snmp/users/config", params={"all_options": all_options})

    def create_snmp_users_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new SNMP V3 user configuration."""
        return self._client.request("POST", "/snmp/users/config", json={"data": config})

    def update_snmp_users_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the specified SNMP V3 user configurations."""
        return self._client.request("PUT", "/snmp/users/config", json={"data": config})

    def delete_snmp_users_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the specified SNMP V3 user configurations."""
        return self._client.request("DELETE", "/snmp/users/config", json={"data": config})

    def get_snmp_users_config_by_id(self, user_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified SNMP V3 user configuration."""
        return self._client.request("GET", f"/snmp/users/config/{user_id}", params={"all_options": all_options})

    def update_snmp_users_config_by_id(self, user_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified SNMP V3 user configuration."""
        return self._client.request("PUT", f"/snmp/users/config/{user_id}", json={"data": config})

    def delete_snmp_users_config_by_id(self, user_id: str) -> dict[str, Any]:
        """Deletes the specified SNMP V3 user configuration."""
        return self._client.request("DELETE", f"/snmp/users/config/{user_id}")
