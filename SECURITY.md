# Security Policy

Pytonika is a client library for the Teltonika Networks Web API. This document
explains which versions receive security fixes, how to report a vulnerability,
and where the boundaries of the project lie.

## Supported versions

Pytonika is pre-1.0 and under active development. Security fixes are released
for the **latest version** on [PyPI](https://pypi.org/project/pytonika/) only.
Please confirm that an issue reproduces on the latest release before reporting it.

| Version        | Supported |
|----------------|-----------|
| Latest release | ✅        |
| Older releases | ❌        |

## Reporting a vulnerability

> [!IMPORTANT]
> Please **do not** report security vulnerabilities through public GitHub
> issues, discussions or pull requests.

Report vulnerabilities privately through GitHub's
[private vulnerability reporting](https://github.com/ikergcalvino/pytonika/security/advisories/new).
If that is not possible, email the maintainer at **iker.gcalvino@udc.es**.

Please include:

- A description of the vulnerability and its potential impact.
- Steps to reproduce or a minimal proof of concept.
- The affected Pytonika, Python and `httpx` versions.

### What to expect

- **Acknowledgement** within 5 business days.
- **Initial assessment** — whether the report is accepted, and its severity —
  within 10 business days.
- **Fix and disclosure** coordinated with you. Once a fix is released, a
  GitHub Security Advisory is published and the reporter is credited unless
  they prefer to remain anonymous.

Please allow a reasonable amount of time for a fix before disclosing the issue
publicly.

## Scope

### In scope

Vulnerabilities in Pytonika's own code, for example:

- Leakage of credentials or session tokens (e.g. through logs, exceptions or
  object representations).
- Insecure defaults, such as TLS verification being disabled without the user
  explicitly requesting it.
- Requests being sent to an unintended endpoint or host as a result of how the
  library builds URLs or request bodies.
- Issues in the packaging or release process that could compromise the
  published distribution.

### Out of scope

- **Vulnerabilities in Teltonika devices, firmware, the Web API itself or RMS.**
  Pytonika is not affiliated with Teltonika Networks and cannot fix these.
  Please report them directly to
  [Teltonika Networks](https://teltonika-networks.com/) through their official
  support channels.
- Vulnerabilities in third-party dependencies such as `httpx`, which should be
  reported to their respective maintainers. Reports about Pytonika depending
  on a vulnerable version are welcome.
- Insecure usage that the user explicitly opts into, such as disabling TLS
  verification or connecting over plain `http://`.

## Using Pytonika securely

These points come from how the device API works rather than from Pytonika
itself, but they matter for operating it safely:

- **Credentials and tokens.** `authentication.login()` sends the username and
  password to the device and keeps the returned Bearer token in memory for the
  lifetime of the client. Treat both as secrets: load them from environment
  variables or a secrets manager, never hard-code or commit them, and call
  `authentication.logout()` and `close()` (or use the device as a context
  manager) when you are done.
- **TLS verification.** TLS verification is enabled by default. Teltonika
  devices usually ship with a self-signed certificate, so connections fail
  unless you either provide a trusted CA bundle or pass `verify=False`.
  Disabling verification exposes the connection to man-in-the-middle attacks
  and should be limited to local, trusted networks. To keep it enabled, issue
  the device a certificate whose subject alternative names include the
  address you use to reach it (IP or hostname).
- **Transport.** Always connect over HTTPS. `http://` sends credentials and
  tokens in clear text.
- **Least privilege.** Use a dedicated device account with only the
  permissions your automation needs rather than the administrator account.
