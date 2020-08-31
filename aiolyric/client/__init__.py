"""Lyric: Client"""
import async_timeout
import logging

from abc import abstractmethod
from asyncio import CancelledError, TimeoutError, get_event_loop
from aiohttp import ClientError, ClientSession, ClientResponse

from ..base import LyricBase
from ..exceptions import LyricException, LyricAuthenticationException


class LyricClient(LyricBase):
    """Client to handle API calls."""

    def __init__(self, session: ClientSession) -> None:
        """Initialize the client."""
        self._session = session

    @abstractmethod
    async def async_get_access_token(self) -> str:
        """Return a valid access token."""

    async def get(self, url: str, **kwargs) -> ClientResponse:
        """Make a GET request."""
        return await self.request("GET", url, **kwargs)

    async def post(self, url: str, **kwargs) -> ClientResponse:
        """Make a POST request."""
        return await self.request("POST", url, **kwargs)

    async def request(
        self, method: str in ["GET", "POST"], url: str, **kwargs
    ) -> ClientResponse:
        """Make a request."""
        headers = kwargs.get("headers")

        if headers is None:
            headers = {}
        else:
            headers = dict(headers)

        access_token = await self.async_get_access_token()
        headers["authorization"] = f"Bearer {access_token}"

        async with async_timeout.timeout(20, loop=get_event_loop()):
            response: ClientResponse = await self._session.request(
                method,
                url,
                **kwargs,
                headers=headers,
            )
        if response.status != 200:
            if response.status == 401:
                raise LyricAuthenticationException(
                    {
                        "request": {"method": method, "url": url, "headers": headers},
                        "status": response.status,
                        "text": await response.json(),
                    }
                )
            else:
                raise LyricException(
                    {
                        "request": {"method": method, "url": url, "headers": headers},
                        "status": response.status,
                        "text": await response.text(),
                    }
                )
        return response
