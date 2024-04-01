"""Tests for the Priority object."""

from aiolyric.objects.priority import LyricPriority


def test_priority(priority_fixture_response: dict):
    """Test priority object."""
    obj = LyricPriority(priority_fixture_response)
    assert obj.device_id == priority_fixture_response["deviceId"]
    assert obj.status == priority_fixture_response["status"]
    assert (
        obj.current_priority.priority_type
        == priority_fixture_response["currentPriority"]["priorityType"]
    )
    assert (
        obj.current_priority.selected_rooms[0]
        == priority_fixture_response["currentPriority"]["selectedRooms"][0]
    )
    assert (
        obj.current_priority.rooms[0].id
        == priority_fixture_response["currentPriority"]["rooms"][0]["id"]
    )
    assert (
        obj.current_priority.rooms[0].room_name
        == priority_fixture_response["currentPriority"]["rooms"][0]["roomName"]
    )
    assert (
        obj.current_priority.rooms[0].room_avg_temp
        == priority_fixture_response["currentPriority"]["rooms"][0]["roomAvgTemp"]
    )
    assert (
        obj.current_priority.rooms[0].room_avg_humidity
        == priority_fixture_response["currentPriority"]["rooms"][0]["roomAvgHumidity"]
    )
    assert (
        obj.current_priority.rooms[0].overall_motion
        == priority_fixture_response["currentPriority"]["rooms"][0]["overallMotion"]
    )
    assert (
        obj.current_priority.rooms[0].accessories[0].id
        == priority_fixture_response["currentPriority"]["rooms"][0]["accessories"][0][
            "id"
        ]
    )
    assert (
        obj.current_priority.rooms[0].accessories[0].type
        == priority_fixture_response["currentPriority"]["rooms"][0]["accessories"][0][
            "type"
        ]
    )
    assert (
        obj.current_priority.rooms[0].accessories[0].exclude_temp
        == priority_fixture_response["currentPriority"]["rooms"][0]["accessories"][0][
            "excludeTemp"
        ]
    )
    assert (
        obj.current_priority.rooms[0].accessories[0].exclude_motion
        == priority_fixture_response["currentPriority"]["rooms"][0]["accessories"][0][
            "excludeMotion"
        ]
    )
    assert (
        obj.current_priority.rooms[0].accessories[0].temperature
        == priority_fixture_response["currentPriority"]["rooms"][0]["accessories"][0][
            "temperature"
        ]
    )
    assert (
        obj.current_priority.rooms[0].accessories[0].status
        == priority_fixture_response["currentPriority"]["rooms"][0]["accessories"][0][
            "status"
        ]
    )
    assert (
        obj.current_priority.rooms[0].accessories[0].detect_motion
        == priority_fixture_response["currentPriority"]["rooms"][0]["accessories"][0][
            "detectMotion"
        ]
    )
