# Pytonika

[![PyPI version](https://img.shields.io/pypi/v/pytonika)](https://pypi.org/project/pytonika/)
[![Python versions](https://img.shields.io/pypi/pyversions/pytonika)](https://pypi.org/project/pytonika/)
[![License](https://img.shields.io/github/license/ikergcalvino/pytonika)](LICENSE)

Pytonika is a lightweight Python client library to interact with **Teltonika Networks devices** via their Web API.
It provides simple device abstractions and grouped endpoint interfaces to make automation and scripting straightforward.

> [!IMPORTANT]
> Pytonika is **not an official Teltonika library**.
> This project is maintained by the community and is not affiliated with or endorsed by Teltonika Networks.

## Why Pytonika?

Instead of crafting raw HTTP requests against the Teltonika Web API, Pytonika gives you:

- **Device-aware wrappers** for routers, gateways, access points and switches with model-specific endpoints.
- **Clean, Pythonic interface** — authenticate once and call methods directly.
- **Lightweight** — synchronous HTTP client built on top of [httpx](https://www.python-httpx.org/) with zero extra dependencies.

## Installation

### Requirements

- Python **3.10+**
- [httpx](https://pypi.org/project/httpx/) >= **0.28.1**

### Install from PyPI

```bash
pip install pytonika
```

## Quick start

```python
from pytonika import Router

router = Router("http://192.168.1.1/")

# Authenticate
router.authentication.login("admin", "admin01")

# Query device info
router.firmware.get_firmware_device_status()

# Manage WireGuard
router.wireguard.get_wireguard_config()

# Check interfaces
router.interfaces.get_interfaces_status()

# Logout when done
router.authentication.logout()
```

You can also target a specific device model for access to model-specific endpoints:

```python
from pytonika import RUTX50

device = RUTX50("http://192.168.1.1/")
device.authentication.login("admin", "admin01")
```

## Supported devices

Pytonika provides wrappers for a wide range of Teltonika devices. You can use the generic class per device type or a model-specific subclass.

### Routers

| Generic class | Models |
|---|---|
| `Router` | DAP140, DAP142, DAP145, OTD140, OTD144, OTD500, RUT140, RUT142, RUT200, RUT206, RUT240, RUT241, RUT260, RUT271, RUT300, RUT301, RUT360, RUT361, RUT901, RUT906, RUT950, RUT951, RUT955, RUT956, RUT976, RUTC50, RUTM08, RUTM09, RUTM10, RUTM11, RUTM30, RUTM31, RUTM50, RUTM51, RUTM52, RUTM54, RUTM55, RUTM56, RUTM59, RUTX08, RUTX09, RUTX10, RUTX11, RUTX12, RUTX14, RUTX50, RUTXR1, TCR100 |

### Gateways

| Generic class | Models |
|---|---|
| `Gateway` | TRB140, TRB141, TRB142, TRB143, TRB145, TRB160, TRB245, TRB246, TRB247, TRB255, TRB256, TRB500, TRB501 |

### Access Points

| Generic class | Models |
|---|---|
| `AccessPoint` | TAP100, TAP200 |

### Switches

| Generic class | Models |
|---|---|
| `Switch` | SWM280, SWM281, SWM282, TSW202, TSW212 |

## Available endpoints

| Endpoint | Status | Description |
|---|---|---|
| `authentication` | ✅ Ready | Login, logout, session status |
| `wireguard` | ✅ Ready | WireGuard tunnels and peers configuration |
| `firewall` | ✅ Ready | Connections status, port forwards |
| `users` | ✅ Ready | User management |
| `interfaces` | ✅ Ready | Interface configuration and status |
| `firmware` | ✅ Ready | Firmware status, FOTA, upgrade |
| `system` | ✅ Ready | Reboot, first login password change |
| `unauthorized` | ✅ Ready | Unauthorized status |
| `access_control` | 🚧 Planned | — |
| `auto_reboot` | 🚧 Planned | — |
| `backup` | 🚧 Planned | — |
| `date_time` | 🚧 Planned | — |
| `diagnostics` | 🚧 Planned | — |
| `events_log` | 🚧 Planned | — |
| `modbus` | 🚧 Planned | — |
| `network` | 🚧 Planned | — |
| `profiles` | 🚧 Planned | — |
| `rms` | 🚧 Planned | — |
| `wireless` | 🚧 Planned | — |
| _...and more_ | 🚧 Planned | See [endpoints/](pytonika/endpoints/) |

Contributions to implement planned endpoints are very welcome! See [Contributing](CONTRIBUTING.md).

## Development

```bash
# Clone the repository
git clone https://github.com/ikergcalvino/pytonika.git
cd pytonika

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install in editable mode with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run linter
ruff check .
```

## Contributing

Contributions, bug reports and feature requests are welcome!
Check out the [Contributing guidelines](CONTRIBUTING.md) to get started.

## License

[MIT License](LICENSE)
