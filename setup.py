"""Setup."""
from setuptools import find_packages, setup

# Get packages from requirements.txt
with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="aiolyric",
    version="2.0.2",
    author="Aidan Timson (Timmo)",
    author_email="aidan@timmo.dev",
    description="Python package for the Honeywell Lyric Platform",
    keywords="aiolyric,api,async,asyncio,honeywell lyric,honeywell,lyric,integration",
    license="Apache-2.0",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/timmo001/aiolyric",
    install_requires=requirements,
    packages=find_packages(exclude=["tests", "generator"]),
    python_requires=">=3.11",
)
