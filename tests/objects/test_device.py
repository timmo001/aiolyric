"""Test device object."""

from aiolyric.objects.device import LyricDevice


def test_device(device_fixture_response):
    """Test device object."""
    obj = LyricDevice(
        None,
        device_fixture_response,
    )
    assert obj.locationID == device_fixture_response["locationID"]
    assert (
        obj.displayedOutdoorHumidity
        == device_fixture_response["displayedOutdoorHumidity"]
    )
    assert (
        obj.vacationHold.enabled == device_fixture_response["vacationHold"]["enabled"]
    )
    assert (
        obj.currentSchedulePeriod.day
        == device_fixture_response["currentSchedulePeriod"]["day"]
    )
    assert (
        obj.currentSchedulePeriod.period
        == device_fixture_response["currentSchedulePeriod"]["period"]
    )
    assert (
        obj.scheduleCapabilities.availableScheduleTypes[0]
        == device_fixture_response["scheduleCapabilities"]["availableScheduleTypes"][0]
    )
    assert (
        obj.scheduleCapabilities.schedulableFan
        == device_fixture_response["scheduleCapabilities"]["schedulableFan"]
    )
    assert (
        obj.scheduleType.scheduleType
        == device_fixture_response["scheduleType"]["scheduleType"]
    )
    assert (
        obj.scheduleType.scheduleSubType
        == device_fixture_response["scheduleType"]["scheduleSubType"]
    )
    assert obj.scheduleStatus == device_fixture_response["scheduleStatus"]
    assert obj.allowedTimeIncrements == device_fixture_response["allowedTimeIncrements"]
    assert (
        obj.settings.hardwareSettings.brightness
        == device_fixture_response["settings"]["hardwareSettings"]["brightness"]
    )
    assert (
        obj.settings.hardwareSettings.maxBrightness
        == device_fixture_response["settings"]["hardwareSettings"]["maxBrightness"]
    )
    assert (
        obj.settings.temperatureMode.air
        == device_fixture_response["settings"]["temperatureMode"]["air"]
    )
    assert (
        obj.settings.devicePairingEnabled
        == device_fixture_response["settings"]["devicePairingEnabled"]
    )
    assert obj.deviceClass == device_fixture_response["deviceClass"]
    assert obj.deviceType == device_fixture_response["deviceType"]
    assert obj.deviceID == device_fixture_response["deviceID"]
    assert obj.name == device_fixture_response["name"]
    assert obj.isAlive == device_fixture_response["isAlive"]
    assert obj.isUpgrading == device_fixture_response["isUpgrading"]
    assert obj.isProvisioned == device_fixture_response["isProvisioned"]
    assert obj.macID == device_fixture_response["macID"]
    assert obj.service.mode == device_fixture_response["service"]["mode"]
    assert (
        obj.deviceRegistrationDate == device_fixture_response["deviceRegistrationDate"]
    )
    assert obj.dataSyncStatus == device_fixture_response["dataSyncStatus"]
    assert obj.units == device_fixture_response["units"]
    assert obj.indoorTemperature == device_fixture_response["indoorTemperature"]
    assert obj.outdoorTemperature == device_fixture_response["outdoorTemperature"]
    assert obj.allowedModes[0] == device_fixture_response["allowedModes"][0]
    assert obj.deadband == device_fixture_response["deadband"]
    assert obj.hasDualSetpointStatus == device_fixture_response["hasDualSetpointStatus"]
    assert obj.minHeatSetpoint == device_fixture_response["minHeatSetpoint"]
    assert obj.maxHeatSetpoint == device_fixture_response["maxHeatSetpoint"]
    assert obj.minCoolSetpoint == device_fixture_response["minCoolSetpoint"]
    assert obj.maxCoolSetpoint == device_fixture_response["maxCoolSetpoint"]
    assert (
        obj.changeableValues.mode == device_fixture_response["changeableValues"]["mode"]
    )
    assert (
        obj.changeableValues.heatSetpoint
        == device_fixture_response["changeableValues"]["heatSetpoint"]
    )
    assert (
        obj.changeableValues.coolSetpoint
        == device_fixture_response["changeableValues"]["coolSetpoint"]
    )
    assert (
        obj.changeableValues.thermostatSetpointStatus
        == device_fixture_response["changeableValues"]["thermostatSetpointStatus"]
    )
    assert (
        obj.changeableValues.nextPeriodTime
        == device_fixture_response["changeableValues"]["nextPeriodTime"]
    )
    assert (
        obj.changeableValues.heatCoolMode
        == device_fixture_response["changeableValues"]["heatCoolMode"]
    )
    assert (
        obj.changeableValues.endHeatSetpoint
        == device_fixture_response["changeableValues"]["endHeatSetpoint"]
    )
    assert (
        obj.changeableValues.endCoolSetpoint
        == device_fixture_response["changeableValues"]["endCoolSetpoint"]
    )
    assert (
        obj.operationStatus.mode == device_fixture_response["operationStatus"]["mode"]
    )
    assert (
        obj.operationStatus.fanRequest
        == device_fixture_response["operationStatus"]["fanRequest"]
    )
    assert (
        obj.operationStatus.circulationFanRequest
        == device_fixture_response["operationStatus"]["circulationFanRequest"]
    )
    assert obj.deviceModel == device_fixture_response["deviceModel"]
