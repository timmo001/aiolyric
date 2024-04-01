"""Test the lytic client module."""

from aioresponses import aioresponses
import pytest

from aiolyric.client import LyricClient
from aiolyric.const import BASE_URL
from aiolyric.exceptions import LyricAuthenticationException, LyricException


@pytest.mark.asyncio
async def test_get(
    mock_aioresponse: aioresponses,
    lyric_client: LyricClient,
) -> None:
    """Test the get method."""
    mock_aioresponse.get(
        BASE_URL,
        payload={"test": "test"},
    )
    response = await lyric_client.get(BASE_URL)
    assert response.status == 200
    assert await response.json() == {"test": "test"}


@pytest.mark.asyncio
async def test_post(
    mock_aioresponse: aioresponses,
    lyric_client: LyricClient,
) -> None:
    """Test the post method."""
    mock_aioresponse.post(
        BASE_URL,
        payload={"test": "test"},
    )
    response = await lyric_client.post(BASE_URL)
    assert response.status == 200
    assert await response.json() == {"test": "test"}


@pytest.mark.asyncio
async def test_request(
    mock_aioresponse: aioresponses,
    lyric_client: LyricClient,
) -> None:
    """Test the request method."""
    mock_aioresponse.get(
        BASE_URL,
        payload={"test": "test"},
    )
    response = await lyric_client.request(
        "GET",
        BASE_URL,
    )
    assert response.status == 200
    assert await response.json() == {"test": "test"}

    mock_aioresponse.post(
        BASE_URL,
        payload={"test": "test"},
    )
    response = await lyric_client.request(
        "POST",
        BASE_URL,
    )
    assert response.status == 200
    assert await response.json() == {"test": "test"}


@pytest.mark.asyncio
async def test_authentication_exception(
    mock_aioresponse: aioresponses,
    lyric_client: LyricClient,
) -> None:
    """Test the request method with an authentication error."""
    mock_aioresponse.clear()
    mock_aioresponse.get(
        BASE_URL,
        status=401,
        payload={"test": "test"},
    )
    with pytest.raises(LyricAuthenticationException):
        await lyric_client.request(
            "GET",
            BASE_URL,
        )


@pytest.mark.asyncio
async def test_exception(
    mock_aioresponse: aioresponses,
    lyric_client: LyricClient,
) -> None:
    """Test the request method with an error."""
    mock_aioresponse.clear()
    mock_aioresponse.get(
        BASE_URL,
        status=500,
        payload={"test": "test"},
    )
    with pytest.raises(LyricException):
        await lyric_client.request(
            "GET",
            BASE_URL,
        )
