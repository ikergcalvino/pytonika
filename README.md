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

## Highlights

- **The whole Web API**: one method per operation of the official reference, including file uploads and downloads.
- **Device-aware**: each of the 88 supported models exposes the endpoint groups documented for it, so your editor
  autocompletes only what that device supports.
- **Typed and lightweight**: type hints on every method, and [httpx](https://www.python-httpx.org/) as its only
  dependency.

## Installation

Pytonika requires Python 3.11 or later.

```bash
pip install pytonika
```

## Quick start

```python
import os

from pytonika import RUTX50

with RUTX50("https://192.168.1.1") as device:
    device.authentication.login("admin", os.environ["TELTONIKA_PASSWORD"])

    status = device.firmware.get_firmware_device_status()
    print(status["data"]["version"])

    device.authentication.logout()
```

The `with` block closes the connection when it exits; outside it, call `device.close()`.
The Bearer token returned by `login()` is sent with every request until `logout()`.

> [!TIP]
> Not sure which model or firmware a device has? The unauthenticated status endpoint tells you, without logging in:
>
> ```python
> from pytonika import Router
>
> with Router("https://192.168.1.1") as router:
>     info = router.unauthorized.get_unauthorized_status()["data"]
>     print(info["device_model"], info["api_version"])  # RUT956 1.16.3
> ```

## Usage

### From the Teltonika documentation to Pytonika

Pytonika mirrors the [Teltonika Web API reference](https://developers.teltonika-networks.com/): each documentation
page is a device attribute, and each operation is a method named after its path.

| Teltonika Web API reference | Pytonika |
|---|---|
| Page "WireGuard" | `device.wireguard` |
| `GET /wireguard/config/{id}` | `device.wireguard.get_wireguard_config_by_id(wireguard_id)` |
| `POST /wireguard/config` with body `{"data": {...}}` | `device.wireguard.create_wireguard_config({...})` |
| `POST /wireguard/actions/generate_keys` | `device.wireguard.wireguard_actions_generate_keys()` |

Method names follow the same pattern everywhere:

| Pattern | HTTP |
|---|---|
| `get_<path>` / `get_<path>_by_id` | `GET` |
| `create_<path>` | `POST` |
| `update_<path>` / `update_<path>_by_id` | `PUT` |
| `delete_<path>` / `delete_<path>_by_id` | `DELETE` |
| `upload_<path>` | `POST` with a file |
| `<group>_actions_<action>` | `POST` to an action |

For every endpoint group and method, see the
[endpoint reference](https://github.com/ikergcalvino/pytonika/blob/main/docs/endpoints.md). For request payloads
and response fields, see the Teltonika Web API reference.

### Responses and errors

Methods return the device's JSON response as a `dict`, without modification.

> [!NOTE]
> Pytonika does not raise exceptions for API errors: check `success` before using `data`.

```python
response = device.interfaces.get_interfaces_status()

if response["success"]:
    for interface in response["data"]:
        print(interface["id"], interface["is_up"])
else:
    print(response["errors"])
```

Network failures, such as timeouts or an unreachable device, raise the usual
[httpx exceptions](https://www.python-httpx.org/exceptions/) (`httpx.TimeoutException`, `httpx.ConnectError`, …).

### Query parameters, uploads and downloads

Optional query parameters are keyword arguments, sent only when you pass them:

```python
device.wireguard.get_wireguard_config(all_options=True)
```

Methods that upload a file take a `file` argument: bytes, an open binary file or a `(filename, content)` pair.
Methods that download a file return its content as `bytes`, or the error `dict` if the device refuses:

```python
from pathlib import Path

with open("ca.pem", "rb") as certificate:
    device.certificates.upload_certificates_config(("ca.pem", certificate))

device.backup.backup_actions_generate()
backup = device.backup.backup_actions_download()

if isinstance(backup, bytes):
    Path("backup.tar.gz").write_bytes(backup)
```

### Generic device classes

`Router`, `Gateway`, `AccessPoint` and `Switch` work with any model of their family and expose the endpoint groups
common to all of them. Use them when your code does not depend on a specific model:

```python
from pytonika import Router

with Router("https://192.168.1.1") as router:
    ...
```

### Connection options

Every device class accepts the same keyword arguments:

| Argument | Default | Description |
|---|---|---|
| `timeout` | `10.0` | Request timeout in seconds. |
| `verify` | `True` | TLS verification: `True`, `False`, or an `ssl.SSLContext` with your own certificate authority. |

> [!WARNING]
> Teltonika devices ship with a self-signed certificate, so connecting with the default `verify=True` fails until
> the device has a trusted certificate. `verify=False` disables certificate checks and exposes the connection to
> man-in-the-middle attacks: use it only on local, trusted networks. See the
> [Security Policy](https://github.com/ikergcalvino/pytonika/blob/main/SECURITY.md#using-pytonika-securely) for how to
> keep verification enabled.

## Supported devices

| Family | Generic class | Models | Firmware |
|---|---|---|---|
| Routers | `Router` | 66: RUT, RUTX, RUTM, RUTC, OTD, DAP, CAP, ATRM and TCR series | RutOS 7.26 |
| Gateways | `Gateway` | 14: TRB series | RutOS 7.26 |
| Access points | `AccessPoint` | 3: TAP series | RutOS 7.26 |
| Switches | `Switch` | 5: TSW and SWM series | SwOS 1.10.4 |

Endpoints follow the latest firmware documented for each model. A few models are documented only for older
firmware lines.

> [!NOTE]
> Operations added in a newer firmware than your device's return an error from the device.

The [device reference](https://github.com/ikergcalvino/pytonika/blob/main/docs/devices.md) lists every model,
its reference firmware and its endpoint groups. Missing a device?
[Open a device request](https://github.com/ikergcalvino/pytonika/issues/new/choose).

## Project

> [!CAUTION]
> Pytonika is in **beta** (pre-1.0): the public interface may change between minor releases. Check the
> [release notes](https://github.com/ikergcalvino/pytonika/releases) before upgrading.

- **Contributing:** bug reports, device and endpoint requests and pull requests are welcome. See the
  [contributing guidelines](https://github.com/ikergcalvino/pytonika/blob/main/CONTRIBUTING.md).
- **Security:** report vulnerabilities privately, as described in the
  [security policy](https://github.com/ikergcalvino/pytonika/blob/main/SECURITY.md).
- **License:** [MIT](https://github.com/ikergcalvino/pytonika/blob/main/LICENSE).
