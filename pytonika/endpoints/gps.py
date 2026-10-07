from typing import Any

from ._endpoint import Endpoint


class GPS(Endpoint):
    def get_gps_avl_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get GPS AVL General configurations."""
        return self._client.request("GET", "/gps/avl/config", params={"all_options": all_options})

    def update_gps_avl_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update GPS AVL General configurations."""
        return self._client.request("PUT", "/gps/avl/config", json={"data": config})

    def get_gps_avl_config_by_id(self, avl_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get GPS AVL General configuration."""
        return self._client.request("GET", f"/gps/avl/config/{avl_id}", params={"all_options": all_options})

    def update_gps_avl_config_by_id(self, avl_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update GPS AVL General configuration."""
        return self._client.request("PUT", f"/gps/avl/config/{avl_id}", json={"data": config})

    def get_gps_avl_io_rules_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get GPS AVL IO configurations."""
        return self._client.request("GET", "/gps/avl/io_rules/config", params={"all_options": all_options})

    def create_gps_avl_io_rules_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create GPS AVL IO configuration."""
        return self._client.request("POST", "/gps/avl/io_rules/config", json={"data": config})

    def update_gps_avl_io_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update GPS AVL IO configurations."""
        return self._client.request("PUT", "/gps/avl/io_rules/config", json={"data": config})

    def delete_gps_avl_io_rules_config(self, config: list[str]) -> dict[str, Any]:
        """Delete GPS AVL IO configurations."""
        return self._client.request("DELETE", "/gps/avl/io_rules/config", json={"data": config})

    def get_gps_avl_io_rules_config_by_id(self, io_rule_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get GPS AVL IO configuration."""
        return self._client.request(
            "GET", f"/gps/avl/io_rules/config/{io_rule_id}", params={"all_options": all_options}
        )

    def update_gps_avl_io_rules_config_by_id(self, io_rule_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update GPS AVL IO configuration."""
        return self._client.request("PUT", f"/gps/avl/io_rules/config/{io_rule_id}", json={"data": config})

    def delete_gps_avl_io_rules_config_by_id(self, io_rule_id: str) -> dict[str, Any]:
        """Delete GPS AVL IO configuration."""
        return self._client.request("DELETE", f"/gps/avl/io_rules/config/{io_rule_id}")

    def get_gps_avl_main_rules_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get GPS AVL Main configurations."""
        return self._client.request("GET", "/gps/avl/main_rules/config", params={"all_options": all_options})

    def update_gps_avl_main_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update GPS AVL Main configurations."""
        return self._client.request("PUT", "/gps/avl/main_rules/config", json={"data": config})

    def get_gps_avl_main_rules_config_by_id(
        self, main_rule_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Get GPS AVL Main configuration."""
        return self._client.request(
            "GET", f"/gps/avl/main_rules/config/{main_rule_id}", params={"all_options": all_options}
        )

    def update_gps_avl_main_rules_config_by_id(self, main_rule_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update GPS AVL Main configuration."""
        return self._client.request("PUT", f"/gps/avl/main_rules/config/{main_rule_id}", json={"data": config})

    def get_gps_avl_secondary_rules_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get GPS AVL Rules configurations."""
        return self._client.request("GET", "/gps/avl/secondary_rules/config", params={"all_options": all_options})

    def create_gps_avl_secondary_rules_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create GPS AVL Rules configuration."""
        return self._client.request("POST", "/gps/avl/secondary_rules/config", json={"data": config})

    def update_gps_avl_secondary_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update GPS AVL Rules configurations."""
        return self._client.request("PUT", "/gps/avl/secondary_rules/config", json={"data": config})

    def delete_gps_avl_secondary_rules_config(self, config: list[str]) -> dict[str, Any]:
        """Delete GPS AVL Rules configurations."""
        return self._client.request("DELETE", "/gps/avl/secondary_rules/config", json={"data": config})

    def get_gps_avl_secondary_rules_config_by_id(
        self, secondary_rule_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Get GPS AVL Rules configuration."""
        return self._client.request(
            "GET", f"/gps/avl/secondary_rules/config/{secondary_rule_id}", params={"all_options": all_options}
        )

    def update_gps_avl_secondary_rules_config_by_id(
        self, secondary_rule_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Update GPS AVL Rules configuration."""
        return self._client.request(
            "PUT", f"/gps/avl/secondary_rules/config/{secondary_rule_id}", json={"data": config}
        )

    def delete_gps_avl_secondary_rules_config_by_id(self, secondary_rule_id: str) -> dict[str, Any]:
        """Delete GPS AVL Rules configuration."""
        return self._client.request("DELETE", f"/gps/avl/secondary_rules/config/{secondary_rule_id}")

    def get_gps_avl_status(self) -> dict[str, Any]:
        """Returns GPS AVL status."""
        return self._client.request("GET", "/gps/avl/status")

    def get_gps_avl_tavl_rules_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get GPS TAVL Rules configurations."""
        return self._client.request("GET", "/gps/avl/tavl_rules/config", params={"all_options": all_options})

    def create_gps_avl_tavl_rules_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create GPS TAVL rule configuration."""
        return self._client.request("POST", "/gps/avl/tavl_rules/config", json={"data": config})

    def update_gps_avl_tavl_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update GPS TAVL Rules configurations."""
        return self._client.request("PUT", "/gps/avl/tavl_rules/config", json={"data": config})

    def delete_gps_avl_tavl_rules_config(self, config: list[str]) -> dict[str, Any]:
        """Delete GPS TAVL rules configurations."""
        return self._client.request("DELETE", "/gps/avl/tavl_rules/config", json={"data": config})

    def get_gps_avl_tavl_rules_config_by_id(
        self, tavl_rule_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Get GPS TAVL Rules configuration."""
        return self._client.request(
            "GET", f"/gps/avl/tavl_rules/config/{tavl_rule_id}", params={"all_options": all_options}
        )

    def update_gps_avl_tavl_rules_config_by_id(self, tavl_rule_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update GPS TAVL Rules configuration."""
        return self._client.request("PUT", f"/gps/avl/tavl_rules/config/{tavl_rule_id}", json={"data": config})

    def delete_gps_avl_tavl_rules_config_by_id(self, tavl_rule_id: str) -> dict[str, Any]:
        """Delete GPS TAVL Rule configuration."""
        return self._client.request("DELETE", f"/gps/avl/tavl_rules/config/{tavl_rule_id}")

    def get_gps_geofencing_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get GPS Geofencing configurations."""
        return self._client.request("GET", "/gps/geofencing/config", params={"all_options": all_options})

    def create_gps_geofencing_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create GPS Geofencing configuration."""
        return self._client.request("POST", "/gps/geofencing/config", json={"data": config})

    def update_gps_geofencing_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update GPS Geofencing configurations."""
        return self._client.request("PUT", "/gps/geofencing/config", json={"data": config})

    def delete_gps_geofencing_config(self, config: list[str]) -> dict[str, Any]:
        """Delete GPS Geofencing configurations."""
        return self._client.request("DELETE", "/gps/geofencing/config", json={"data": config})

    def get_gps_geofencing_config_by_id(self, geofencing_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get GPS Geofencing configuration."""
        return self._client.request(
            "GET", f"/gps/geofencing/config/{geofencing_id}", params={"all_options": all_options}
        )

    def update_gps_geofencing_config_by_id(self, geofencing_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update GPS Geofencing configuration."""
        return self._client.request("PUT", f"/gps/geofencing/config/{geofencing_id}", json={"data": config})

    def delete_gps_geofencing_config_by_id(self, geofencing_id: str) -> dict[str, Any]:
        """Delete GPS Geofencing configuration."""
        return self._client.request("DELETE", f"/gps/geofencing/config/{geofencing_id}")

    def get_gps_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get GPS General configuration."""
        return self._client.request("GET", "/gps/global", params={"all_options": all_options})

    def update_gps_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Update GPS General configuration."""
        return self._client.request("PUT", "/gps/global", json={"data": config})

    def get_gps_https_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get GPS HTTP General configurations."""
        return self._client.request("GET", "/gps/https/config", params={"all_options": all_options})

    def update_gps_https_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update GPS HTTP General configurations."""
        return self._client.request("PUT", "/gps/https/config", json={"data": config})

    def get_gps_https_config_by_id(self, http_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get GPS HTTP General configuration."""
        return self._client.request("GET", f"/gps/https/config/{http_id}", params={"all_options": all_options})

    def update_gps_https_config_by_id(self, http_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update GPS HTTP General configuration."""
        return self._client.request("PUT", f"/gps/https/config/{http_id}", json={"data": config})

    def get_gps_https_status(self) -> dict[str, Any]:
        """Returns GPS HTTPS status."""
        return self._client.request("GET", "/gps/https/status")

    def get_gps_https_tavl_rules_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get GPS HTTP configurations."""
        return self._client.request("GET", "/gps/https/tavl_rules/config", params={"all_options": all_options})

    def create_gps_https_tavl_rules_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create GPS HTTP configuration."""
        return self._client.request("POST", "/gps/https/tavl_rules/config", json={"data": config})

    def update_gps_https_tavl_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update GPS HTTP configurations."""
        return self._client.request("PUT", "/gps/https/tavl_rules/config", json={"data": config})

    def delete_gps_https_tavl_rules_config(self, config: list[str]) -> dict[str, Any]:
        """Delete GPS HTTP configurations."""
        return self._client.request("DELETE", "/gps/https/tavl_rules/config", json={"data": config})

    def get_gps_https_tavl_rules_config_by_id(
        self, tavl_rule_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Get GPS HTTP configuration."""
        return self._client.request(
            "GET", f"/gps/https/tavl_rules/config/{tavl_rule_id}", params={"all_options": all_options}
        )

    def update_gps_https_tavl_rules_config_by_id(self, tavl_rule_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update GPS HTTP configuration."""
        return self._client.request("PUT", f"/gps/https/tavl_rules/config/{tavl_rule_id}", json={"data": config})

    def delete_gps_https_tavl_rules_config_by_id(self, tavl_rule_id: str) -> dict[str, Any]:
        """Delete GPS HTTP configuration."""
        return self._client.request("DELETE", f"/gps/https/tavl_rules/config/{tavl_rule_id}")

    def get_gps_nmea_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get GPS NMEA configurations."""
        return self._client.request("GET", "/gps/nmea/config", params={"all_options": all_options})

    def update_gps_nmea_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update GPS NMEA configurations."""
        return self._client.request("PUT", "/gps/nmea/config", json={"data": config})

    def get_gps_nmea_config_by_id(self, nmea_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get GPS NMEA configuration."""
        return self._client.request("GET", f"/gps/nmea/config/{nmea_id}", params={"all_options": all_options})

    def update_gps_nmea_config_by_id(self, nmea_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update GPS NMEA configuration."""
        return self._client.request("PUT", f"/gps/nmea/config/{nmea_id}", json={"data": config})

    def get_gps_nmea_rules_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get GPS NMEA Rules configurations."""
        return self._client.request("GET", "/gps/nmea/rules/config", params={"all_options": all_options})

    def update_gps_nmea_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update GPS NMEA Rules configurations."""
        return self._client.request("PUT", "/gps/nmea/rules/config", json={"data": config})

    def get_gps_nmea_rules_config_by_id(self, rule_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get GPS NMEA Rule configuration."""
        return self._client.request("GET", f"/gps/nmea/rules/config/{rule_id}", params={"all_options": all_options})

    def update_gps_nmea_rules_config_by_id(self, rule_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update GPS NMEA Rule configuration."""
        return self._client.request("PUT", f"/gps/nmea/rules/config/{rule_id}", json={"data": config})

    def get_gps_nmea_rules_options(self) -> dict[str, Any]:
        """Returns available NMEA sentences."""
        return self._client.request("GET", "/gps/nmea/rules/options")

    def get_gps_nmea_serial_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns GPS NMEA Serial Port configurations."""
        return self._client.request("GET", "/gps/nmea/serial/config", params={"all_options": all_options})

    def create_gps_nmea_serial_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates GPS NMEA Serial Port configuration."""
        return self._client.request("POST", "/gps/nmea/serial/config", json={"data": config})

    def update_gps_nmea_serial_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update GPS NMEA Serial Port configurations."""
        return self._client.request("PUT", "/gps/nmea/serial/config", json={"data": config})

    def delete_gps_nmea_serial_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified GPS NMEA Serial Port configurations."""
        return self._client.request("DELETE", "/gps/nmea/serial/config", json={"data": config})

    def get_gps_nmea_serial_config_by_id(self, serial_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns GPS NMEA Serial Port configuration."""
        return self._client.request("GET", f"/gps/nmea/serial/config/{serial_id}", params={"all_options": all_options})

    def update_gps_nmea_serial_config_by_id(self, serial_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update GPS NMEA Serial Port configuration."""
        return self._client.request("PUT", f"/gps/nmea/serial/config/{serial_id}", json={"data": config})

    def delete_gps_nmea_serial_config_by_id(self, serial_id: str) -> dict[str, Any]:
        """Deletes the specified NMEA Serial Port configuration."""
        return self._client.request("DELETE", f"/gps/nmea/serial/config/{serial_id}")

    def get_gps_nmea_status(self) -> dict[str, Any]:
        """Returns GPS NMEA status."""
        return self._client.request("GET", "/gps/nmea/status")

    def get_gps_position_status(self) -> dict[str, Any]:
        """Get GPS position."""
        return self._client.request("GET", "/gps/position/status")

    def get_gps_status(self) -> dict[str, Any]:
        """Returns GPS service status."""
        return self._client.request("GET", "/gps/status")
