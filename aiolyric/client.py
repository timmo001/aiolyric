"""Lyric client."""

from abc import abstractmethod
import asyncio
import logging

from aiohttp import ClientResponse, ClientSession

from .exceptions import LyricAuthenticationException, LyricException


class LyricClient:
    """Client to handle API calls."""

    logger = logging.getLogger(__name__)

    def __init__(
        self,
        session: ClientSession,
    ) -> None:
        """Initialize the client."""
        self._session = session

    @abstractmethod
    async def async_get_access_token(self) -> str:
        """Return a valid access token."""

    async def get(
        self,
        url: str,
        **kwargs,
    ) -> ClientResponse:
        """Make a GET request."""
        return await self.request("GET", url, **kwargs)

    async def post(
        self,
        url: str,
        **kwargs,
    ) -> ClientResponse:
        """Make a POST request."""
        return await self.request(
            "POST",
            url,
            **kwargs,
        )

    async def request(
        self,
        method: str,
        url: str,
        **kwargs,
    ) -> ClientResponse:
        """Make a request."""
        if (headers := kwargs.get("headers")) is None:
            headers = {}

        access_token = await self.async_get_access_token()
        headers["Authorization"] = f"Bearer {access_token}"
        headers["Content-Type"] = "application/json"

        async with asyncio.timeout(20):
            response: ClientResponse = await self._session.request(
                method,
                url,
                headers=headers,
                **kwargs,
            )
        if response.status != 200:
            if response.status == 401:
                raise LyricAuthenticationException(
                    {
                        "request": {
                            "method": method,
                            "url": url,
                            "headers": headers,
                            **kwargs,
                        },
                        "response": await response.json(),
                        "status": response.status,
                    }
                )
            raise LyricException(
                {
                    "request": {
                        "method": method,
                        "url": url,
                        "headers": headers,
                        **kwargs,
                    },
                    "response": await response.json(),
                    "status": response.status,
                }
            )
        return response
