"""Fixtures for testing."""

from collections.abc import AsyncGenerator

from aiohttp import ClientSession
from aioresponses import aioresponses
import pytest

from aiolyric.client import LyricClient
from aiolyric.const import AUTH_URL, BASE_URL, TOKEN_URL

from . import (
    RESPONSE_JSON_BASIC,
    RESPONSE_JSON_DEVICE,
    RESPONSE_JSON_LOCATION,
    RESPONSE_JSON_PRIORITY,
)


@pytest.fixture(autouse=True)
def mock_aioresponse():
    """Return a client session."""
    with aioresponses() as mocker:
        mocker.get(
            AUTH_URL,
            payload=RESPONSE_JSON_BASIC,
            status=200,
            repeat=True,
        )
        mocker.get(
            TOKEN_URL,
            payload=RESPONSE_JSON_BASIC,
            status=200,
            repeat=True,
        )
        mocker.get(
            BASE_URL,
            payload=RESPONSE_JSON_BASIC,
            status=200,
            repeat=True,
        )
        mocker.get(
            f"{BASE_URL}/devices?apikey=test&locationId=1",
            payload=[RESPONSE_JSON_DEVICE],
            status=200,
            repeat=True,
        )
        mocker.get(
            f"{BASE_URL}/locations?apikey=test",
            payload=[RESPONSE_JSON_LOCATION],
            status=200,
            repeat=True,
        )
        mocker.get(
            f"{BASE_URL}/devices/thermostats/test/priority?apikey=test&locationId=1",
            payload=RESPONSE_JSON_PRIORITY,
            status=200,
            repeat=True,
        )
        mocker.post(
            f"{BASE_URL}/devices/thermostats/LCC-00A01AB1ABCD?apikey=test&locationId=123456",
            payload=RESPONSE_JSON_BASIC,
            status=200,
            repeat=True,
        )

        yield mocker


@pytest.fixture
async def lyric_client() -> AsyncGenerator[LyricClient, None]:
    """Return a LyricClient."""
    async with ClientSession() as session:
        yield LyricClient(session=session)


@pytest.fixture()
def device_fixture_response() -> dict:
    """Return a fixture response for a device."""
    return RESPONSE_JSON_DEVICE


@pytest.fixture()
def location_fixture_response() -> dict:
    """Return a fixture response for a location."""
    return RESPONSE_JSON_LOCATION


@pytest.fixture()
def priority_fixture_response() -> dict:
    """Return a fixture response for a priority."""
    return RESPONSE_JSON_PRIORITY
