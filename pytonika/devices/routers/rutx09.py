from .router import Router


class RUTX09(Router):
    def __init__(self, base_url: str, *, timeout: float = 10.0, verify: bool = True) -> None:
        super().__init__(base_url, timeout=timeout, verify=verify)

        self.unauthorized = None
        self.authentication = None
        self.serial = None
        self.diagnostics = None
        self.logging = None
        self.troubleshoot = None
        self.bgp = None
        self.sms_gateway = None
        self.internet_connection = None
        self.users = None
        self.nat64 = None
        self.services = None
        self.igmp_proxy = None
        self.firmware = None
        self.fota = None
        self.opc_ua = None
        self.backup = None
        self.date_time = None
        self.sshfs = None
        self.input_output = None
        self.dlna = None
        self.modbus = None
        self.access_control = None
        self.failover = None
        self.console = None
        self.ip_rules = None
        self.routing_tables = None
        self.ip_routes = None
        self.ip_neighbors = None
        self.snmp = None
        self.cloud_of_things = None
        self.cumulocity = None
        self.ntrip = None
        self.package_manager = None
        self.bacnet = None
        self.port_based_vlan = None
        self.zerotier = None
        self.sd_usb_tools = None
        self.mqtt = None
        self.samba = None
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
        self.tailscale = None
        self.ospf = None
        self.data_limit = None
        self.interfaces = None
        self.bfd = None
        self.system = None
        self.recipients = None
        self.pptp = None
        self.dnp3 = None
        self.wireguard = None
        self.qos = None
        self.ports_settings = None
        self.upnp = None
        self.tinc = None
        self.dlms = None
        self.stunnel = None
        self.gps = None
        self.smpp = None
        self.rip = None
        self.sms_utilities = None
        self.messages = None
        self.sim_idle_protection = None
        self.password_policy = None
        self.modem_control = None
        self.firewall = None
        self.dmz = None
        self.attack_prevention = None
        self.nat_offloading = None
        self.dhcp_servers = None
        self.port_mirroring = None
        self.eoip = None
        self.dot1x = None
        self.openconnect = None
        self.apn_database = None
        self.esim = None
        self.operator_lists = None
        self.sim_cards = None
        self.modems = None
        self.dfota = None
        self.data_usage = None
        self.sim_switch = None
        self.traffic_logging = None
        self.overip = None
        self.l2tp = None
        self.l2tpv3 = None
        self.universal_gateway = None
        self.openvpn = None
        self.impulse_counter = None
        self.data_to_server = None
        self.email_relay = None
        self.vrrp = None
        self.wake_on_lan = None
        self.aws = None
        self.udp_broadcast_relay = None
        self.auto_reboot = None
        self.vrf = None
        self.call_utilities = None
        self.ipsec = None
        self.network_usage = None

        self._endpoints.extend([])

    def __getattr__(self, attr: str):
        for endpoint in self._endpoints:
            if hasattr(endpoint, attr):
                return getattr(endpoint, attr)

        return super().__getattr__(attr)
