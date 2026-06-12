from typing import Any

from ._base import Endpoint


class SIMCards(Endpoint):
    def get_sim_cards_config(self) -> dict[str, Any]:
        """Returns multiple SIM card configurations."""
        endpoint = "/sim_cards/config"

        return self._api_client.get(endpoint)

    def update_sim_cards_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates multiple SIM card configurations."""
        endpoint = "/sim_cards/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_sim_cards_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns specified SIM card configuration."""
        endpoint = f"/sim_cards/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_sim_cards_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified SIM card configuration."""
        endpoint = f"/sim_cards/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_sim_cards_status(self) -> dict[str, Any]:
        """Returns multiple SIM card status information."""
        endpoint = "/sim_cards/status"

        return self._api_client.get(endpoint)

    def get_sim_cards_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Returns specified SIM card status information."""
        endpoint = f"/sim_cards/status/{status_id}"

        return self._api_client.get(endpoint)

    def sim_cards_actions_clear_sms_limit(self, sim_id: str) -> dict[str, Any]:
        """Clears SMS limit for specified SIM card configuration."""
        endpoint = f"/sim_cards/{sim_id}/actions/clear_sms_limit"

        return self._api_client.post(endpoint)
