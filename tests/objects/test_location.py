"""Tests for the location object."""

from aiolyric.client import LyricClient
from aiolyric.objects.location import LyricLocation


def test_location(
    location_fixture_response: dict,
    lyric_client: LyricClient,
):
    """Test location object."""
    obj = LyricLocation(
        lyric_client,
        location_fixture_response,
    )
    assert obj.location_id == location_fixture_response["locationID"]
    assert obj.name == location_fixture_response["name"]
    assert obj.country == location_fixture_response["country"]
    assert obj.zipcode == location_fixture_response["zipcode"]
    assert isinstance(obj.devices_dict, dict)
    assert (
        obj.devices[0].displayed_outdoor_humidity
        == location_fixture_response["devices"][0]["displayedOutdoorHumidity"]
    )
    assert (
        obj.devices[0].vacation_hold.enabled
        == location_fixture_response["devices"][0]["vacationHold"]["enabled"]
    )
    assert (
        obj.devices[0].current_schedule_period.day
        == location_fixture_response["devices"][0]["currentSchedulePeriod"]["day"]
    )
    assert (
        obj.devices[0].current_schedule_period.period
        == location_fixture_response["devices"][0]["currentSchedulePeriod"]["period"]
    )
    assert (
        obj.devices[0].schedule_capabilities.available_schedule_types
        == location_fixture_response["devices"][0]["scheduleCapabilities"][
            "availableScheduleTypes"
        ]
    )
    assert (
        obj.devices[0].schedule_capabilities.schedulable_fan
        == location_fixture_response["devices"][0]["scheduleCapabilities"][
            "schedulableFan"
        ]
    )
    assert (
        obj.devices[0].schedule_type.schedule_type
        == location_fixture_response["devices"][0]["scheduleType"]["scheduleType"]
    )
    assert (
        obj.devices[0].schedule_type.schedule_sub_type
        == location_fixture_response["devices"][0]["scheduleType"]["scheduleSubType"]
    )
    assert (
        obj.devices[0].schedule_status
        == location_fixture_response["devices"][0]["scheduleStatus"]
    )
    assert (
        obj.devices[0].allowed_time_increments
        == location_fixture_response["devices"][0]["allowedTimeIncrements"]
    )
    assert (
        obj.devices[0].settings.hardware_settings.brightness
        == location_fixture_response["devices"][0]["settings"]["hardwareSettings"][
            "brightness"
        ]
    )
    assert (
        obj.devices[0].settings.hardware_settings.max_brightness
        == location_fixture_response["devices"][0]["settings"]["hardwareSettings"][
            "maxBrightness"
        ]
    )
    assert (
        obj.devices[0].settings.temperature_mode.air
        == location_fixture_response["devices"][0]["settings"]["temperatureMode"]["air"]
    )
    assert (
        obj.devices[0].settings.device_pairing_enabled
        == location_fixture_response["devices"][0]["settings"]["devicePairingEnabled"]
    )
    assert (
        obj.devices[0].device_class
        == location_fixture_response["devices"][0]["deviceClass"]
    )
    assert (
        obj.devices[0].device_type
        == location_fixture_response["devices"][0]["deviceType"]
    )
    assert (
        obj.devices[0].device_id == location_fixture_response["devices"][0]["deviceID"]
    )
    assert obj.devices[0].name == location_fixture_response["devices"][0]["name"]
    assert obj.devices[0].is_alive == location_fixture_response["devices"][0]["isAlive"]
    assert (
        obj.devices[0].is_upgrading
        == location_fixture_response["devices"][0]["isUpgrading"]
    )
    assert (
        obj.devices[0].is_provisioned
        == location_fixture_response["devices"][0]["isProvisioned"]
    )
    assert obj.devices[0].mac_id == location_fixture_response["devices"][0]["macID"]
    assert (
        obj.devices[0].service.mode
        == location_fixture_response["devices"][0]["service"]["mode"]
    )
    assert (
        obj.devices[0].device_registration_date
        == location_fixture_response["devices"][0]["deviceRegistrationDate"]
    )
    assert (
        obj.devices[0].data_sync_status
        == location_fixture_response["devices"][0]["dataSyncStatus"]
    )
    assert obj.devices[0].units == location_fixture_response["devices"][0]["units"]
    assert (
        obj.devices[0].indoor_temperature
        == location_fixture_response["devices"][0]["indoorTemperature"]
    )
    assert (
        obj.devices[0].outdoor_temperature
        == location_fixture_response["devices"][0]["outdoorTemperature"]
    )
    assert (
        obj.devices[0].allowed_modes
        == location_fixture_response["devices"][0]["allowedModes"]
    )
    assert (
        obj.devices[0].deadband == location_fixture_response["devices"][0]["deadband"]
    )
    assert (
        obj.devices[0].has_dual_setpoint_status
        == location_fixture_response["devices"][0]["hasDualSetpointStatus"]
    )
    assert (
        obj.devices[0].min_heat_setpoint
        == location_fixture_response["devices"][0]["minHeatSetpoint"]
    )
    assert (
        obj.devices[0].max_heat_setpoint
        == location_fixture_response["devices"][0]["maxHeatSetpoint"]
    )
    assert (
        obj.devices[0].min_cool_setpoint
        == location_fixture_response["devices"][0]["minCoolSetpoint"]
    )
    assert (
        obj.devices[0].max_cool_setpoint
        == location_fixture_response["devices"][0]["maxCoolSetpoint"]
    )
    assert (
        obj.devices[0].changeable_values.mode
        == location_fixture_response["devices"][0]["changeableValues"]["mode"]
    )
    assert (
        obj.devices[0].changeable_values.heat_setpoint
        == location_fixture_response["devices"][0]["changeableValues"]["heatSetpoint"]
    )
    assert (
        obj.devices[0].changeable_values.cool_setpoint
        == location_fixture_response["devices"][0]["changeableValues"]["coolSetpoint"]
    )
    assert (
        obj.devices[0].changeable_values.thermostat_setpoint_status
        == location_fixture_response["devices"][0]["changeableValues"][
            "thermostatSetpointStatus"
        ]
    )
    assert (
        obj.devices[0].changeable_values.next_period_time
        == location_fixture_response["devices"][0]["changeableValues"]["nextPeriodTime"]
    )
    assert (
        obj.devices[0].changeable_values.heat_cool_mode
        == location_fixture_response["devices"][0]["changeableValues"]["heatCoolMode"]
    )
    assert (
        obj.devices[0].changeable_values.end_heat_setpoint
        == location_fixture_response["devices"][0]["changeableValues"][
            "endHeatSetpoint"
        ]
    )
    assert (
        obj.devices[0].changeable_values.end_cool_setpoint
        == location_fixture_response["devices"][0]["changeableValues"][
            "endCoolSetpoint"
        ]
    )
    assert (
        obj.devices[0].operation_status.mode
        == location_fixture_response["devices"][0]["operationStatus"]["mode"]
    )
    assert (
        obj.devices[0].operation_status.fan_request
        == location_fixture_response["devices"][0]["operationStatus"]["fanRequest"]
    )
    assert (
        obj.devices[0].operation_status.circulation_fan_request
        == location_fixture_response["devices"][0]["operationStatus"][
            "circulationFanRequest"
        ]
    )
    assert (
        obj.devices[0].device_model
        == location_fixture_response["devices"][0]["deviceModel"]
    )
    assert obj.users[0].user_id == location_fixture_response["users"][0]["userID"]
    assert obj.users[0].username == location_fixture_response["users"][0]["username"]
    assert obj.users[0].first_name == location_fixture_response["users"][0]["firstname"]
    assert obj.users[0].last_name == location_fixture_response["users"][0]["lastname"]
    assert obj.users[0].created == location_fixture_response["users"][0]["created"]
    assert obj.users[0].deleted == location_fixture_response["users"][0]["deleted"]
    assert obj.users[0].activated == location_fixture_response["users"][0]["activated"]
    assert (
        obj.users[0].connected_home_account_exists
        == location_fixture_response["users"][0]["connectedHomeAccountExists"]
    )
    assert (
        obj.users[0].location_role_mapping[0].location_id
        == location_fixture_response["users"][0]["locationRoleMapping"][0]["locationID"]
    )
    assert (
        obj.users[0].location_role_mapping[0].role
        == location_fixture_response["users"][0]["locationRoleMapping"][0]["role"]
    )
    assert (
        obj.users[0].location_role_mapping[0].location_name
        == location_fixture_response["users"][0]["locationRoleMapping"][0][
            "locationName"
        ]
    )
    assert (
        obj.users[0].location_role_mapping[0].status
        == location_fixture_response["users"][0]["locationRoleMapping"][0]["status"]
    )
    assert obj.users[0].is_opt_out == location_fixture_response["users"][0]["isOptOut"]
    assert (
        obj.users[0].is_current_user
        == location_fixture_response["users"][0]["isCurrentUser"]
    )
    assert obj.time_zone == location_fixture_response["timeZone"]
    assert obj.iana_time_zone == location_fixture_response["ianaTimeZone"]
    assert (
        obj.daylight_saving_time_enabled
        == location_fixture_response["daylightSavingTimeEnabled"]
    )
    assert obj.geo_fence_enabled == location_fixture_response["geoFenceEnabled"]
    assert (
        obj.predictive_air_enabled == location_fixture_response["predictiveAIREnabled"]
    )
    assert obj.comfort_level == location_fixture_response["comfortLevel"]
    assert (
        obj.geo_fence_notification_enabled
        == location_fixture_response["geoFenceNotificationEnabled"]
    )
    assert (
        obj.geo_fence_notification_type_id
        == location_fixture_response["geoFenceNotificationTypeId"]
    )
    assert (
        obj.configuration.face_recognition.enabled
        == location_fixture_response["configuration"]["faceRecognition"]["enabled"]
    )
    assert (
        obj.configuration.face_recognition.max_persons
        == location_fixture_response["configuration"]["faceRecognition"]["maxPersons"]
    )
    assert (
        obj.configuration.face_recognition.max_etas
        == location_fixture_response["configuration"]["faceRecognition"]["maxEtas"]
    )
    assert (
        obj.configuration.face_recognition.max_eta_persons
        == location_fixture_response["configuration"]["faceRecognition"][
            "maxEtaPersons"
        ]
    )
    assert (
        obj.configuration.face_recognition.schedules[0].time[0].start
        == location_fixture_response["configuration"]["faceRecognition"]["schedules"][
            0
        ]["time"][0]["start"]
    )
    assert (
        obj.configuration.face_recognition.schedules[0].time[0].end
        == location_fixture_response["configuration"]["faceRecognition"]["schedules"][
            0
        ]["time"][0]["end"]
    )
    assert (
        obj.configuration.face_recognition.schedules[0].days
        == location_fixture_response["configuration"]["faceRecognition"]["schedules"][
            0
        ]["days"]
    )
