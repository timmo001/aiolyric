"""Fixtures for testing."""

from collections.abc import AsyncGenerator

from aiohttp import ClientSession
from aioresponses import aioresponses
import pytest

from aiolyric.client import LyricClient
from aiolyric.const import AUTH_URL, BASE_URL, TOKEN_URL

from . import RESPONSE_JSON_BASIC


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

        yield mocker


@pytest.fixture
async def lyric_client() -> AsyncGenerator[LyricClient, None]:
    """Return a LyricClient."""
    async with ClientSession() as session:
        yield LyricClient(session=session)
