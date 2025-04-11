#!/usr/bin/env python3

from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="teltonika-api",
    version="0.1.0",
    author="Iker García Calviño",
    author_email="iker.gcalvino@udc.es",
    description="API client for Teltonika routers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ikergcalvino/teltonika-api",
    project_urls={
        "Bug Tracker": "https://github.com/ikergcalvino/teltonika-api/issues",
        "Documentation": "https://github.com/ikergcalvino/teltonika-api#readme",
        "Source Code": "https://github.com/ikergcalvino/teltonika-api",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: System :: Networking",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="teltonika, router, api, networking",
    packages=[
        "teltonika_api",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.12.0",
            "black>=21.5b2",
            "isort>=5.9.1",
            "mypy>=0.812",
            "flake8>=3.9.2",
        ],
        "docs": [
            "sphinx>=4.0.2",
            "sphinx-rtd-theme>=0.5.2",
        ],
    },
)
