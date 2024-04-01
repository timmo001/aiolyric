"""Fixture for priority response."""

import pytest


@pytest.fixture()
def priority_fixture_response():
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
