"""Test the lyric module."""

from aioresponses import aioresponses
import pytest

from aiolyric import Lyric
from aiolyric.client import LyricClient


@pytest.mark.asyncio
async def test_lyric(
    mock_aioresponse: aioresponses,
    lyric_client: LyricClient,
) -> None:
    """Test the lyric class."""
    lyric = Lyric(lyric_client, "test")
    assert lyric.client_id == "test"
    assert isinstance(lyric.devices, list)
    assert isinstance(lyric.devices_dict, dict)
    assert isinstance(lyric.locations, list)
    assert isinstance(lyric.locations_dict, dict)
    assert isinstance(lyric.rooms_dict, dict)

    await lyric.get_devices(1)
    assert isinstance(lyric.devices, list)
    assert isinstance(lyric.devices_dict, dict)

    await lyric.get_locations()
    assert isinstance(lyric.locations, list)
    assert isinstance(lyric.locations_dict, dict)

    thermostat_rooms = await lyric.get_thermostat_rooms(1, "test")
    assert thermostat_rooms is None
    assert isinstance(lyric.rooms_dict, dict)

    await lyric.update_thermostat(
        lyric.locations[0],
        lyric.devices[0],
    )

    await lyric.update_thermostat(
        lyric.locations[0],
        lyric.devices[0],
        "NoHold",
    )

    await lyric.update_thermostat(
        lyric.locations[0],
        lyric.devices[0],
        "HoldUntil",
    )

    await lyric.update_thermostat(
        lyric.locations[0],
        lyric.devices[0],
        "HoldUntil",
        75,
        20,
        True,
        "test",
        "10:00:00",
    )

    await lyric.update_fan(
        lyric.locations[0],
        lyric.devices[0],
        "auto",
    )
