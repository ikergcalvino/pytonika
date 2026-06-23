# Contributing to Pytonika

Thanks for your interest in improving Pytonika! Contributions, bug reports and
feature requests are all welcome. This guide covers how to set up your
environment and the conventions the project follows.

> Pytonika is **not an official Teltonika library** and is not affiliated with
> Teltonika Networks. Endpoint and device definitions are derived from the
> public [Teltonika Web API reference](https://developers.teltonika-networks.com/).

## Ways to contribute

- **Report a bug** or **request a feature / new device / new endpoint** by
  opening an [issue](https://github.com/ikergcalvino/pytonika/issues) — there
  are dedicated templates for each.
- **Open a pull request** to fix a bug, add an endpoint, or add a device model.

## Development setup

An **editable install is required** — the package reads its own version via
`importlib.metadata`, so it must be installed to import correctly.

```bash
# Clone and enter the repository
git clone https://github.com/ikergcalvino/pytonika.git
cd pytonika

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# Install in editable mode with all dev dependencies
pip install -e ".[dev]"
```

## Branching and pull requests

- Branch off **`develop`** and target your pull request at **`develop`**.
  `main` is reserved for releases.
- Keep pull requests focused; one logical change per PR.
- Fill in the PR template and make sure the checklist passes before requesting
  review.
- Commit messages follow a [Conventional Commits](https://www.conventionalcommits.org/)
  style (`feat:`, `fix:`, `chore:`, `docs:`, …).

## Quality checks

CI runs lint, format, type-check and build-check on every push and pull request
to `main` and `develop`. Run them locally before pushing:

```bash
ruff check .                 # lint
ruff format --check .        # formatting (use `ruff format .` to fix)
ty check pytonika            # type checking
pytest                       # tests
python -m build              # build sdist + wheel
twine check dist/*           # validate package metadata
```

The codebase is fully typed (`py.typed`) and the `ANN` lint rules are enforced,
so **all public method signatures must have type hints**. Line length is 120 and
strings use double quotes (both enforced by ruff).

## Adding a new endpoint

Endpoints live in `pytonika/endpoints/`, one module per Web API feature area.
Each class inherits `Endpoint` and its methods build a path and delegate to the
shared `APIClient`, returning the raw JSON response as `dict[str, Any]`.

1. Create `pytonika/endpoints/<name>.py` with a class inheriting `Endpoint`.
   Each method defines `endpoint = "/path"` and calls
   `self._api_client.<get|post|put|delete>(...)`. Follow the existing naming
   convention: `get_*` / `create_*` / `update_*` / `delete_*` for resources
   (with `_by_id` variants), and `<group>_actions_<action>` for actions.
2. Register the class in `pytonika/endpoints/__init__.py` (alphabetical import
   and `__all__` entry).
3. Attach it in the `__init__` of every device class that supports it.

```python
from typing import Any

from ._base import Endpoint


class Example(Endpoint):
    def get_example_config(self) -> dict[str, Any]:
        """Returns the Example configuration."""
        endpoint = "/example/config"

        return self._api_client.get(endpoint)
```

## Adding a new device model

Device classes live in `pytonika/devices/`, grouped into four families
(`routers/`, `gateways/`, `access_points/`, `switches/`). Each model subclasses
its family base and declares the full set of endpoints it exposes — the model
files are intentionally repetitive because each model supports a different
subset of the API.

1. Create `pytonika/devices/<family>/<model>.py` subclassing the family base,
   calling `super().__init__()` and assigning the model's endpoint attributes.
2. Register it in the family `__init__.py`, in `pytonika/devices/__init__.py`,
   and in the `__all__` of `pytonika/__init__.py`.
3. Add the model to the supported-devices table in `README.md`.

When in doubt about which endpoints a model exposes, check the device's page in
the [Teltonika Web API reference](https://developers.teltonika-networks.com/).

## License

By contributing, you agree that your contributions will be licensed under the
[MIT License](LICENSE).
