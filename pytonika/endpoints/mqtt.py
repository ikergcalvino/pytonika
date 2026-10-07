from typing import Any

from ._endpoint import Endpoint, File


class MQTT(Endpoint):
    def get_mqtt_bridge_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all MQTT broker bridge configurations."""
        return self._client.request("GET", "/mqtt/bridge/config", params={"all_options": all_options})

    def create_mqtt_bridge_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates MQTT broker bridge."""
        return self._client.request("POST", "/mqtt/bridge/config", json={"data": config})

    def update_mqtt_bridge_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the specified MQTT broker bridge configurations."""
        return self._client.request("PUT", "/mqtt/bridge/config", json={"data": config})

    def delete_mqtt_bridge_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the specified MQTT broker bridge configurations."""
        return self._client.request("DELETE", "/mqtt/bridge/config", json={"data": config})

    def get_mqtt_bridge_config_by_id(self, bridge_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified MQTT broker bridge."""
        return self._client.request("GET", f"/mqtt/bridge/config/{bridge_id}", params={"all_options": all_options})

    def upload_mqtt_bridge_config_by_id(
        self, bridge_id: str, file: File, *, option: str | None = None
    ) -> dict[str, Any]:
        """Uploads MQTT bridge certificate files."""
        return self._client.request(
            "POST", f"/mqtt/bridge/config/{bridge_id}", files={"file": file}, form={"option": option}
        )

    def update_mqtt_bridge_config_by_id(self, bridge_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified MQTT broker bridge configuration."""
        return self._client.request("PUT", f"/mqtt/bridge/config/{bridge_id}", json={"data": config})

    def delete_mqtt_bridge_config_by_id(self, bridge_id: str) -> dict[str, Any]:
        """Deletes the specified MQTT broker bridge configuration."""
        return self._client.request("DELETE", f"/mqtt/bridge/config/{bridge_id}")

    def get_mqtt_bridge_topics_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns MQTT Broker Bridge Topic configurations."""
        return self._client.request("GET", "/mqtt/bridge/topics/config", params={"all_options": all_options})

    def update_mqtt_bridge_topics_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected MQTT Broker Bridge Topic configurations."""
        return self._client.request("PUT", "/mqtt/bridge/topics/config", json={"data": config})

    def delete_mqtt_bridge_topics_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the selected MQTT Broker Bridge Topic configurations."""
        return self._client.request("DELETE", "/mqtt/bridge/topics/config", json={"data": config})

    def get_mqtt_bridge_topics_config_by_id(self, topic_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the selected MQTT Broker Bridge Topic configuration."""
        return self._client.request(
            "GET", f"/mqtt/bridge/topics/config/{topic_id}", params={"all_options": all_options}
        )

    def update_mqtt_bridge_topics_config_by_id(self, topic_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected MQTT Broker Bridge Topic configuration."""
        return self._client.request("PUT", f"/mqtt/bridge/topics/config/{topic_id}", json={"data": config})

    def delete_mqtt_bridge_topics_config_by_id(self, topic_id: str) -> dict[str, Any]:
        """Deletes the selected MQTT Broker Bridge Topic configuration."""
        return self._client.request("DELETE", f"/mqtt/bridge/topics/config/{topic_id}")

    def create_mqtt_bridge_topics_config(self, bridge_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new MQTT Broker Bridge Topic configuration."""
        return self._client.request("POST", f"/mqtt/bridge/{bridge_id}/topics/config", json={"data": config})

    def get_mqtt_broker_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns MQTT Broker configuration in an array."""
        return self._client.request("GET", "/mqtt/broker/config", params={"all_options": all_options})

    def update_mqtt_broker_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates MQTT Broker configuration in an array."""
        return self._client.request("PUT", "/mqtt/broker/config", json={"data": config})

    def get_mqtt_broker_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns MQTT Broker configuration."""
        return self._client.request("GET", f"/mqtt/broker/config/{config_id}", params={"all_options": all_options})

    def upload_mqtt_broker_config_by_id(
        self, config_id: str, file: File, *, option: str | None = None
    ) -> dict[str, Any]:
        """Uploads MQTT broker files."""
        return self._client.request(
            "POST", f"/mqtt/broker/config/{config_id}", files={"file": file}, form={"option": option}
        )

    def update_mqtt_broker_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates MQTT Broker configuration."""
        return self._client.request("PUT", f"/mqtt/broker/config/{config_id}", json={"data": config})

    def get_mqtt_publisher_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns MQTT Publisher configuration in an array."""
        return self._client.request("GET", "/mqtt/publisher/config", params={"all_options": all_options})

    def update_mqtt_publisher_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates MQTT Publisher configuration in an array."""
        return self._client.request("PUT", "/mqtt/publisher/config", json={"data": config})

    def get_mqtt_publisher_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns MQTT Publisher configuration."""
        return self._client.request("GET", f"/mqtt/publisher/config/{config_id}", params={"all_options": all_options})

    def upload_mqtt_publisher_config_by_id(
        self, config_id: str, file: File, *, option: str | None = None
    ) -> dict[str, Any]:
        """Uploads MQTT Publisher certificate files."""
        return self._client.request(
            "POST", f"/mqtt/publisher/config/{config_id}", files={"file": file}, form={"option": option}
        )

    def update_mqtt_publisher_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates MQTT Publisher configuration."""
        return self._client.request("PUT", f"/mqtt/publisher/config/{config_id}", json={"data": config})
