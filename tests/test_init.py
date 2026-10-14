"""Test the lyric module."""

from copy import deepcopy
from typing import Any

from aioresponses import aioresponses
from aioresponses.core import normalize_url
import pytest

from aiolyric import Lyric
from aiolyric.client import LyricClient
from aiolyric.const import BASE_URL
from aiolyric.objects.device import LyricDevice
from aiolyric.objects.location import LyricLocation

from . import RESPONSE_JSON_DEVICE, RESPONSE_JSON_LOCATION

THERMOSTAT_URL = (
    f"{BASE_URL}/devices/thermostats/LCC-00A01AB1ABCD?apikey=test&locationId=123456"
)
PRIORITY_URL = f"{BASE_URL}/devices/thermostats/LCC-00A01AB1ABCD/priority?apikey=test&locationId=123456"


def last_sent_json(mocker: aioresponses, method: str, url: str) -> Any:
    """Return the JSON body of the last request made to a URL."""
    return mocker.requests[(method, normalize_url(url))][-1].kwargs["json"]


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

    await lyric.update_priority(
        lyric.locations[0],
        lyric.devices[0],
        "PickARoom",
        [0, 1],
    )

    await lyric.update_priority(
        lyric.locations[0],
        lyric.devices[0],
        "FollowMe",
    )

    await lyric.update_priority(
        lyric.locations[0],
        lyric.devices[0],
        "WholeHouse",
    )


@pytest.mark.parametrize(
    ("changeable_values", "kwargs", "expected"),
    [
        pytest.param(
            {},
            {},
            {
                "mode": "Heat",
                "heatSetpoint": 15,
                "coolSetpoint": 28,
                "autoChangeoverActive": False,
                "thermostatSetpointStatus": "TemporaryHold",
            },
            id="defaults_from_device_and_no_hold_becomes_temporary",
        ),
        pytest.param(
            {},
            {"mode": "Cool", "heat_setpoint": 18, "cool_setpoint": 24},
            {
                "mode": "Cool",
                "heatSetpoint": 18,
                "coolSetpoint": 24,
                "autoChangeoverActive": False,
                "thermostatSetpointStatus": "TemporaryHold",
            },
            id="explicit_values_override_device",
        ),
        pytest.param(
            {"thermostatSetpointStatus": "PermanentHold"},
            {},
            {
                "mode": "Heat",
                "heatSetpoint": 15,
                "coolSetpoint": 28,
                "autoChangeoverActive": False,
                "thermostatSetpointStatus": "PermanentHold",
            },
            id="existing_hold_is_kept",
        ),
        pytest.param(
            {},
            {"thermostat_setpoint_status": "HoldUntil", "next_period_time": "22:00:00"},
            {
                "mode": "Heat",
                "heatSetpoint": 15,
                "coolSetpoint": 28,
                "autoChangeoverActive": False,
                "thermostatSetpointStatus": "HoldUntil",
                "nextPeriodTime": "22:00:00",
            },
            id="hold_until_sends_given_time",
        ),
        pytest.param(
            {},
            {"thermostat_setpoint_status": "HoldUntil"},
            {
                "mode": "Heat",
                "heatSetpoint": 15,
                "coolSetpoint": 28,
                "autoChangeoverActive": False,
                "thermostatSetpointStatus": "HoldUntil",
                "nextPeriodTime": "19:00:00",
            },
            id="hold_until_falls_back_to_device_time",
        ),
        pytest.param(
            {"autoChangeoverActive": None, "thermostatSetpointStatus": None},
            {},
            {"mode": "Heat", "heatSetpoint": 15, "coolSetpoint": 28},
            id="omits_values_the_device_does_not_report",
        ),
    ],
)
async def test_update_thermostat_payload(
    mock_aioresponse: aioresponses,
    lyric_client: LyricClient,
    changeable_values: dict[str, Any],
    kwargs: dict[str, Any],
    expected: dict[str, Any],
) -> None:
    """Test the thermostat update sends the expected values."""
    device_json = deepcopy(RESPONSE_JSON_DEVICE)
    device_json["changeableValues"].update(changeable_values)
    lyric = Lyric(lyric_client, "test")

    await lyric.update_thermostat(
        LyricLocation(lyric_client, RESPONSE_JSON_LOCATION),
        LyricDevice(lyric_client, device_json),
        **kwargs,
    )

    assert last_sent_json(mock_aioresponse, "POST", THERMOSTAT_URL) == expected


@pytest.mark.parametrize(
    ("rooms", "expected"),
    [
        pytest.param(
            [0, 1],
            {"currentPriority": {"priorityType": "PickARoom", "selectedRooms": [0, 1]}},
            id="with_rooms",
        ),
        pytest.param(
            None,
            {"currentPriority": {"priorityType": "PickARoom"}},
            id="without_rooms",
        ),
    ],
)
async def test_update_priority_payload(
    mock_aioresponse: aioresponses,
    lyric_client: LyricClient,
    rooms: list[int] | None,
    expected: dict[str, Any],
) -> None:
    """Test the priority update is a PUT and only sends rooms when given."""
    lyric = Lyric(lyric_client, "test")

    await lyric.update_priority(
        LyricLocation(lyric_client, RESPONSE_JSON_LOCATION),
        LyricDevice(lyric_client, RESPONSE_JSON_DEVICE),
        "PickARoom",
        rooms,
    )

    assert last_sent_json(mock_aioresponse, "PUT", PRIORITY_URL) == expected
