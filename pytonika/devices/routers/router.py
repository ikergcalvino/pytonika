from ..._client import APIClient
from ...endpoints import *


class Router():
    def __init__(self, base_url: str, *, timeout: float = 10.0, verify: bool = True) -> None:
        self._client = APIClient(base_url, timeout=timeout, verify=verify)

        self.unauthorized = Unauthorized(self._client)
        self.authentication = Authentication(self._client)
        self.diagnostics = None
        self.logging = None
        self.troubleshoot = None
        self.bgp = None
        self.internet_connection = None
        self.users = Users(self._client)
        self.nat64 = None
        self.services = None
        self.igmp_proxy = None
        self.firmware = Firmware(self._client)
        self.fota = None
        self.opc_ua = None
        self.backup = None
        self.date_time = None
        self.sshfs = None
        self.modbus = None
        self.access_control = None
        self.failover = None
        self.ip_rules = None
        self.routing_tables = None
        self.ip_routes = None
        self.ip_neighbors = None
        self.snmp = None
        self.cloud_of_things = None
        self.cumulocity = None
        self.package_manager = None
        self.zerotier = None
        self.mqtt = None
        self.profiles = None
        self.azure_iot_hub = None
        self.certificates = None
        self.event_juggler = None
        self.tr_069 = None
        self.sstp = None
        self.dns = None
        self.topology = None
        self.speedtest = None
        self.eigrp = None
        self.dmvpn = None
        self.hotspot = None
        self.network = None
        self.custom_scripts = None
        self.web_filter = None
        self.events_reporting = None
        self.nhrp = None
        self.sqm = None
        self.ddns = None
        self.thingworx = None
        self.rms = None
        self.events_log = None
        self.gre = None
        self.ospf = None
        self.interfaces = Interfaces(self._client)
        self.bfd = None
        self.system = None
        self.recipients = None
        self.pptp = None
        self.dnp3 = None
        self.wireguard = WireGuard(self._client)
        self.qos = None
        self.upnp = None
        self.tinc = None
        self.dlms = None
        self.stunnel = None
        self.rip = None
        self.password_policy = None
        self.firewall = Firewall(self._client)
        self.dmz = None
        self.attack_prevention = None
        self.nat_offloading = None
        self.dhcp_servers = None
        self.eoip = None
        self.traffic_logging = None
        self.l2tp = None
        self.l2tpv3 = None
        self.openvpn = None
        self.data_to_server = None
        self.email_relay = None
        self.vrrp = None
        self.wake_on_lan = None
        self.aws = None
        self.udp_broadcast_relay = None
        self.auto_reboot = None
        self.vrf = None
        self.ipsec = None

        self._endpoints = [
            self.unauthorized,
            self.authentication,
            self.diagnostics,
            self.logging,
            self.troubleshoot,
            self.bgp,
            self.internet_connection,
            self.users,
            self.nat64,
            self.services,
            self.igmp_proxy,
            self.firmware,
            self.fota,
            self.opc_ua,
            self.backup,
            self.date_time,
            self.sshfs,
            self.modbus,
            self.access_control,
            self.failover,
            self.ip_rules,
            self.routing_tables,
            self.ip_routes,
            self.ip_neighbors,
            self.snmp,
            self.cloud_of_things,
            self.cumulocity,
            self.package_manager,
            self.zerotier,
            self.mqtt,
            self.profiles,
            self.azure_iot_hub,
            self.certificates,
            self.event_juggler,
            self.tr_069,
            self.sstp,
            self.dns,
            self.topology,
            self.speedtest,
            self.eigrp,
            self.dmvpn,
            self.hotspot,
            self.network,
            self.custom_scripts,
            self.web_filter,
            self.events_reporting,
            self.nhrp,
            self.sqm,
            self.ddns,
            self.thingworx,
            self.rms,
            self.events_log,
            self.gre,
            self.ospf,
            self.interfaces,
            self.bfd,
            self.system,
            self.recipients,
            self.pptp,
            self.dnp3,
            self.wireguard,
            self.qos,
            self.upnp,
            self.tinc,
            self.dlms,
            self.stunnel,
            self.rip,
            self.password_policy,
            self.firewall,
            self.dmz,
            self.attack_prevention,
            self.nat_offloading,
            self.dhcp_servers,
            self.eoip,
            self.traffic_logging,
            self.l2tp,
            self.l2tpv3,
            self.openvpn,
            self.data_to_server,
            self.email_relay,
            self.vrrp,
            self.wake_on_lan,
            self.aws,
            self.udp_broadcast_relay,
            self.auto_reboot,
            self.vrf,
            self.ipsec,
        ]

    def __getattr__(self, attr: str):
        for endpoint in self._endpoints:
            if hasattr(endpoint, attr):
                return getattr(endpoint, attr)

        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{attr}'"
        )
