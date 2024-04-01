"""Tests for the location object."""

from aiolyric.objects.location import LyricLocation


def test_location(location_fixture_response):
    """Test location object."""
    obj = LyricLocation(
        None,
        location_fixture_response,
    )
    assert obj.locationID == location_fixture_response["locationID"]
    assert obj.name == location_fixture_response["name"]
    assert obj.country == location_fixture_response["country"]
    assert obj.zipcode == location_fixture_response["zipcode"]
    assert (
        obj.devices[0].displayedOutdoorHumidity
        == location_fixture_response["devices"][0]["displayedOutdoorHumidity"]
    )
    assert (
        obj.devices[0].vacationHold.enabled
        == location_fixture_response["devices"][0]["vacationHold"]["enabled"]
    )
    assert (
        obj.devices[0].currentSchedulePeriod.day
        == location_fixture_response["devices"][0]["currentSchedulePeriod"]["day"]
    )
    assert (
        obj.devices[0].currentSchedulePeriod.period
        == location_fixture_response["devices"][0]["currentSchedulePeriod"]["period"]
    )
    assert (
        obj.devices[0].scheduleCapabilities.availableScheduleTypes
        == location_fixture_response["devices"][0]["scheduleCapabilities"][
            "availableScheduleTypes"
        ]
    )
    assert (
        obj.devices[0].scheduleCapabilities.schedulableFan
        == location_fixture_response["devices"][0]["scheduleCapabilities"][
            "schedulableFan"
        ]
    )
    assert (
        obj.devices[0].scheduleType.scheduleType
        == location_fixture_response["devices"][0]["scheduleType"]["scheduleType"]
    )
    assert (
        obj.devices[0].scheduleType.scheduleSubType
        == location_fixture_response["devices"][0]["scheduleType"]["scheduleSubType"]
    )
    assert (
        obj.devices[0].scheduleStatus
        == location_fixture_response["devices"][0]["scheduleStatus"]
    )
    assert (
        obj.devices[0].allowedTimeIncrements
        == location_fixture_response["devices"][0]["allowedTimeIncrements"]
    )
    assert (
        obj.devices[0].settings.hardwareSettings.brightness
        == location_fixture_response["devices"][0]["settings"]["hardwareSettings"][
            "brightness"
        ]
    )
    assert (
        obj.devices[0].settings.hardwareSettings.maxBrightness
        == location_fixture_response["devices"][0]["settings"]["hardwareSettings"][
            "maxBrightness"
        ]
    )
    assert (
        obj.devices[0].settings.temperatureMode.air
        == location_fixture_response["devices"][0]["settings"]["temperatureMode"]["air"]
    )
    assert (
        obj.devices[0].settings.devicePairingEnabled
        == location_fixture_response["devices"][0]["settings"]["devicePairingEnabled"]
    )
    assert (
        obj.devices[0].deviceClass
        == location_fixture_response["devices"][0]["deviceClass"]
    )
    assert (
        obj.devices[0].deviceType
        == location_fixture_response["devices"][0]["deviceType"]
    )
    assert (
        obj.devices[0].deviceID == location_fixture_response["devices"][0]["deviceID"]
    )
    assert obj.devices[0].name == location_fixture_response["devices"][0]["name"]
    assert obj.devices[0].isAlive == location_fixture_response["devices"][0]["isAlive"]
    assert (
        obj.devices[0].isUpgrading
        == location_fixture_response["devices"][0]["isUpgrading"]
    )
    assert (
        obj.devices[0].isProvisioned
        == location_fixture_response["devices"][0]["isProvisioned"]
    )
    assert obj.devices[0].macID == location_fixture_response["devices"][0]["macID"]
    assert (
        obj.devices[0].service.mode
        == location_fixture_response["devices"][0]["service"]["mode"]
    )
    assert (
        obj.devices[0].deviceRegistrationDate
        == location_fixture_response["devices"][0]["deviceRegistrationDate"]
    )
    assert (
        obj.devices[0].dataSyncStatus
        == location_fixture_response["devices"][0]["dataSyncStatus"]
    )
    assert obj.devices[0].units == location_fixture_response["devices"][0]["units"]
    assert (
        obj.devices[0].indoorTemperature
        == location_fixture_response["devices"][0]["indoorTemperature"]
    )
    assert (
        obj.devices[0].outdoorTemperature
        == location_fixture_response["devices"][0]["outdoorTemperature"]
    )
    assert (
        obj.devices[0].allowedModes
        == location_fixture_response["devices"][0]["allowedModes"]
    )
    assert (
        obj.devices[0].deadband == location_fixture_response["devices"][0]["deadband"]
    )
    assert (
        obj.devices[0].hasDualSetpointStatus
        == location_fixture_response["devices"][0]["hasDualSetpointStatus"]
    )
    assert (
        obj.devices[0].minHeatSetpoint
        == location_fixture_response["devices"][0]["minHeatSetpoint"]
    )
    assert (
        obj.devices[0].maxHeatSetpoint
        == location_fixture_response["devices"][0]["maxHeatSetpoint"]
    )
    assert (
        obj.devices[0].minCoolSetpoint
        == location_fixture_response["devices"][0]["minCoolSetpoint"]
    )
    assert (
        obj.devices[0].maxCoolSetpoint
        == location_fixture_response["devices"][0]["maxCoolSetpoint"]
    )
    assert (
        obj.devices[0].changeableValues.mode
        == location_fixture_response["devices"][0]["changeableValues"]["mode"]
    )
    assert (
        obj.devices[0].changeableValues.heatSetpoint
        == location_fixture_response["devices"][0]["changeableValues"]["heatSetpoint"]
    )
    assert (
        obj.devices[0].changeableValues.coolSetpoint
        == location_fixture_response["devices"][0]["changeableValues"]["coolSetpoint"]
    )
    assert (
        obj.devices[0].changeableValues.thermostatSetpointStatus
        == location_fixture_response["devices"][0]["changeableValues"][
            "thermostatSetpointStatus"
        ]
    )
    assert (
        obj.devices[0].changeableValues.nextPeriodTime
        == location_fixture_response["devices"][0]["changeableValues"]["nextPeriodTime"]
    )
    assert (
        obj.devices[0].changeableValues.heatCoolMode
        == location_fixture_response["devices"][0]["changeableValues"]["heatCoolMode"]
    )
    assert (
        obj.devices[0].changeableValues.endHeatSetpoint
        == location_fixture_response["devices"][0]["changeableValues"][
            "endHeatSetpoint"
        ]
    )
    assert (
        obj.devices[0].changeableValues.endCoolSetpoint
        == location_fixture_response["devices"][0]["changeableValues"][
            "endCoolSetpoint"
        ]
    )
    assert (
        obj.devices[0].operationStatus.mode
        == location_fixture_response["devices"][0]["operationStatus"]["mode"]
    )
    assert (
        obj.devices[0].operationStatus.fanRequest
        == location_fixture_response["devices"][0]["operationStatus"]["fanRequest"]
    )
    assert (
        obj.devices[0].operationStatus.circulationFanRequest
        == location_fixture_response["devices"][0]["operationStatus"][
            "circulationFanRequest"
        ]
    )
    assert (
        obj.devices[0].deviceModel
        == location_fixture_response["devices"][0]["deviceModel"]
    )
    assert obj.users[0].userID == location_fixture_response["users"][0]["userID"]
    assert obj.users[0].username == location_fixture_response["users"][0]["username"]
    assert obj.users[0].firstname == location_fixture_response["users"][0]["firstname"]
    assert obj.users[0].lastname == location_fixture_response["users"][0]["lastname"]
    assert obj.users[0].created == location_fixture_response["users"][0]["created"]
    assert obj.users[0].deleted == location_fixture_response["users"][0]["deleted"]
    assert obj.users[0].activated == location_fixture_response["users"][0]["activated"]
    assert (
        obj.users[0].connectedHomeAccountExists
        == location_fixture_response["users"][0]["connectedHomeAccountExists"]
    )
    assert (
        obj.users[0].locationRoleMapping[0].locationID
        == location_fixture_response["users"][0]["locationRoleMapping"][0]["locationID"]
    )
    assert (
        obj.users[0].locationRoleMapping[0].role
        == location_fixture_response["users"][0]["locationRoleMapping"][0]["role"]
    )
    assert (
        obj.users[0].locationRoleMapping[0].locationName
        == location_fixture_response["users"][0]["locationRoleMapping"][0][
            "locationName"
        ]
    )
    assert (
        obj.users[0].locationRoleMapping[0].status
        == location_fixture_response["users"][0]["locationRoleMapping"][0]["status"]
    )
    assert obj.users[0].isOptOut == location_fixture_response["users"][0]["isOptOut"]
    assert (
        obj.users[0].isCurrentUser
        == location_fixture_response["users"][0]["isCurrentUser"]
    )
    assert obj.timeZone == location_fixture_response["timeZone"]
    assert obj.ianaTimeZone == location_fixture_response["ianaTimeZone"]
    assert (
        obj.daylightSavingTimeEnabled
        == location_fixture_response["daylightSavingTimeEnabled"]
    )
    assert obj.geoFenceEnabled == location_fixture_response["geoFenceEnabled"]
    assert obj.predictiveAIREnabled == location_fixture_response["predictiveAIREnabled"]
    assert obj.comfortLevel == location_fixture_response["comfortLevel"]
    assert (
        obj.geoFenceNotificationEnabled
        == location_fixture_response["geoFenceNotificationEnabled"]
    )
    assert (
        obj.geoFenceNotificationTypeId
        == location_fixture_response["geoFenceNotificationTypeId"]
    )
    assert (
        obj.configuration.faceRecognition.enabled
        == location_fixture_response["configuration"]["faceRecognition"]["enabled"]
    )
    assert (
        obj.configuration.faceRecognition.maxPersons
        == location_fixture_response["configuration"]["faceRecognition"]["maxPersons"]
    )
    assert (
        obj.configuration.faceRecognition.maxEtas
        == location_fixture_response["configuration"]["faceRecognition"]["maxEtas"]
    )
    assert (
        obj.configuration.faceRecognition.maxEtaPersons
        == location_fixture_response["configuration"]["faceRecognition"][
            "maxEtaPersons"
        ]
    )
    assert (
        obj.configuration.faceRecognition.schedules[0].time[0].start
        == location_fixture_response["configuration"]["faceRecognition"]["schedules"][
            0
        ]["time"][0]["start"]
    )
    assert (
        obj.configuration.faceRecognition.schedules[0].time[0].end
        == location_fixture_response["configuration"]["faceRecognition"]["schedules"][
            0
        ]["time"][0]["end"]
    )
    assert (
        obj.configuration.faceRecognition.schedules[0].days
        == location_fixture_response["configuration"]["faceRecognition"]["schedules"][
            0
        ]["days"]
    )
