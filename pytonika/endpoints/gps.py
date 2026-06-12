from typing import Any

from ._base import Endpoint


class GPS(Endpoint):
    def get_gps_nmea_config(self) -> dict[str, Any]:
        """Get GPS NMEA configurations."""
        endpoint = "/gps/nmea/config"

        return self._api_client.get(endpoint)

    def update_gps_nmea_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update GPS NMEA configurations."""
        endpoint = "/gps/nmea/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_gps_nmea_config_by_id(self, nmea_id: str) -> dict[str, Any]:
        """Get GPS NMEA configuration."""
        endpoint = f"/gps/nmea/config/{nmea_id}"

        return self._api_client.get(endpoint)

    def update_gps_nmea_config_by_id(self, nmea_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update GPS NMEA configuration."""
        endpoint = f"/gps/nmea/config/{nmea_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_gps_nmea_status(self) -> dict[str, Any]:
        """Returns GPS NMEA status."""
        endpoint = "/gps/nmea/status"

        return self._api_client.get(endpoint)

    def get_gps_avl_secondary_rules_config(self) -> dict[str, Any]:
        """Get GPS AVL Rules configurations."""
        endpoint = "/gps/avl/secondary_rules/config"

        return self._api_client.get(endpoint)

    def create_gps_avl_secondary_rules_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create GPS AVL Rules configuration."""
        endpoint = "/gps/avl/secondary_rules/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_gps_avl_secondary_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update GPS AVL Rules configurations."""
        endpoint = "/gps/avl/secondary_rules/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_gps_avl_secondary_rules_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Delete GPS AVL Rules configurations."""
        return [self.delete_gps_avl_secondary_rules_config_by_id(secondary_rule_id) for secondary_rule_id in config]

    def get_gps_avl_secondary_rules_config_by_id(self, secondary_rule_id: str) -> dict[str, Any]:
        """Get GPS AVL Rules configuration."""
        endpoint = f"/gps/avl/secondary_rules/config/{secondary_rule_id}"

        return self._api_client.get(endpoint)

    def update_gps_avl_secondary_rules_config_by_id(
        self, secondary_rule_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Update GPS AVL Rules configuration."""
        endpoint = f"/gps/avl/secondary_rules/config/{secondary_rule_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_gps_avl_secondary_rules_config_by_id(self, secondary_rule_id: str) -> dict[str, Any]:
        """Delete GPS AVL Rules configuration."""
        endpoint = f"/gps/avl/secondary_rules/config/{secondary_rule_id}"

        return self._api_client.delete(endpoint)

    def get_gps_https_config(self) -> dict[str, Any]:
        """Get GPS HTTP General configurations."""
        endpoint = "/gps/https/config"

        return self._api_client.get(endpoint)

    def update_gps_https_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update GPS HTTP General configurations."""
        endpoint = "/gps/https/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_gps_https_config_by_id(self, http_id: str) -> dict[str, Any]:
        """Get GPS HTTP General configuration."""
        endpoint = f"/gps/https/config/{http_id}"

        return self._api_client.get(endpoint)

    def update_gps_https_config_by_id(self, http_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update GPS HTTP General configuration."""
        endpoint = f"/gps/https/config/{http_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_gps_https_status(self) -> dict[str, Any]:
        """Returns GPS HTTPS status."""
        endpoint = "/gps/https/status"

        return self._api_client.get(endpoint)

    def get_gps_avl_main_rules_config(self) -> dict[str, Any]:
        """Get GPS AVL Main configurations."""
        endpoint = "/gps/avl/main_rules/config"

        return self._api_client.get(endpoint)

    def update_gps_avl_main_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update GPS AVL Main configurations."""
        endpoint = "/gps/avl/main_rules/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_gps_avl_main_rules_config_by_id(self, main_rule_id: str) -> dict[str, Any]:
        """Get GPS AVL Main configuration."""
        endpoint = f"/gps/avl/main_rules/config/{main_rule_id}"

        return self._api_client.get(endpoint)

    def update_gps_avl_main_rules_config_by_id(self, main_rule_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update GPS AVL Main configuration."""
        endpoint = f"/gps/avl/main_rules/config/{main_rule_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_gps_nmea_serial_config(self) -> dict[str, Any]:
        """Returns GPS NMEA Serial Port configurations."""
        endpoint = "/gps/nmea/serial/config"

        return self._api_client.get(endpoint)

    def create_gps_nmea_serial_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates GPS NMEA Serial Port configuration."""
        endpoint = "/gps/nmea/serial/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_gps_nmea_serial_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update GPS NMEA Serial Port configurations."""
        endpoint = "/gps/nmea/serial/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_gps_nmea_serial_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified GPS NMEA Serial Port configurations."""
        return [self.delete_gps_nmea_serial_config_by_id(serial_id) for serial_id in config]

    def get_gps_nmea_serial_config_by_id(self, serial_id: str) -> dict[str, Any]:
        """Returns GPS NMEA Serial Port configuration."""
        endpoint = f"/gps/nmea/serial/config/{serial_id}"

        return self._api_client.get(endpoint)

    def update_gps_nmea_serial_config_by_id(self, serial_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update GPS NMEA Serial Port configuration."""
        endpoint = f"/gps/nmea/serial/config/{serial_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_gps_nmea_serial_config_by_id(self, serial_id: str) -> dict[str, Any]:
        """Deletes the specified NMEA Serial Port configuration."""
        endpoint = f"/gps/nmea/serial/config/{serial_id}"

        return self._api_client.delete(endpoint)

    def get_gps_avl_tavl_rules_config(self) -> dict[str, Any]:
        """Get GPS TAVL Rules configurations."""
        endpoint = "/gps/avl/tavl_rules/config"

        return self._api_client.get(endpoint)

    def create_gps_avl_tavl_rules_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create GPS TAVL rule configuration."""
        endpoint = "/gps/avl/tavl_rules/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_gps_avl_tavl_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update GPS TAVL Rules configurations."""
        endpoint = "/gps/avl/tavl_rules/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_gps_avl_tavl_rules_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Delete GPS TAVL rules configurations."""
        return [self.delete_gps_avl_tavl_rules_config_by_id(tavl_rule_id) for tavl_rule_id in config]

    def get_gps_avl_tavl_rules_config_by_id(self, tavl_rule_id: str) -> dict[str, Any]:
        """Get GPS TAVL Rules configuration."""
        endpoint = f"/gps/avl/tavl_rules/config/{tavl_rule_id}"

        return self._api_client.get(endpoint)

    def update_gps_avl_tavl_rules_config_by_id(self, tavl_rule_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update GPS TAVL Rules configuration."""
        endpoint = f"/gps/avl/tavl_rules/config/{tavl_rule_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_gps_avl_tavl_rules_config_by_id(self, tavl_rule_id: str) -> dict[str, Any]:
        """Delete GPS TAVL Rule configuration."""
        endpoint = f"/gps/avl/tavl_rules/config/{tavl_rule_id}"

        return self._api_client.delete(endpoint)

    def get_gps_avl_config(self) -> dict[str, Any]:
        """Get GPS AVL General configurations."""
        endpoint = "/gps/avl/config"

        return self._api_client.get(endpoint)

    def update_gps_avl_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update GPS AVL General configurations."""
        endpoint = "/gps/avl/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_gps_avl_config_by_id(self, avl_id: str) -> dict[str, Any]:
        """Get GPS AVL General configuration."""
        endpoint = f"/gps/avl/config/{avl_id}"

        return self._api_client.get(endpoint)

    def update_gps_avl_config_by_id(self, avl_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update GPS AVL General configuration."""
        endpoint = f"/gps/avl/config/{avl_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_gps_avl_status(self) -> dict[str, Any]:
        """Returns GPS AVL status."""
        endpoint = "/gps/avl/status"

        return self._api_client.get(endpoint)

    def get_gps_global(self) -> dict[str, Any]:
        """Get GPS General configuration."""
        endpoint = "/gps/global"

        return self._api_client.get(endpoint)

    def update_gps_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Update GPS General configuration."""
        endpoint = "/gps/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_gps_status(self) -> dict[str, Any]:
        """Returns GPS service status."""
        endpoint = "/gps/status"

        return self._api_client.get(endpoint)

    def get_gps_position_status(self) -> dict[str, Any]:
        """Get GPS position."""
        endpoint = "/gps/position/status"

        return self._api_client.get(endpoint)

    def get_gps_https_tavl_rules_config(self) -> dict[str, Any]:
        """Get GPS HTTP configurations."""
        endpoint = "/gps/https/tavl_rules/config"

        return self._api_client.get(endpoint)

    def create_gps_https_tavl_rules_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create GPS HTTP configuration."""
        endpoint = "/gps/https/tavl_rules/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_gps_https_tavl_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update GPS HTTP configurations."""
        endpoint = "/gps/https/tavl_rules/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_gps_https_tavl_rules_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Delete GPS HTTP configurations."""
        return [self.delete_gps_https_tavl_rules_config_by_id(tavl_rule_id) for tavl_rule_id in config]

    def get_gps_https_tavl_rules_config_by_id(self, tavl_rule_id: str) -> dict[str, Any]:
        """Get GPS HTTP configuration."""
        endpoint = f"/gps/https/tavl_rules/config/{tavl_rule_id}"

        return self._api_client.get(endpoint)

    def update_gps_https_tavl_rules_config_by_id(self, tavl_rule_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update GPS HTTP configuration."""
        endpoint = f"/gps/https/tavl_rules/config/{tavl_rule_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_gps_https_tavl_rules_config_by_id(self, tavl_rule_id: str) -> dict[str, Any]:
        """Delete GPS HTTP configuration."""
        endpoint = f"/gps/https/tavl_rules/config/{tavl_rule_id}"

        return self._api_client.delete(endpoint)

    def get_gps_geofencing_config(self) -> dict[str, Any]:
        """Get GPS Geofencing configurations."""
        endpoint = "/gps/geofencing/config"

        return self._api_client.get(endpoint)

    def create_gps_geofencing_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create GPS Geofencing configuration."""
        endpoint = "/gps/geofencing/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_gps_geofencing_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update GPS Geofencing configurations."""
        endpoint = "/gps/geofencing/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_gps_geofencing_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Delete GPS Geofencing configurations."""
        return [self.delete_gps_geofencing_config_by_id(geofencing_id) for geofencing_id in config]

    def get_gps_geofencing_config_by_id(self, geofencing_id: str) -> dict[str, Any]:
        """Get GPS Geofencing configuration."""
        endpoint = f"/gps/geofencing/config/{geofencing_id}"

        return self._api_client.get(endpoint)

    def update_gps_geofencing_config_by_id(self, geofencing_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update GPS Geofencing configuration."""
        endpoint = f"/gps/geofencing/config/{geofencing_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_gps_geofencing_config_by_id(self, geofencing_id: str) -> dict[str, Any]:
        """Delete GPS Geofencing configuration."""
        endpoint = f"/gps/geofencing/config/{geofencing_id}"

        return self._api_client.delete(endpoint)

    def get_gps_nmea_rules_config(self) -> dict[str, Any]:
        """Get GPS NMEA Rules configurations."""
        endpoint = "/gps/nmea/rules/config"

        return self._api_client.get(endpoint)

    def update_gps_nmea_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update GPS NMEA Rules configurations."""
        endpoint = "/gps/nmea/rules/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_gps_nmea_rules_config_by_id(self, rule_id: str) -> dict[str, Any]:
        """Get GPS NMEA Rule configuration."""
        endpoint = f"/gps/nmea/rules/config/{rule_id}"

        return self._api_client.get(endpoint)

    def update_gps_nmea_rules_config_by_id(self, rule_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update GPS NMEA Rule configuration."""
        endpoint = f"/gps/nmea/rules/config/{rule_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_gps_nmea_rules_options(self) -> dict[str, Any]:
        """Returns available NMEA sentences."""
        endpoint = "/gps/nmea/rules/options"

        return self._api_client.get(endpoint)

    def get_gps_avl_io_rules_config(self) -> dict[str, Any]:
        """Get GPS AVL IO configurations."""
        endpoint = "/gps/avl/io_rules/config"

        return self._api_client.get(endpoint)

    def create_gps_avl_io_rules_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create GPS AVL IO configuration."""
        endpoint = "/gps/avl/io_rules/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_gps_avl_io_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update GPS AVL IO configurations."""
        endpoint = "/gps/avl/io_rules/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_gps_avl_io_rules_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Delete GPS AVL IO configurations."""
        return [self.delete_gps_avl_io_rules_config_by_id(io_rule_id) for io_rule_id in config]

    def get_gps_avl_io_rules_config_by_id(self, io_rule_id: str) -> dict[str, Any]:
        """Get GPS AVL IO configuration."""
        endpoint = f"/gps/avl/io_rules/config/{io_rule_id}"

        return self._api_client.get(endpoint)

    def update_gps_avl_io_rules_config_by_id(self, io_rule_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update GPS AVL IO configuration."""
        endpoint = f"/gps/avl/io_rules/config/{io_rule_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_gps_avl_io_rules_config_by_id(self, io_rule_id: str) -> dict[str, Any]:
        """Delete GPS AVL IO configuration."""
        endpoint = f"/gps/avl/io_rules/config/{io_rule_id}"

        return self._api_client.delete(endpoint)
