"""Test the http client module."""

from aioresponses import aioresponses
import pytest

from aiolyric.client import LyricClient


@pytest.mark.asyncio
async def test_authorize(
    mock_aioresponse: aioresponses,
    lyric_client: LyricClient,
) -> None:
    """Test the authorize method."""
