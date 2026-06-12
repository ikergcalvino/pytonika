from typing import Any

from ._base import Endpoint


class Hotspot2(Endpoint):
    def get_hotspot2_config(self) -> dict[str, Any]:
        """Returns all Hotspot 2.0 configurations."""
        endpoint = "/hotspot2/config"

        return self._api_client.get(endpoint)

    def update_hotspot2_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Hotspot 2.0 configurations."""
        endpoint = "/hotspot2/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_hotspot2_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified Hotspot 2.0 configuration."""
        endpoint = f"/hotspot2/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_hotspot2_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Hotspot 2.0 configuration."""
        endpoint = f"/hotspot2/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_hotspot2_venues_config(self, hotspot_id: str) -> dict[str, Any]:
        """Returns all Venue configurations for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/venues/config"

        return self._api_client.get(endpoint)

    def create_hotspot2_venues_config(self, hotspot_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Venue configuration for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/venues/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_hotspot2_venues_config(self, hotspot_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Venue configurations for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/venues/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_hotspot2_venues_config(self, hotspot_id: str, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified Venue configurations for specified Hotspot 2.0 instance."""
        return [self.delete_hotspot2_venues_config_by_id(hotspot_id, venue_id) for venue_id in config]

    def get_hotspot2_venues_config_by_id(self, hotspot_id: str, venue_id: str) -> dict[str, Any]:
        """Returns specified Venue configuration for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/venues/config/{venue_id}"

        return self._api_client.get(endpoint)

    def update_hotspot2_venues_config_by_id(
        self, hotspot_id: str, venue_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates specified Venue configuration for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/venues/config/{venue_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_hotspot2_venues_config_by_id(self, hotspot_id: str, venue_id: str) -> dict[str, Any]:
        """Deletes specified Venue configuration for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/venues/config/{venue_id}"

        return self._api_client.delete(endpoint)

    def get_hotspot2_3gpp_config(self, hotspot_id: str) -> dict[str, Any]:
        """Returns all 3GPP configurations for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/3gpp/config"

        return self._api_client.get(endpoint)

    def create_hotspot2_3gpp_config(self, hotspot_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates 3GPP configuration for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/3gpp/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_hotspot2_3gpp_config(self, hotspot_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified 3GPP configurations for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/3gpp/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_hotspot2_3gpp_config(self, hotspot_id: str, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified 3GPP configurations for specified Hotspot 2.0 instance."""
        return [self.delete_hotspot2_3gpp_config_by_id(hotspot_id, gpp_id) for gpp_id in config]

    def get_hotspot2_3gpp_config_by_id(self, hotspot_id: str, gpp_id: str) -> dict[str, Any]:
        """Returns specified 3GPP configuration for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/3gpp/config/{gpp_id}"

        return self._api_client.get(endpoint)

    def update_hotspot2_3gpp_config_by_id(self, hotspot_id: str, gpp_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified 3GPP configuration for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/3gpp/config/{gpp_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_hotspot2_3gpp_config_by_id(self, hotspot_id: str, gpp_id: str) -> dict[str, Any]:
        """Deletes specified 3GPP configuration for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/3gpp/config/{gpp_id}"

        return self._api_client.delete(endpoint)

    def get_hotspot2_nai_config(self, hotspot_id: str) -> dict[str, Any]:
        """Returns all NAI realm configurations for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/nai/config"

        return self._api_client.get(endpoint)

    def create_hotspot2_nai_config(self, hotspot_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates NAI realm configuration for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/nai/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_hotspot2_nai_config(self, hotspot_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified NAI realm configurations for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/nai/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_hotspot2_nai_config(self, hotspot_id: str, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified NAI realm configurations for specified Hotspot 2.0 instance."""
        return [self.delete_hotspot2_nai_config_by_id(hotspot_id, nai_id) for nai_id in config]

    def get_hotspot2_nai_config_by_id(self, hotspot_id: str, nai_id: str) -> dict[str, Any]:
        """Returns specified NAI realm configuration for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/nai/config/{nai_id}"

        return self._api_client.get(endpoint)

    def update_hotspot2_nai_config_by_id(self, hotspot_id: str, nai_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified NAI realm configuration for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/nai/config/{nai_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_hotspot2_nai_config_by_id(self, hotspot_id: str, nai_id: str) -> dict[str, Any]:
        """Deletes specified NAI realm configuration for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/nai/config/{nai_id}"

        return self._api_client.delete(endpoint)

    def get_hotspot2_names_config(self, hotspot_id: str) -> dict[str, Any]:
        """Returns all Operator configurations for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/names/config"

        return self._api_client.get(endpoint)

    def create_hotspot2_names_config(self, hotspot_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Operator configuration for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/names/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_hotspot2_names_config(self, hotspot_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Operator configurations for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/names/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_hotspot2_names_config(self, hotspot_id: str, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified Operator configurations for specified Hotspot 2.0 instance."""
        return [self.delete_hotspot2_names_config_by_id(hotspot_id, name_id) for name_id in config]

    def get_hotspot2_names_config_by_id(self, hotspot_id: str, name_id: str) -> dict[str, Any]:
        """Returns specified Operator configuration for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/names/config/{name_id}"

        return self._api_client.get(endpoint)

    def update_hotspot2_names_config_by_id(
        self, hotspot_id: str, name_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates specified Operator configuration for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/names/config/{name_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_hotspot2_names_config_by_id(self, hotspot_id: str, name_id: str) -> dict[str, Any]:
        """Deletes specified Operator configuration for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/names/config/{name_id}"

        return self._api_client.delete(endpoint)

    def get_hotspot2_capabilities_config(self, hotspot_id: str) -> dict[str, Any]:
        """Returns all Connection capability configurations for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/capabilities/config"

        return self._api_client.get(endpoint)

    def create_hotspot2_capabilities_config(self, hotspot_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Connection capability configuration for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/capabilities/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_hotspot2_capabilities_config(self, hotspot_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Connection capability configurations for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/capabilities/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_hotspot2_capabilities_config(self, hotspot_id: str, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified Connection capability configurations for specified Hotspot 2.0 instance."""
        return [self.delete_hotspot2_capabilities_config_by_id(hotspot_id, cap_id) for cap_id in config]

    def get_hotspot2_capabilities_config_by_id(self, hotspot_id: str, capabilities_id: str) -> dict[str, Any]:
        """Returns specified Connection capability configuration for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/capabilities/config/{capabilities_id}"

        return self._api_client.get(endpoint)

    def update_hotspot2_capabilities_config_by_id(
        self, hotspot_id: str, capabilities_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates specified Connection capability configuration for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/capabilities/config/{capabilities_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_hotspot2_capabilities_config_by_id(self, hotspot_id: str, capabilities_id: str) -> dict[str, Any]:
        """Deletes specified Connection capability configuration for specified Hotspot 2.0 instance."""
        endpoint = f"/hotspot2/{hotspot_id}/capabilities/config/{capabilities_id}"

        return self._api_client.delete(endpoint)
