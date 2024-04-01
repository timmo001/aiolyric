"""Fixtures for testing."""

from collections.abc import AsyncGenerator

from aiohttp import ClientSession
from aioresponses import aioresponses
import pytest

from aiolyric.client import LyricClient
from aiolyric.const import AUTH_URL, BASE_URL, TOKEN_URL

from . import RESPONSE_JSON_BASIC


@pytest.fixture(autouse=True)
def mock_aioresponse():
    """Return a client session."""
    with aioresponses() as mocker:
        mocker.get(
            AUTH_URL,
            payload=RESPONSE_JSON_BASIC,
            status=200,
            repeat=True,
        )
        mocker.get(
            TOKEN_URL,
            payload=RESPONSE_JSON_BASIC,
            status=200,
            repeat=True,
        )
        mocker.get(
            BASE_URL,
            payload=RESPONSE_JSON_BASIC,
            status=200,
            repeat=True,
        )

        yield mocker


@pytest.fixture
async def lyric_client() -> AsyncGenerator[LyricClient, None]:
    """Return a LyricClient."""
    async with ClientSession() as session:
        yield LyricClient(session=session)


@pytest.fixture()
def device_fixture_response() -> dict:
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


@pytest.fixture()
def location_fixture_response() -> dict:
    """Return a fixture response for a location."""
    return {
        "locationID": 123456,
        "name": "Home",
        "country": "GB",
        "zipcode": "AB12 3AB",
        "devices": [
            {
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
                "deviceID": "LCC-00D02DD9CADE",
                "userDefinedDeviceName": "Thermostat",
                "name": "Thermostat",
                "isAlive": True,
                "isUpgrading": False,
                "isProvisioned": True,
                "macID": "00D02DD9CADE",
                "deviceSettings": {},
                "service": {"mode": "Up"},
                "deviceRegistrationDate": "2019-04-04T19:32:20.4766667",
                "dataSyncStatus": "Initiated",
                "units": "Celsius",
                "indoorTemperature": 23,
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
        ],
        "users": [
            {
                "userID": 123456,
                "username": "example@example.com",
                "firstname": "Tim",
                "lastname": "Drake",
                "created": 1554403500,
                "deleted": -62135596800,
                "activated": True,
                "connectedHomeAccountExists": True,
                "locationRoleMapping": [
                    {
                        "locationID": 1214161,
                        "role": "Adult",
                        "locationName": "Home",
                        "status": 1,
                    }
                ],
                "isOptOut": "False",
                "isCurrentUser": True,
            }
        ],
        "timeZone": "GMT Standard Time",
        "ianaTimeZone": "Europe/London",
        "daylightSavingTimeEnabled": True,
        "geoFenceEnabled": False,
        "predictiveAIREnabled": False,
        "comfortLevel": 0,
        "geoFenceNotificationEnabled": False,
        "geoFenceNotificationTypeId": 13,
        "configuration": {
            "faceRecognition": {
                "enabled": False,
                "maxPersons": 10,
                "maxEtas": 2,
                "maxEtaPersons": 1,
                "schedules": [
                    {
                        "time": [{"start": "00:00:00", "end": "23:59:59"}],
                        "days": [
                            "Sunday",
                            "Monday",
                            "Tuesday",
                            "Wednesday",
                            "Thursday",
                            "Friday",
                            "Saturday",
                        ],
                    }
                ],
            }
        },
    }


@pytest.fixture()
def priority_fixture_response() -> dict:
    """Return a fixture response for a priority."""
    return {
        "deviceId": "00A01AB1ABCD",
        "status": "NoHold",
        "currentPriority": {
            "priorityType": "PickARoom",
            "selectedRooms": [0],
            "rooms": [
                {
                    "id": 0,
                    "roomName": "Hallway",
                    "roomAvgTemp": 76,
                    "roomAvgHumidity": 54,
                    "overallMotion": False,
                    "accessories": [
                        {
                            "id": 0,
                            "type": "Thermostat",
                            "excludeTemp": False,
                            "excludeMotion": False,
                            "temperature": 75.828,
                            "status": "Ok",
                            "detectMotion": False,
                        }
                    ],
                },
                {
                    "id": 1,
                    "roomName": "Office",
                    "roomAvgTemp": 76,
                    "roomAvgHumidity": 52,
                    "overallMotion": True,
                    "accessories": [
                        {
                            "id": 1,
                            "type": "IndoorAirSensor",
                            "excludeTemp": False,
                            "excludeMotion": False,
                            "temperature": 76,
                            "status": "Ok",
                            "detectMotion": True,
                        }
                    ],
                },
                {
                    "id": 2,
                    "roomName": "Master Bedroom",
                    "roomAvgTemp": 76,
                    "roomAvgHumidity": 52,
                    "overallMotion": False,
                    "accessories": [
                        {
                            "id": 2,
                            "type": "IndoorAirSensor",
                            "excludeTemp": False,
                            "excludeMotion": False,
                            "temperature": 76,
                            "status": "Ok",
                            "detectMotion": True,
                        }
                    ],
                },
            ],
        },
    }
