import ssl
from typing import Self

from ..._client import APIClient
from ...endpoints import *


class AccessPoint:
    def __init__(self, base_url: str, *, timeout: float = 10.0, verify: bool | ssl.SSLContext = True) -> None:
        self._client = APIClient(base_url, timeout=timeout, verify=verify)

        self.access_control = AccessControl(self._client)
        self.authentication = Authentication(self._client)
        self.auto_reboot = AutoReboot(self._client)
        self.backup = Backup(self._client)
        self.bgp = BGP(self._client)
        self.date_time = DateTime(self._client)
        self.diagnostics = Diagnostics(self._client)
        self.dot1x = Dot1X(self._client)
        self.events_log = EventsLog(self._client)
        self.firmware = Firmware(self._client)
        self.fota = FOTA(self._client)
        self.iec_60870_5_client = IEC608705Client(self._client)
        self.iec_60870_5_server = IEC608705Server(self._client)
        self.integrity = Integrity(self._client)
        self.interfaces = Interfaces(self._client)
        self.jwt_login = JWTLogin(self._client)
        self.logging = Logging(self._client)
        self.modbus = Modbus(self._client)
        self.network = Network(self._client)
        self.password_policy = PasswordPolicy(self._client)
        self.profiles = Profiles(self._client)
        self.refresh = Refresh(self._client)
        self.rms = RMS(self._client)
        self.site_manager_client_status = SiteManagerClientStatus(self._client)
        self.sso = SSO(self._client)
        self.sso_login = SSOLogin(self._client)
        self.system = System(self._client)
        self.troubleshoot = Troubleshoot(self._client)
        self.two_fa = TwoFA(self._client)
        self.two_fa_login = TwoFALogin(self._client)
        self.unauthorized = Unauthorized(self._client)
        self.universal_gateway = UniversalGateway(self._client)
        self.users = Users(self._client)
        self.wifi_scanner = WiFiScanner(self._client)
        self.wireless = Wireless(self._client)

    def __repr__(self) -> str:
        return f"<{type(self).__name__} {self._client.base_url}>"

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()

    def close(self) -> None:
        self._client.close()
