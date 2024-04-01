"""Test device object."""

from aiolyric.client import LyricClient
from aiolyric.objects.device import DeviceSettings, LyricDevice, SettingsSpecialMode


def test_device(
    device_fixture_response: dict,
    lyric_client: LyricClient,
):
    """Test device object."""
    obj = LyricDevice(lyric_client, device_fixture_response)
    assert obj.location_id == device_fixture_response["locationID"]
    assert obj.indoor_humidity == device_fixture_response["indoorHumidity"]
    assert (
        obj.displayed_outdoor_humidity
        == device_fixture_response["displayedOutdoorHumidity"]
    )
    assert (
        obj.vacation_hold.enabled == device_fixture_response["vacationHold"]["enabled"]
    )
    assert (
        obj.current_schedule_period.day
        == device_fixture_response["currentSchedulePeriod"]["day"]
    )
    assert (
        obj.current_schedule_period.period
        == device_fixture_response["currentSchedulePeriod"]["period"]
    )
    assert (
        obj.schedule_capabilities.available_schedule_types[0]
        == device_fixture_response["scheduleCapabilities"]["availableScheduleTypes"][0]
    )
    assert (
        obj.schedule_capabilities.schedulable_fan
        == device_fixture_response["scheduleCapabilities"]["schedulableFan"]
    )
    assert (
        obj.schedule_type.schedule_type
        == device_fixture_response["scheduleType"]["scheduleType"]
    )
    assert (
        obj.schedule_type.schedule_sub_type
        == device_fixture_response["scheduleType"]["scheduleSubType"]
    )
    assert obj.schedule_status == device_fixture_response["scheduleStatus"]
    assert (
        obj.allowed_time_increments == device_fixture_response["allowedTimeIncrements"]
    )
    assert (
        obj.settings.hardware_settings.brightness
        == device_fixture_response["settings"]["hardwareSettings"]["brightness"]
    )
    assert (
        obj.settings.hardware_settings.max_brightness
        == device_fixture_response["settings"]["hardwareSettings"]["maxBrightness"]
    )
    assert (
        obj.settings.temperature_mode.air
        == device_fixture_response["settings"]["temperatureMode"]["air"]
    )
    assert isinstance(obj.settings.special_mode, SettingsSpecialMode)
    assert (
        obj.settings.device_pairing_enabled
        == device_fixture_response["settings"]["devicePairingEnabled"]
    )
    assert obj.device_class == device_fixture_response["deviceClass"]
    assert obj.device_type == device_fixture_response["deviceType"]
    assert obj.device_id == device_fixture_response["deviceID"]
    assert obj.name == device_fixture_response["name"]
    assert obj.is_alive == device_fixture_response["isAlive"]
    assert obj.is_upgrading == device_fixture_response["isUpgrading"]
    assert obj.is_provisioned == device_fixture_response["isProvisioned"]
    assert obj.mac_id == device_fixture_response["macID"]
    assert isinstance(obj.device_settings, DeviceSettings)
    assert obj.service.mode == device_fixture_response["service"]["mode"]
    assert (
        obj.device_registration_date
        == device_fixture_response["deviceRegistrationDate"]
    )
    assert obj.data_sync_status == device_fixture_response["dataSyncStatus"]
    assert obj.units == device_fixture_response["units"]
    assert obj.indoor_temperature == device_fixture_response["indoorTemperature"]
    assert obj.outdoor_temperature == device_fixture_response["outdoorTemperature"]
    assert obj.allowed_modes[0] == device_fixture_response["allowedModes"][0]
    assert obj.deadband == device_fixture_response["deadband"]
    assert (
        obj.has_dual_setpoint_status == device_fixture_response["hasDualSetpointStatus"]
    )
    assert obj.min_heat_setpoint == device_fixture_response["minHeatSetpoint"]
    assert obj.max_heat_setpoint == device_fixture_response["maxHeatSetpoint"]
    assert obj.min_cool_setpoint == device_fixture_response["minCoolSetpoint"]
    assert obj.max_cool_setpoint == device_fixture_response["maxCoolSetpoint"]
    assert (
        obj.changeable_values.auto_changeover_active
        == device_fixture_response["changeableValues"]["autoChangeoverActive"]
    )
    assert (
        obj.changeable_values.emergency_heat_active
        == device_fixture_response["changeableValues"]["emergencyHeatActive"]
    )
    assert (
        obj.changeable_values.mode
        == device_fixture_response["changeableValues"]["mode"]
    )
    assert (
        obj.changeable_values.heat_setpoint
        == device_fixture_response["changeableValues"]["heatSetpoint"]
    )
    assert (
        obj.changeable_values.cool_setpoint
        == device_fixture_response["changeableValues"]["coolSetpoint"]
    )
    assert (
        obj.changeable_values.thermostat_setpoint_status
        == device_fixture_response["changeableValues"]["thermostatSetpointStatus"]
    )
    assert (
        obj.changeable_values.next_period_time
        == device_fixture_response["changeableValues"]["nextPeriodTime"]
    )
    assert (
        obj.changeable_values.heat_cool_mode
        == device_fixture_response["changeableValues"]["heatCoolMode"]
    )
    assert (
        obj.changeable_values.end_heat_setpoint
        == device_fixture_response["changeableValues"]["endHeatSetpoint"]
    )
    assert (
        obj.changeable_values.end_cool_setpoint
        == device_fixture_response["changeableValues"]["endCoolSetpoint"]
    )
    assert (
        obj.operation_status.mode == device_fixture_response["operationStatus"]["mode"]
    )
    assert (
        obj.operation_status.fan_request
        == device_fixture_response["operationStatus"]["fanRequest"]
    )
    assert (
        obj.operation_status.circulation_fan_request
        == device_fixture_response["operationStatus"]["circulationFanRequest"]
    )
    assert obj.device_model == device_fixture_response["deviceModel"]
    assert obj.fan_mode == device_fixture_response["fanMode"]
