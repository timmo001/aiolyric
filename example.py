"""Example usage of Lyric"""
import asyncio

from aiohttp import ClientSession

from lyric.client import LyricClient
from lyric.exceptions import LyricException, LyricAuthenticationException

CLIENT_ID = "abc123"
CODE = "123456"
REDIRECT_URL = "http://192.168.1.123:8123/auth/lyric/callback"


async def example():
    """Example usage of Lyric."""
    async with ClientSession() as session:
        try:
            client = LyricClient(session)
        except LyricAuthenticationException as err:
            print(f"Lyric authentication error: {err}")
        except LyricException as err:
            print(f"Lyric error: {err}")


asyncio.get_event_loop().run_until_complete(example())
