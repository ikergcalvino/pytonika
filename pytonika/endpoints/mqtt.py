from typing import Any

from ._base import Endpoint


class MQTT(Endpoint):
    def get_mqtt_bridge_config(self) -> dict[str, Any]:
        """Returns all MQTT broker bridge configurations."""
        endpoint = "/mqtt/bridge/config"

        return self._api_client.get(endpoint)

    def create_mqtt_bridge_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates MQTT broker bridge."""
        endpoint = "/mqtt/bridge/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_mqtt_bridge_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the specified MQTT broker bridge configurations."""
        endpoint = "/mqtt/bridge/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_mqtt_bridge_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes the specified MQTT broker bridge configurations."""
        return [self.delete_mqtt_bridge_config_by_id(bridge_id) for bridge_id in config]

    def get_mqtt_bridge_config_by_id(self, bridge_id: str) -> dict[str, Any]:
        """Returns the specified MQTT broker bridge."""
        endpoint = f"/mqtt/bridge/config/{bridge_id}"

        return self._api_client.get(endpoint)

    def upload_mqtt_bridge_certificate(self, bridge_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads MQTT bridge certificate files."""
        endpoint = f"/mqtt/bridge/config/{bridge_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_mqtt_bridge_config_by_id(self, bridge_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified MQTT broker bridge configuration."""
        endpoint = f"/mqtt/bridge/config/{bridge_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_mqtt_bridge_config_by_id(self, bridge_id: str) -> dict[str, Any]:
        """Deletes the specified MQTT broker bridge configuration."""
        endpoint = f"/mqtt/bridge/config/{bridge_id}"

        return self._api_client.delete(endpoint)

    def create_mqtt_bridge_topic_config(self, bridge_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new MQTT Broker Bridge Topic configuration."""
        endpoint = f"/mqtt/bridge/{bridge_id}/topics/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def get_mqtt_bridge_topics_config(self) -> dict[str, Any]:
        """Returns MQTT Broker Bridge Topic configurations."""
        endpoint = "/mqtt/bridge/topics/config"

        return self._api_client.get(endpoint)

    def update_mqtt_bridge_topics_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected MQTT Broker Bridge Topic configurations."""
        endpoint = "/mqtt/bridge/topics/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_mqtt_bridge_topics_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes the selected MQTT Broker Bridge Topic configurations."""
        return [self.delete_mqtt_bridge_topics_config_by_id(topic_id) for topic_id in config]

    def get_mqtt_bridge_topics_config_by_id(self, topic_id: str) -> dict[str, Any]:
        """Returns the selected MQTT Broker Bridge Topic configuration."""
        endpoint = f"/mqtt/bridge/topics/config/{topic_id}"

        return self._api_client.get(endpoint)

    def update_mqtt_bridge_topics_config_by_id(self, topic_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected MQTT Broker Bridge Topic configuration."""
        endpoint = f"/mqtt/bridge/topics/config/{topic_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_mqtt_bridge_topics_config_by_id(self, topic_id: str) -> dict[str, Any]:
        """Deletes the selected MQTT Broker Bridge Topic configuration."""
        endpoint = f"/mqtt/bridge/topics/config/{topic_id}"

        return self._api_client.delete(endpoint)

    def get_mqtt_publisher_config(self) -> dict[str, Any]:
        """Returns MQTT Publisher configuration in an array."""
        endpoint = "/mqtt/publisher/config"

        return self._api_client.get(endpoint)

    def update_mqtt_publisher_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates MQTT Publisher configuration in an array."""
        endpoint = "/mqtt/publisher/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_mqtt_publisher_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns MQTT Publisher configuration."""
        endpoint = f"/mqtt/publisher/config/{config_id}"

        return self._api_client.get(endpoint)

    def upload_mqtt_publisher_certificate(self, config_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads MQTT Publisher certificate files."""
        endpoint = f"/mqtt/publisher/config/{config_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_mqtt_publisher_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates MQTT Publisher configuration."""
        endpoint = f"/mqtt/publisher/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_mqtt_broker_config(self) -> dict[str, Any]:
        """Returns MQTT Broker configuration in an array."""
        endpoint = "/mqtt/broker/config"

        return self._api_client.get(endpoint)

    def update_mqtt_broker_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates MQTT Broker configuration in an array."""
        endpoint = "/mqtt/broker/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_mqtt_broker_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns MQTT Broker configuration."""
        endpoint = f"/mqtt/broker/config/{config_id}"

        return self._api_client.get(endpoint)

    def upload_mqtt_broker_files(self, config_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads MQTT broker files."""
        endpoint = f"/mqtt/broker/config/{config_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_mqtt_broker_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates MQTT Broker configuration."""
        endpoint = f"/mqtt/broker/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
