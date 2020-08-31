"""Lyric: Init"""
from aiohttp import ClientError, ClientSession, ClientResponse
from asyncio import CancelledError, TimeoutError, get_event_loop
from datetime import datetime, timedelta
from typing import List

from .objects.base import LyricBase
from .const import BASE_URL
from .exceptions import LyricException, LyricAuthenticationException
from .objects.device import LyricDevice
from .objects.location import LyricLocation


class Lyric(LyricBase):
    """Handles authentication refresh tokens."""

    def __init__(self, client: "LyricClient", client_id: str) -> None:
        """Initialize the token manager class."""
        self._client = client
        self._client_id = client_id
        self._devices: List[LyricDevice] = []
        self._locations: List[LyricLocation] = []

    @property
    def client_id(self) -> str:
        return self._client_id

    @property
    def devices(self) -> List[LyricDevice]:
        return self._devices

    @property
    def locations(self) -> List[LyricLocation]:
        return self._locations

    async def get_devices(self, location_id: int) -> None:
        """Get Devices."""
        response: ClientResponse = await self._client.get(
            f"{BASE_URL}/devices?apikey={self.client_id}&locationId={location_id}"
        )
        json = await response.json()
        self.logger.debug(json)
        devices = []
        for device in json:
            devices.append(LyricDevice(self._client, device))
        self._devices = devices

    async def get_locations(self) -> None:
        """Get Locations."""
        response: ClientResponse = await self._client.get(
            f"{BASE_URL}/locations?apikey={self.client_id}"
        )
        json = await response.json()
        self.logger.debug(json)
        locations = []
        for location in json:
            locations.append(LyricLocation(self._client, location))
        self._locations = locations
