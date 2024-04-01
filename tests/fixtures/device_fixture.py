"""Fixtures for device tests."""

import pytest


@pytest.fixture()
def device_fixture_response():
    """Return a fixture response for a device."""
    return {
        "locationID": 123456,
        "displayedOutdoorHumidity": 51,
        "vacationHold": {"enabled": False},
        "currentSchedulePeriod": {"day": "Monday", "period": "P2"},
        "scheduleCapabilities": {
            "availableScheduleTypes": ["None", "Geofenced", "TimedEmea"],
            "schedulableFan": False,
        },
        "scheduleType": {"scheduleType": "Timed", "scheduleSubType": "EMEA"},
        "scheduleStatus": "Resume",
        "allowedTimeIncrements": 10,
        "settings": {
            "hardwareSettings": {"brightness": 5, "maxBrightness": 5},
            "temperatureMode": {"air": True},
            "specialMode": {},
            "devicePairingEnabled": True,
        },
        "deviceClass": "Thermostat",
        "deviceType": "Thermostat",
        "deviceID": "LCC-00A01AB1ABCD",
        "name": "Thermostat",
        "isAlive": True,
        "isUpgrading": False,
        "isProvisioned": True,
        "macID": "00A01AB1ABCD",
        "deviceSettings": {},
        "service": {"mode": "Up"},
        "deviceRegistrationDate": "2019-01-01T19:32:20.4766667",
        "dataSyncStatus": "Initiated",
        "units": "Celsius",
        "indoorTemperature": 23.5,
        "outdoorTemperature": 16,
        "allowedModes": ["Heat", "Off"],
        "deadband": 0,
        "hasDualSetpointStatus": False,
        "minHeatSetpoint": 5,
        "maxHeatSetpoint": 35,
        "minCoolSetpoint": -18,
        "maxCoolSetpoint": -18,
        "changeableValues": {
            "mode": "Heat",
            "heatSetpoint": 15,
            "coolSetpoint": 28,
            "thermostatSetpointStatus": "NoHold",
            "nextPeriodTime": "19:00:00",
            "heatCoolMode": "Heat",
            "endHeatSetpoint": None,
            "endCoolSetpoint": None,
        },
        "operationStatus": {
            "mode": "EquipmentOff",
            "fanRequest": False,
            "circulationFanRequest": False,
        },
        "deviceModel": "T5-T6",
    }
