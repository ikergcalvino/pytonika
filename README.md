# Pytonika

[![PyPI version](https://img.shields.io/pypi/v/pytonika)](https://pypi.org/project/pytonika/)
[![Python versions](https://img.shields.io/pypi/pyversions/pytonika)](https://pypi.org/project/pytonika/)
[![CI](https://github.com/ikergcalvino/pytonika/actions/workflows/ci.yml/badge.svg)](https://github.com/ikergcalvino/pytonika/actions/workflows/ci.yml)
[![License](https://img.shields.io/github/license/ikergcalvino/pytonika)](LICENSE)

Pytonika is a lightweight Python client library for the **Teltonika Networks Web API**.
It provides device-aware wrappers and grouped endpoint interfaces to make automation and scripting straightforward.

> [!IMPORTANT]
> Pytonika is **not an official Teltonika library**.
> This project is maintained by the community and is not affiliated with or endorsed by Teltonika Networks.

## Why Pytonika?

Instead of crafting raw HTTP requests against the Teltonika Web API, Pytonika gives you:

- **Device-aware wrappers** — every supported model exposes the endpoint set documented for it in the [official API reference](https://developers.teltonika-networks.com/).
- **Clean, Pythonic interface** — authenticate once and call methods directly; the session token is handled for you.
- **Full API coverage** — 160+ endpoint groups, from VPN and firewall to SMS, GPS and Modbus.
- **Lightweight** — synchronous HTTP client built on [httpx](https://www.python-httpx.org/), with no other dependencies.

## Installation

Requires Python **3.10+**:

```bash
pip install pytonika
```

## Quick start

```python
from pytonika import RUTX50

device = RUTX50("https://192.168.1.1/", verify=False)  # self-signed cert on the device

# Authenticate — the Bearer token is stored and reused automatically
device.authentication.login("admin", "admin01")

# Query the device
status = device.firmware.get_firmware_device_status()
print(status["data"]["version"])

# Manage configuration
device.wireguard.get_wireguard_config()
device.interfaces.get_interfaces_status()

# Log out when done
device.authentication.logout()
```

Every method returns the raw API response as a `dict`, typically shaped as
`{"success": True, "data": ...}` or `{"success": False, "errors": [...]}`.

If you don't care about model-specific endpoints, the generic classes (`Router`,
`Gateway`, `AccessPoint`, `Switch`) work with any device of that type:

```python
from pytonika import Router

router = Router("http://192.168.1.1/", timeout=10.0)
```

## Supported devices

Use the generic class per device type or a model-specific subclass:

| Generic class | Models |
|---|---|
| `Router` | ATRM50, CAP700, DAP140, DAP142, DAP145, OTD140, OTD144, OTD500, RUT140, RUT142, RUT145, RUT200, RUT202, RUT204, RUT206, RUT240, RUT241, RUT260, RUT271, RUT276, RUT281, RUT300, RUT301, RUT360, RUT361, RUT901, RUT906, RUT950, RUT951, RUT955, RUT956, RUT976, RUT981, RUT986, RUTC40, RUTC41, RUTC42, RUTC50, RUTM08, RUTM09, RUTM10, RUTM11, RUTM16, RUTM20, RUTM30, RUTM31, RUTM50, RUTM51, RUTM52, RUTM54, RUTM55, RUTM56, RUTM59, RUTX08, RUTX09, RUTX10, RUTX11, RUTX12, RUTX14, RUTX50, RUTXR1, TCR100 |
| `Gateway` | TRB140, TRB141, TRB142, TRB143, TRB145, TRB160, TRB236, TRB245, TRB246, TRB247, TRB255, TRB256, TRB500, TRB501 |
| `AccessPoint` | TAP100, TAP200, TAP400 |
| `Switch` | SWM280, SWM281, SWM282, TSW202, TSW212 |

Each model class exposes exactly the endpoints documented for its latest firmware,
so your editor can autocomplete what a given device actually supports.

## Endpoints

Every endpoint group from the official API reference is available as an attribute
named after the group — a few examples:

| Attribute | Description |
|---|---|
| `authentication` | Login, logout, session status |
| `firmware`, `fota` | Firmware status, upgrades, FOTA |
| `interfaces`, `dhcp_servers`, `firewall` | Networking essentials |
| `wireguard`, `openvpn`, `ipsec`, `zerotier`, `tailscale` | VPN services |
| `modems`, `sim_cards`, `messages`, `sms_utilities` | Mobile and SMS |
| `gps`, `input_output`, `modbus`, `serial` | Industrial / IoT features |
| `users`, `access_control`, `backup`, `system` | Administration |

Method names follow the API structure: `get_*` / `create_*` / `update_*` / `delete_*`
for configuration resources (with `_by_id` variants), and `<group>_actions_<action>`
for actions. See [`pytonika/endpoints/`](pytonika/endpoints/) for the full list of
160+ groups, or browse the [Teltonika API reference](https://developers.teltonika-networks.com/)
for request and response details.

## Development

```bash
# Clone and set up a virtual environment
git clone https://github.com/ikergcalvino/pytonika.git
cd pytonika
python -m venv .venv
source .venv/bin/activate

# Install in editable mode with all dev dependencies
pip install -e ".[dev]"

# Lint and format
ruff check .
ruff format --check .

# Type check
ty check pytonika

# Run tests
pytest

# Build and verify the package
python -m build && twine check dist/*
```

## Contributing

Contributions, bug reports and feature requests are welcome!
Check out the [Contributing guidelines](CONTRIBUTING.md) to get started.

## License

[MIT License](LICENSE)
