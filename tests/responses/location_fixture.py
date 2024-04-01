"""Fixtures for location responses."""

import pytest


@pytest.fixture()
def location_fixture_response():
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
