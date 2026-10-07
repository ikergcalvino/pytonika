from typing import Any

from ._endpoint import Endpoint


class SIMCards(Endpoint):
    def get_sim_cards_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns multiple SIM card configurations."""
        return self._client.request("GET", "/sim_cards/config", params={"all_options": all_options})

    def update_sim_cards_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates multiple SIM card configurations."""
        return self._client.request("PUT", "/sim_cards/config", json={"data": config})

    def get_sim_cards_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified SIM card configuration."""
        return self._client.request("GET", f"/sim_cards/config/{config_id}", params={"all_options": all_options})

    def update_sim_cards_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified SIM card configuration."""
        return self._client.request("PUT", f"/sim_cards/config/{config_id}", json={"data": config})

    def get_sim_cards_status(self) -> dict[str, Any]:
        """Returns multiple SIM card status information."""
        return self._client.request("GET", "/sim_cards/status")

    def get_sim_cards_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Returns specified SIM card status information."""
        return self._client.request("GET", f"/sim_cards/status/{status_id}")

    def sim_cards_actions_clear_sms_limit(self, sim_id: str) -> dict[str, Any]:
        """Clears SMS limit for specified SIM card configuration."""
        return self._client.request("POST", f"/sim_cards/{sim_id}/actions/clear_sms_limit")
