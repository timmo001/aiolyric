"""Tests for the Priority object."""

from aiolyric.objects.priority import LyricPriority


def test_priority(priority_fixture_response: dict):
    """Test priority object."""
    obj = LyricPriority(priority_fixture_response)
    assert obj.deviceId == priority_fixture_response["deviceId"]
    assert obj.status == priority_fixture_response["status"]
    assert (
        obj.currentPriority.priorityType
        == priority_fixture_response["currentPriority"]["priorityType"]
    )
    assert (
        obj.currentPriority.selectedRooms[0]
        == priority_fixture_response["currentPriority"]["selectedRooms"][0]
    )
    assert (
        obj.currentPriority.rooms[0].id
        == priority_fixture_response["currentPriority"]["rooms"][0]["id"]
    )
    assert (
        obj.currentPriority.rooms[0].roomName
        == priority_fixture_response["currentPriority"]["rooms"][0]["roomName"]
    )
    assert (
        obj.currentPriority.rooms[0].roomAvgTemp
        == priority_fixture_response["currentPriority"]["rooms"][0]["roomAvgTemp"]
    )
    assert (
        obj.currentPriority.rooms[0].roomAvgHumidity
        == priority_fixture_response["currentPriority"]["rooms"][0]["roomAvgHumidity"]
    )
    assert (
        obj.currentPriority.rooms[0].overallMotion
        == priority_fixture_response["currentPriority"]["rooms"][0]["overallMotion"]
    )
    assert (
        obj.currentPriority.rooms[0].accessories[0].id
        == priority_fixture_response["currentPriority"]["rooms"][0]["accessories"][0][
            "id"
        ]
    )
    assert (
        obj.currentPriority.rooms[0].accessories[0].type
        == priority_fixture_response["currentPriority"]["rooms"][0]["accessories"][0][
            "type"
        ]
    )
    assert (
        obj.currentPriority.rooms[0].accessories[0].excludeTemp
        == priority_fixture_response["currentPriority"]["rooms"][0]["accessories"][0][
            "excludeTemp"
        ]
    )
    assert (
        obj.currentPriority.rooms[0].accessories[0].excludeMotion
        == priority_fixture_response["currentPriority"]["rooms"][0]["accessories"][0][
            "excludeMotion"
        ]
    )
    assert (
        obj.currentPriority.rooms[0].accessories[0].temperature
        == priority_fixture_response["currentPriority"]["rooms"][0]["accessories"][0][
            "temperature"
        ]
    )
    assert (
        obj.currentPriority.rooms[0].accessories[0].status
        == priority_fixture_response["currentPriority"]["rooms"][0]["accessories"][0][
            "status"
        ]
    )
    assert (
        obj.currentPriority.rooms[0].accessories[0].detectMotion
        == priority_fixture_response["currentPriority"]["rooms"][0]["accessories"][0][
            "detectMotion"
        ]
    )
