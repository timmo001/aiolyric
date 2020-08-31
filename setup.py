#!/usr/bin/env python
import io

from setuptools import setup, find_packages

version = "1.0.0"

setup(
    name="aiolyric",
    version=version,
    description="AIO package for the Honeywell Lyric Platform.",
    long_description=io.open("README.md", encoding="UTF-8").read(),
    keywords="honeywell lyric thermostat",
    author="Aidan Timson (Timmo)",
    author_email="contact@timmo.xyz",
    url="https://github.com/timmo001/aiolyric",
    packages=find_packages(exclude=["tests", "generator"]),
    install_requires=["aiohttp>=3.6.2"],
)
