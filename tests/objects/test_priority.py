"""Tests for the Priority object."""

from aiolyric.objects.priority import LyricAccessory, LyricPriority, LyricRoom


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


def test_priority_classic_schema(priority_classic_fixture_response: dict):
    """Test priority object with the classic response schema.

    Resideo still serves this schema to part of its accounts, so both key
    sets must parse to the same values.
    """
    obj = LyricPriority(priority_classic_fixture_response)
    assert obj.device_id == "00A01AB1ABCD"
    assert obj.status == "NoHold"
    assert obj.current_priority.priority_type == "PickARoom"
    assert obj.current_priority.selected_rooms == [0]

    rooms = obj.current_priority.rooms
    assert len(rooms) == 2
    assert rooms[0].id == 0
    assert rooms[0].room_name == "Hallway"
    assert rooms[0].room_avg_temp == 76
    assert rooms[0].room_avg_humidity == 54
    assert rooms[0].overall_motion is False
    assert rooms[1].room_name == "Office"
    assert rooms[1].overall_motion is True

    accessory = rooms[1].accessories[0]
    assert accessory.id == 1
    assert accessory.type == "IndoorAirSensor"
    assert accessory.exclude_temp is False
    assert accessory.exclude_motion is False
    assert accessory.temperature == 76
    assert accessory.status == "Ok"
    assert accessory.detect_motion is True


def test_priority_missing_keys():
    """Test defaults when a payload carries neither schema's keys."""
    obj = LyricPriority({})
    assert obj.device_id == ""
    assert obj.status == ""
    assert obj.current_priority.priority_type == ""
    assert obj.current_priority.rooms == []

    room = LyricRoom({})
    assert room.room_name == ""
    assert room.room_avg_temp is None
    assert room.room_avg_humidity is None

    accessory = LyricAccessory({})
    assert accessory.type == ""
    assert accessory.exclude_temp is False
