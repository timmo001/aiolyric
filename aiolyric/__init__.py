"""Lyric: Init"""
from typing import List

from aiohttp import ClientResponse

from .const import BASE_URL
from .objects.base import LyricBase
from .objects.device import LyricDevice
from .objects.location import LyricLocation
from .objects.priority import LyricPriority, LyricRoom


class Lyric(LyricBase):
    """Handles authentication refresh tokens."""

    def __init__(
        self,
        client: "LyricClient",
        client_id: str,
    ) -> None:
        """Initialize the token manager class."""
        self._client = client
        self._client_id = client_id
        self._devices: List[LyricDevice] = []
        self._devices_dict: dict = {}
        self._locations: List[LyricLocation] = []
        self._locations_dict: dict = {}
        self._rooms_dict: dict = {}    

    @property
    def client_id(self) -> str:
        return self._client_id

    @property
    def devices(self) -> List[LyricDevice]:
        return self._devices

    @property
    def devices_dict(self) -> dict:
        return self._devices_dict

    @property
    def locations(self) -> List[LyricLocation]:
        return self._locations

    @property
    def locations_dict(self) -> dict:
        return self._locations_dict

    @property
    def rooms_dict(self) -> dict[str, dict[str, LyricRoom]]:
        return self._rooms_dict

    async def get_devices(
        self,
        location_id: int,
    ) -> None:
        """Get Devices."""
        response: ClientResponse = await self._client.get(
            f"{BASE_URL}/devices?apikey={self.client_id}&locationId={location_id}"
        )
        json = await response.json()
        self.logger.debug(json)
        self._devices = [LyricDevice(self._client, device) for device in json or []]
        self._devices_dict: dict = {}
        for device in self._devices:
            self._devices_dict[device.macID] = device

    async def get_locations(self) -> None:
        """Get Locations."""
        response: ClientResponse = await self._client.get(
            f"{BASE_URL}/locations?apikey={self.client_id}"
        )
        json = await response.json()
        self.logger.debug(json)
        self._locations = [
            LyricLocation(self._client, location) for location in json or []
        ]
        self._locations_dict: dict = {}
        for location in self._locations:
            self._locations_dict[location.locationID] = location

    async def get_thermostat_rooms(
            self,
            location_id: int,
            device_id: str
        ) -> None:
        """Get Priority, which contains accessory information."""
        response: ClientResponse = await self._client.get(
            f"{BASE_URL}/devices/thermostats/{device_id}/priority?apikey={self.client_id}&locationId={location_id}"
        )
        json = await response.json()
        self.logger.debug(json)
        
        priority = LyricPriority(json)

        macId = priority.deviceId   # device id in the priority payload refers to the mac address of the device
        self._rooms_dict[macId]: dict = {}
        
        # add each room to the room dictionary. Rooms contain motion, temp, and humidity averages for all accessories in a room
        for room in priority.currentPriority.rooms:
            self._rooms_dict[macId][room.id] = room

    async def update_thermostat(
        self,
        location: LyricLocation,
        device: LyricDevice,
        mode=None,
        heatSetpoint=None,
        coolSetpoint=None,
        autoChangeoverActive=None,
        thermostatSetpointStatus=None,
        nextPeriodTime=None,
    ) -> ClientResponse:
        """Update Theremostat."""
        self.logger.debug("Update Thermostat")

        data = {}

        if mode is not None:
            data["mode"] = mode
        else:
            data["mode"] = device.changeableValues.mode

        if heatSetpoint is not None:
            data["heatSetpoint"] = heatSetpoint
        else:
            data["heatSetpoint"] = device.changeableValues.heatSetpoint
        if coolSetpoint is not None:
            data["coolSetpoint"] = coolSetpoint
        else:
            data["coolSetpoint"] = device.changeableValues.coolSetpoint

        # Only for TCC devices
        if autoChangeoverActive is not None:
            data["autoChangeoverActive"] = autoChangeoverActive
        elif device.changeableValues.autoChangeoverActive is not None:
            data["autoChangeoverActive"] = device.changeableValues.autoChangeoverActive

        # Only for LCC devices
        if thermostatSetpointStatus is not None:
            data["thermostatSetpointStatus"] = thermostatSetpointStatus
        elif device.changeableValues.thermostatSetpointStatus is not None:
            if device.changeableValues.thermostatSetpointStatus == "NoHold":
                data["thermostatSetpointStatus"] = "TemporaryHold"
            else:
                data[
                    "thermostatSetpointStatus"
                ] = device.changeableValues.thermostatSetpointStatus

        if data.get("thermostatSetpointStatus", "") == "HoldUntil":
            if nextPeriodTime is not None:
                data["nextPeriodTime"] = nextPeriodTime
            elif device.changeableValues.nextPeriodTime == "NoHold" and mode is None:
                data["nextPeriodTime"] = "TemporaryHold"
            else:
                data["nextPeriodTime"] = device.changeableValues.nextPeriodTime

        self.logger.debug(data)

        return await self._client.post(
            f"{BASE_URL}/devices/thermostats/{device.deviceID}?apikey={self._client_id}&locationId={location.locationID}",
            json=data,
        )

    async def update_fan(
        self,
        location: LyricLocation,
        device: LyricDevice,
        mode: str,
    ) -> ClientResponse:
        """Update Fan."""
        self.logger.debug("Update Fan")

        data = {}

        if mode is not None:
            data["mode"] = mode
        else:
            data["mode"] = device.fanMode

        self.logger.debug(data)

        return await self._client.post(
            f"{BASE_URL}/devices/thermostats/{device.deviceID}/fan?apikey={self._client_id}&locationId={location.locationID}",
            json=data,
        )
