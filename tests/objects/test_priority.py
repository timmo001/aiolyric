"""Tests for the Priority object."""

from aiolyric.objects.priority import LyricPriority


def test_priority(priority_fixture_response: dict):
    """Test priority object."""
    obj = LyricPriority(priority_fixture_response)
    assert obj.device_id == priority_fixture_response["deviceId"]
    assert obj.status == priority_fixture_response["priorityStatus"]
    assert (
        obj.current_priority.priority_type
        == priority_fixture_response["priority"]["priorityType"]
    )
    assert (
        obj.current_priority.selected_rooms[0]
        == priority_fixture_response["priority"]["selectedRooms"][0]
    )
    assert (
        obj.current_priority.rooms[0].id
        == priority_fixture_response["priority"]["rooms"][0]["id"]
    )
    assert (
        obj.current_priority.rooms[0].room_name
        == priority_fixture_response["priority"]["rooms"][0]["name"]
    )
    assert (
        obj.current_priority.rooms[0].room_avg_temp
        == priority_fixture_response["priority"]["rooms"][0]["avgTemperature"]
    )
    assert (
        obj.current_priority.rooms[0].room_avg_humidity
        == priority_fixture_response["priority"]["rooms"][0]["avgHumidity"]
    )
    assert (
        obj.current_priority.rooms[0].overall_motion
        == priority_fixture_response["priority"]["rooms"][0]["overallMotion"]
    )
    assert (
        obj.current_priority.rooms[0].accessories[0].id
        == priority_fixture_response["priority"]["rooms"][0]["accessories"][0]["id"]
    )
    assert (
        obj.current_priority.rooms[0].accessories[0].type
        == priority_fixture_response["priority"]["rooms"][0]["accessories"][0][
            "sensorType"
        ]
    )
    assert (
        obj.current_priority.rooms[0].accessories[0].exclude_temp
        == priority_fixture_response["priority"]["rooms"][0]["accessories"][0][
            "excludeTemperature"
        ]
    )
    assert (
        obj.current_priority.rooms[0].accessories[0].exclude_motion
        == priority_fixture_response["priority"]["rooms"][0]["accessories"][0][
            "excludeMotion"
        ]
    )
    assert (
        obj.current_priority.rooms[0].accessories[0].temperature
        == priority_fixture_response["priority"]["rooms"][0]["accessories"][0][
            "temperature"
        ]
    )
    assert (
        obj.current_priority.rooms[0].accessories[0].status
        == priority_fixture_response["priority"]["rooms"][0]["accessories"][0]["status"]
    )
    assert (
        obj.current_priority.rooms[0].accessories[0].detect_motion
        == priority_fixture_response["priority"]["rooms"][0]["accessories"][0][
            "detectMotion"
        ]
    )
