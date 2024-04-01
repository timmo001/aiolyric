"""Lyric."""

import logging

from aiohttp import ClientResponse

from .client import LyricClient
from .const import BASE_URL
from .objects.device import LyricDevice
from .objects.location import LyricLocation
from .objects.priority import LyricPriority, LyricRoom


class Lyric:
    """Handles authentication refresh tokens."""

    logger = logging.getLogger(__name__)

    def __init__(
        self,
        client: LyricClient,
        client_id: str,
    ) -> None:
        """Initialize the token manager class."""
        self._client = client
        self._client_id = client_id
        self._devices: list[LyricDevice] = []
        self._devices_dict: dict = {}
        self._locations: list[LyricLocation] = []
        self._locations_dict: dict = {}
        self._rooms_dict: dict = {}

    @property
    def client_id(self) -> str:
        """Return the client id."""
        return self._client_id

    @property
    def devices(self) -> list[LyricDevice]:
        """Return the devices."""
        return self._devices

    @property
    def devices_dict(self) -> dict:
        """Return the devices dict."""
        return self._devices_dict

    @property
    def locations(self) -> list[LyricLocation]:
        """Return the locations."""
        return self._locations

    @property
    def locations_dict(self) -> dict:
        """Return the locations dict."""
        return self._locations_dict

    @property
    def rooms_dict(self) -> dict[str, dict[str, LyricRoom]]:
        """Return the rooms dict."""
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
            self._devices_dict[device.mac_id] = device

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
            self._locations_dict[location.location_id] = location

    async def get_thermostat_rooms(
        self,
        location_id: int,
        device_id: str,
    ) -> None:
        """Get Priority, which contains accessory information."""
        response: ClientResponse = await self._client.get(
            f"{BASE_URL}/devices/thermostats/{device_id}/priority?apikey={self.client_id}&locationId={location_id}"
        )
        json = await response.json()
        self.logger.debug(json)

        priority = LyricPriority(json)

        # device id in the priority payload refers to the mac address of the device
        mac_id = priority.device_id
        self._rooms_dict[mac_id] = {}

        # add each room to the room dictionary. Rooms contain motion, temp, and humidity averages for all accessories in a room
        for room in priority.current_priority.rooms:
            self._rooms_dict[mac_id][room.id] = room

    async def update_thermostat(
        self,
        location: LyricLocation,
        device: LyricDevice,
        mode: str | None = None,
        heat_setpoint: int | float | None = None,
        cool_setpoint: int | float | None = None,
        auto_changeover_active: bool | None = None,
        thermostat_setpoint_status: str | None = None,
        next_period_time: str | None = None,
    ) -> ClientResponse:
        """Update Theremostat."""
        self.logger.debug("Update Thermostat")

        data = {}

        if mode is not None:
            data["mode"] = mode
        else:
            data["mode"] = device.changeable_values.mode

        if heat_setpoint is not None:
            data["heatSetpoint"] = heat_setpoint
        else:
            data["heatSetpoint"] = device.changeable_values.heat_setpoint
        if cool_setpoint is not None:
            data["coolSetpoint"] = cool_setpoint
        else:
            data["coolSetpoint"] = device.changeable_values.cool_setpoint

        # Only for TCC devices
        if auto_changeover_active is not None:
            data["autoChangeoverActive"] = auto_changeover_active
        elif device.changeable_values.auto_changeover_active is not None:
            data["autoChangeoverActive"] = (
                device.changeable_values.auto_changeover_active
            )

        # Only for LCC devices
        if thermostat_setpoint_status is not None:
            data["thermostatSetpointStatus"] = thermostat_setpoint_status
        elif device.changeable_values.thermostat_setpoint_status is not None:
            if device.changeable_values.thermostat_setpoint_status == "NoHold":
                data["thermostatSetpointStatus"] = "TemporaryHold"
            else:
                data["thermostatSetpointStatus"] = (
                    device.changeable_values.thermostat_setpoint_status
                )

        if data.get("thermostatSetpointStatus", "") == "HoldUntil":
            if next_period_time is not None:
                data["nextPeriodTime"] = next_period_time
            elif device.changeable_values.next_period_time == "NoHold" and mode is None:
                data["nextPeriodTime"] = "TemporaryHold"
            else:
                data["nextPeriodTime"] = device.changeable_values.next_period_time

        self.logger.debug(data)

        return await self._client.post(
            f"{BASE_URL}/devices/thermostats/{device.device_id}?apikey={self._client_id}&locationId={location.location_id}",
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

        data = {"mode": mode}

        self.logger.debug(data)

        return await self._client.post(
            f"{BASE_URL}/devices/thermostats/{device.device_id}/fan?apikey={self._client_id}&locationId={location.location_id}",
            json=data,
        )
