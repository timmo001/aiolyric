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

    def __init__(self, client: "LyricClient") -> None:
        """Initialize the token manager class."""
        self._client = client
        self._devices: List[LyricDevice] = None
        self._locations: List[LyricLocation] = None

    @property
    def devices(self) -> List[LyricDevice]:
        return self._devices

    @property
    def locations(self) -> List[LyricLocation]:
        return self._locations

    async def get_devices(self, client_id: str, location_id: int) -> None:
        """Get Devices."""
        response: ClientResponse = await self._client.get(
            f"{BASE_URL}/devices?apikey={client_id}&locationId={location_id}"
        )
        self._devices = [
            LyricDevice(self._client, device) for device in await response.json() or []
        ]

    async def get_locations(self, client_id: str) -> None:
        """Get Locations."""
        response: ClientResponse = await self._client.get(
            f"{BASE_URL}/locations?apikey={client_id}"
        )
        self.locations = [
            LyricLocation(self._client, location)
            for location in await response.json() or []
        ]
