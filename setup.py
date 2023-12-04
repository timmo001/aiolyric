#!/usr/bin/env python
import io

from setuptools import find_packages, setup

version = "1.1.1"

setup(
    name="aiolyric",
    version=version,
    description="AIO package for the Honeywell Lyric Platform.",
    long_description=io.open("README.md", encoding="UTF-8").read(),
    keywords="honeywell lyric thermostat",
    author="Aidan Timson (Timmo)",
    author_email="contact@timmo.xyz",
    license="MIT",
    url="https://github.com/timmo001/aiolyric",
    packages=find_packages(exclude=["tests", "generator"]),
    install_requires=["aiohttp>=3.7.3"],
)
