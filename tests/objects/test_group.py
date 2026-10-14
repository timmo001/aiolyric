"""Tests for the group object."""

from aiolyric.objects.group import LyricGroup


def test_group(group_fixture_response: dict):
    """Test group object."""
    obj = LyricGroup(group_fixture_response)
    assert obj.device_id == group_fixture_response["deviceId"]
    assert obj.group_id == group_fixture_response["groupId"]

    room = obj.rooms[0]
    room_response = group_fixture_response["rooms"][0]
    assert room.id == room_response["id"]
    assert room.name == room_response["name"]
    assert room.type == room_response["type"]
    assert room.avg_temperature == room_response["avgTemperature"]
    assert room.avg_humidity == room_response["avgHumidity"]

    accessory = room.accessories[0]
    accessory_response = room_response["accessories"][0]
    assert accessory.id == accessory_response["accessoryId"]

    attribute = accessory_response["accessoryAttribute"]
    assert accessory.attribute.type == attribute["type"]
    assert accessory.attribute.connection_method == attribute["connectionMethod"]
    assert accessory.attribute.name == attribute["name"]
    assert accessory.attribute.model == attribute["model"]
    assert accessory.attribute.serial_number == attribute["serialNumber"]
    assert accessory.attribute.software_revision == attribute["softwareRevision"]
    assert accessory.attribute.hardware_revision == attribute["hardwareRevision"]

    value = accessory_response["accessoryValue"]
    assert accessory.value.cool_setpoint == value["coolSetpoint"]
    assert accessory.value.heat_setpoint == value["heatSetpoint"]
    assert accessory.value.indoor_humidity == value["indoorHumidity"]
    assert accessory.value.indoor_temperature == value["indoorTemperature"]
    assert accessory.value.motion_detected == value["motionDet"]
    assert accessory.value.occupancy_detected == value["occupancyDet"]
    assert accessory.value.exclude_temp == value["excludeTemp"]
    assert accessory.value.exclude_motion == value["excludeMotion"]
    assert accessory.value.pressure == value["pressure"]
    assert accessory.value.occupancy_sensitivity == value["occupancySensitivity"]
    assert accessory.value.occupancy_timeout == value["occupancyTimeout"]
    assert accessory.value.status == value["status"]
    assert accessory.value.battery_status == value["batteryStatus"]
    assert accessory.value.rssi_average == value["rssiAverage"]
