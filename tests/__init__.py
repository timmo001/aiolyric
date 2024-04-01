"""Setup for tests."""

from typing import Final

RESPONSE_JSON_BASIC: Final[dict] = {"test": "test"}

RESPONSE_JSON_DEVICE: Final[dict] = {
    "locationID": 123456,
    "indoorHumidity": 51,
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
        "autoChangeoverActive": False,
        "emergencyHeatActive": False,
        "heatSetpoint": 15,
        "coolSetpoint": 28,
        "thermostatSetpointStatus": "NoHold",
        "nextPeriodTime": "19:00:00",
        "endHeatSetpoint": 62,
        "endCoolSetpoint": 85,
        "heatCoolMode": "Heat",
    },
    "operationStatus": {
        "mode": "EquipmentOff",
        "fanRequest": False,
        "circulationFanRequest": False,
    },
    "deviceModel": "T5-T6",
    "fanMode": "Auto",
}

RESPONSE_JSON_LOCATION: Final[dict] = {
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

RESPONSE_JSON_PRIORITY: Final[dict] = {
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
