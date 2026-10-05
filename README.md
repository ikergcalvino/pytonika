# Pytonika

[![PyPI version](https://img.shields.io/pypi/v/pytonika)](https://pypi.org/project/pytonika/)
[![Python versions](https://img.shields.io/pypi/pyversions/pytonika)](https://pypi.org/project/pytonika/)
[![CI](https://github.com/ikergcalvino/pytonika/actions/workflows/ci.yml/badge.svg)](https://github.com/ikergcalvino/pytonika/actions/workflows/ci.yml)
[![License](https://img.shields.io/github/license/ikergcalvino/pytonika)](https://github.com/ikergcalvino/pytonika/blob/main/LICENSE)

**Pytonika** is a typed Python client for the [Teltonika Networks Web API](https://developers.teltonika-networks.com/).
It wraps the API in device-aware classes, so you can automate routers, gateways, access points and switches
without building raw HTTP requests yourself.

> [!IMPORTANT]
> Pytonika is a community project. It is **not affiliated with, endorsed by or supported by Teltonika Networks**.

## Features

- **Device-aware** — each of the 84 supported models exposes exactly the endpoint groups documented for it,
  so your editor autocompletes only what that device actually supports.
- **Broad API coverage** — 160+ endpoint groups and 2,000+ operations, from interfaces and firewall to VPNs,
  mobile, GPS, Modbus and more.
- **Simple session handling** — log in once and the Bearer token is attached to every subsequent request.
- **Fully typed** — ships with `py.typed` and type hints on every public method.
- **Lightweight** — synchronous client built on [httpx](https://www.python-httpx.org/), with no other runtime dependencies.

## Installation

Pytonika requires Python **3.11** or later.

```bash
pip install pytonika
```

## Quick start

```python
from pytonika import RUTX50

with RUTX50("https://192.168.1.1/") as device:
    device.authentication.login("admin", "<password>")

    status = device.firmware.get_firmware_device_status()
    print(status["data"]["version"])

    device.authentication.logout()
```

Using the device as a context manager closes the underlying HTTP connection when the block exits.
Outside a `with` block, call `device.close()` when you are done.

### Connection options

Every device class accepts the same keyword arguments:

| Argument  | Default | Description |
|-----------|---------|-------------|
| `timeout` | `10.0`  | Request timeout in seconds. |
| `verify`  | `True`  | TLS certificate verification. Pass `False` to disable it. |

> [!WARNING]
> Teltonika devices usually ship with a self-signed certificate, so connections fail with `verify=True`
> unless the device has a trusted certificate. Use `verify=False` only on local, trusted networks: it disables
> certificate checks and exposes the connection to man-in-the-middle attacks.
> See the [Security Policy](https://github.com/ikergcalvino/pytonika/blob/main/SECURITY.md) for recommendations.

### Responses

Methods return the API's JSON response as a `dict`, without modification:

```python
response = device.interfaces.get_interfaces_status()

if response["success"]:
    for interface in response["data"]:
        ...
else:
    print(response["errors"])
```

Pytonika does not raise exceptions for API-level errors, so check the `success` field before using `data`.
Network failures (timeouts, connection errors) are raised by `httpx` as usual.

### Generic device classes

If you don't need model-specific endpoints, use the generic class for the device family. It works with any model
of that family and exposes the endpoint groups common to all of them:

```python
from pytonika import Router

with Router("https://192.168.1.1/", timeout=30.0) as router:
    router.authentication.login("admin", "<password>")
    router.wireguard.get_wireguard_config()
```

## Supported devices

Pytonika supports **84 models** across four families. Each family has a generic class, and each model has its own
class with the endpoints specific to it:

| Generic class | Models | Supported models |
|---|---|---|
| `Router` | 62 | ATRM50, CAP700, DAP140, DAP142, DAP145, OTD140, OTD144, OTD500, RUT140, RUT142, RUT145, RUT200, RUT202, RUT204, RUT206, RUT240, RUT241, RUT260, RUT271, RUT276, RUT281, RUT300, RUT301, RUT360, RUT361, RUT901, RUT906, RUT950, RUT951, RUT955, RUT956, RUT976, RUT981, RUT986, RUTC40, RUTC41, RUTC42, RUTC50, RUTM08, RUTM09, RUTM10, RUTM11, RUTM16, RUTM20, RUTM30, RUTM31, RUTM50, RUTM51, RUTM52, RUTM54, RUTM55, RUTM56, RUTM59, RUTX08, RUTX09, RUTX10, RUTX11, RUTX12, RUTX14, RUTX50, RUTXR1, TCR100 |
| `Gateway` | 14 | TRB140, TRB141, TRB142, TRB143, TRB145, TRB160, TRB236, TRB245, TRB246, TRB247, TRB255, TRB256, TRB500, TRB501 |
| `AccessPoint` | 3 | TAP100, TAP200, TAP400 |
| `Switch` | 5 | SWM280, SWM281, SWM282, TSW202, TSW212 |

Each model's endpoint set follows the official API reference for the latest firmware documented for that model.
A few models are documented for older firmware lines (for example RUT240, RUT950 and RUT955), and their classes
reflect that.

Missing a device? [Open a device request](https://github.com/ikergcalvino/pytonika/issues/new/choose).

## Endpoints

Each endpoint group from the official API reference is available as an attribute named after the group:

| Area | Attributes |
|---|---|
| Session | `authentication`, `unauthorized` |
| System and administration | `system`, `users`, `access_control`, `backup`, `date_time`, `logging` |
| Firmware | `firmware`, `fota` |
| Networking | `interfaces`, `dhcp_servers`, `firewall`, `ip_routes`, `failover` |
| VPN | `wireguard`, `openvpn`, `ipsec`, `zerotier`, `tailscale` |
| Mobile and SMS | `modems`, `sim_cards`, `messages`, `sms_utilities` |
| Industrial and IoT | `gps`, `input_output`, `modbus`, `serial`, `mqtt` |

Method names follow the structure of the API:

| Pattern | Example | HTTP |
|---|---|---|
| `get_<resource>` / `get_<resource>_by_id` | `get_wireguard_config_by_id(id)` | `GET` |
| `create_<resource>` | `create_wireguard_config(config)` | `POST` |
| `update_<resource>` / `update_<resource>_by_id` | `update_wireguard_config_by_id(id, config)` | `PUT` |
| `delete_<resource>` / `delete_<resource>_by_id` | `delete_wireguard_config_by_id(id)` | `DELETE` |
| `<group>_actions_<action>` | `wireguard_actions_generate_keys()` | `POST` |

The full list of groups is in [`pytonika/endpoints/`](https://github.com/ikergcalvino/pytonika/tree/main/pytonika/endpoints).
For request payloads and response schemas, see the [Teltonika Web API reference](https://developers.teltonika-networks.com/).

## Project status

Pytonika is in **beta** (pre-1.0). The public interface may change between minor releases; changes are
documented in the [release notes](https://github.com/ikergcalvino/pytonika/releases).

## Contributing

Bug reports, device and endpoint requests and pull requests are welcome.
See the [Contributing guidelines](https://github.com/ikergcalvino/pytonika/blob/main/CONTRIBUTING.md) to get started.

## Security

Please do not report vulnerabilities through public issues.
See the [Security Policy](https://github.com/ikergcalvino/pytonika/blob/main/SECURITY.md) for how to report them privately.

## License

Distributed under the [MIT License](https://github.com/ikergcalvino/pytonika/blob/main/LICENSE).
