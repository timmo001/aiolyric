"""Lyric base."""

import logging

from ..client import LyricClient


class LyricBase:
    """Base class for Lyric."""

    logger = logging.getLogger(__name__)

    def __init__(self, attributes) -> None:
        """Initialize."""
        self.attributes = attributes


class LyricBaseClient(LyricBase):
    """Base class for Lyric."""

    def __init__(
        self,
        client: LyricClient,
        attributes: dict,
    ) -> None:
        """Initialise."""
        super().__init__(attributes)
        self.client = client
